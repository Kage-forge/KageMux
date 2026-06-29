import json
import subprocess
import threading
import zlib
import re
import sys
import shutil
import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext, messagebox
from pathlib import Path
from typing import Dict, List, Any, Callable, Optional

CONFIG_FILE = Path("kagemux_config.json")

def get_resource_path(relative_path: str) -> Path:
    """Ensures the app can find assets (like the icon) when packaged as an .exe via PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = Path(__file__).resolve().parent
    return Path(base_path) / relative_path

def load_config() -> Dict[str, str]:
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {"mkvmerge_exe": "", "ffmpeg_exe": ""}

def save_config(config: Dict[str, str]) -> None:
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

class UnifiedMKVEngine:
    """
    Combines track scoring, dual-audio routing, surgical subtitle flag manipulation, 
    attachment purging, CRC hashing, and container reordering into a single pass.
    Includes the True Phantom Hybrid Reconstruct for catastrophically broken files.
    """
    def __init__(self, log_callback: Callable[[str], None], append_crc: bool, config: Dict[str, str]) -> None:
        self.mkvmerge_exe: Path = Path(config.get("mkvmerge_exe", ""))
        self.ffmpeg_exe: Path = Path(config.get("ffmpeg_exe", ""))
        self.log = log_callback
        self.append_crc = append_crc

    def verify_environment(self, require_ffmpeg: bool = False) -> bool:
        if not self.mkvmerge_exe or not self.mkvmerge_exe.exists():
            self.log("[CRITICAL ERROR] MKVToolNix path is missing or invalid.")
            self.log(" -> Please click '⚙️ Configure Armory' to set your executables.")
            return False
            
        if require_ffmpeg:
            if not self.ffmpeg_exe or not self.ffmpeg_exe.exists():
                self.log("[CRITICAL ERROR] FFmpeg path is missing or invalid.")
                self.log(" -> Please click '⚙️ Configure Armory' to set your executables.")
                return False
            try:
                subprocess.run([str(self.ffmpeg_exe), "-version"], capture_output=True, check=True)
            except Exception:
                self.log(f"[CRITICAL ERROR] FFmpeg failed to execute at {self.ffmpeg_exe}")
                return False
        return True

    def calculate_crc32(self, file_path: Path) -> str:
        crc = 0
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(65536), b''):
                crc = zlib.crc32(chunk, crc)
        return f"{crc & 0xFFFFFFFF:08X}"

    def parse_telemetry(self, file_path: Path) -> Dict[str, Any]:
        result = subprocess.run(
            [str(self.mkvmerge_exe), "-J", str(file_path)],
            capture_output=True, text=True, encoding='utf-8'
        )
        if result.returncode not in (0, 1):
            return {}
        return json.loads(result.stdout)

    def optimize_container(self, file_path: Path, debug_mode: bool) -> None:
        """The Standard ShadowForge Pipeline: Uses MKVToolNix to process the file."""
        data = self.parse_telemetry(file_path)
        if not data:
            self.log(f"    [ERROR] Failed to read JSON telemetry for {file_path.name}")
            return
            
        tracks: List[Dict[str, Any]] = data.get("tracks", [])
        
        video_tracks = [t for t in tracks if t.get("type") == "video"]
        audio_tracks = [t for t in tracks if t.get("type") == "audio"]
        sub_tracks = [t for t in tracks if t.get("type") == "subtitles"]

        if not audio_tracks:
            self.log("    [ERROR] No audio tracks found. Skipping file.")
            return

        best_audio_by_lang: Dict[str, Dict[str, Any]] = {}
        for track in audio_tracks:
            score = 0
            props = track.get("properties", {})
            track_name = props.get("track_name", "").lower()
            codec = track.get("codec", "").lower()
            lang = props.get("language", "").lower()
            
            is_jp = "jpn" in lang or "japanese" in track_name
            is_en = "eng" in lang or "english" in track_name
            lang_key = "jpn" if is_jp else ("eng" if is_en else "und")

            if "hifi" in track_name or "opus" in codec or "flac" in codec: score += 300
            elif "dolby" in track_name or "ac-3" in codec or "eac3" in codec: score += 200
            elif "aac" in track_name or "aac" in codec: score += 100
            score += (props.get("audio_channels", 2) * 10)

            assigned_name = ""
            if "hifi" in track_name: assigned_name = "HIFI 2.1"
            elif "dolby" in track_name: assigned_name = "Dolby 2.0"
            elif "aac lc" in track_name: assigned_name = "AAC LC 2.0"

            track["calculated_score"] = score
            track["assigned_name"] = assigned_name

            if lang_key not in best_audio_by_lang or score > best_audio_by_lang[lang_key]["calculated_score"]:
                best_audio_by_lang[lang_key] = track

        valid_audio_tracks = list(best_audio_by_lang.values())
        dropped_count = len(audio_tracks) - len(valid_audio_tracks)
        
        sub_default_id = None; sub_signs_id = None; sub_sdh_id = None
        for sub in sub_tracks:
            tid = sub["id"]
            props = sub.get("properties", {})
            name = props.get("track_name", "").lower()
            lang = props.get("language", "").lower()

            if "eng" in lang or "english" in name:
                if "sign" in name or "song" in name or "forced" in name:
                    if sub_signs_id is None: sub_signs_id = tid
                elif "sdh" in name:
                    if sub_sdh_id is None: sub_sdh_id = tid
                else:
                    if sub_default_id is None: sub_default_id = tid

        if sub_default_id is None and sub_sdh_id is not None: sub_default_id = sub_sdh_id

        temp_path = file_path.with_name(f"{file_path.stem}_TEMP{file_path.suffix}")
        cmd: List[str] = [str(self.mkvmerge_exe), "-o", str(temp_path)]
        track_order: List[str] = []

        valid_audio_ids = [str(t["id"]) for t in valid_audio_tracks]
        cmd.extend(["--audio-tracks", ",".join(valid_audio_ids)])

        for vid in video_tracks:
            tid = vid["id"]
            cmd.extend(["--track-name", f"{tid}:"])
            track_order.append(f"0:{tid}")

        has_jp = "jpn" in best_audio_by_lang
        has_en = "eng" in best_audio_by_lang

        for aud in valid_audio_tracks:
            tid = aud["id"]
            assigned = aud["assigned_name"]
            
            if assigned: cmd.extend(["--track-name", f"{tid}:{assigned}"])
            else: cmd.extend(["--track-name", f"{tid}:"])
                
            if has_jp and has_en:
                if "jpn" in aud.get("properties", {}).get("language", "").lower() or "japanese" in aud.get("properties", {}).get("track_name", "").lower():
                    cmd.extend(["--default-track", f"{tid}:yes"])
                else:
                    cmd.extend(["--default-track", f"{tid}:no"])
            else:
                if aud == valid_audio_tracks[0]:
                    cmd.extend(["--default-track", f"{tid}:yes"])
            
            track_order.append(f"0:{tid}")

        if has_jp and has_en: self.log(f"    [AUDIO LOGIC] Dual-Audio (JP/EN) configured. Dropped {dropped_count} inferior duplicates.")
        else: self.log(f"    [AUDIO LOGIC] Kept {len(valid_audio_tracks)} optimal track(s). Dropped {dropped_count} inferior duplicates.")

        for sub in sub_tracks:
            tid = sub["id"]
            props = sub.get("properties", {})
            name = props.get("track_name", "").lower()
            lang = props.get("language", "").lower()
            is_eng = "eng" in lang or "english" in name
            
            cmd.extend(["--default-track", f"{tid}:no", "--forced-track", f"{tid}:no"])

            if is_eng:
                if tid == sub_signs_id: cmd.extend(["--track-name", f"{tid}:English (Signs & Songs)"])
                elif tid == sub_sdh_id: cmd.extend(["--track-name", f"{tid}:English (SDH)"])
                else: cmd.extend(["--track-name", f"{tid}:English"])
            else:
                cmd.extend(["--track-name", f"{tid}:"])

            if tid == sub_default_id:
                cmd.extend(["--default-track", f"{tid}:yes"])
                self.log(f"    [SUB LOGIC] Standard English mapped to Default.")
            if tid == sub_signs_id:
                cmd.extend(["--forced-track", f"{tid}:yes"])
                self.log(f"    [SUB LOGIC] English Signs/Songs mapped to Forced.")
                
            track_order.append(f"0:{tid}")

        attachments = data.get("attachments", [])
        valid_att_ids = []
        for att in attachments:
            content_type = att.get("content_type", "").lower()
            if "image" not in content_type:
                valid_att_ids.append(str(att["id"]))

        if valid_att_ids: cmd.extend(["--attachments", ",".join(valid_att_ids)])
        else: cmd.append("--no-attachments")

        cmd.extend(["--track-order", ",".join(track_order), str(file_path)])

        self.log("    [PROCESS] Executing MKVMerge structural remux...")
        write_result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
        
        if write_result.returncode in (0, 1):
            if write_result.returncode == 1: self.log("    [PROCESS] Minor structural warnings bypassed successfully.")
                
            if self.append_crc:
                self.log("    [PROCESS] Calculating CRC32 hash (this may take a moment)...")
                crc_hash = self.calculate_crc32(temp_path)
                final_path = file_path.with_name(f"{file_path.stem}_({crc_hash}){file_path.suffix}")
            else:
                kage_dir = file_path.parent / "KageMuxed"
                kage_dir.mkdir(exist_ok=True)
                final_path = kage_dir / file_path.name
            
            if final_path.exists(): final_path.unlink()
            temp_path.rename(final_path)
            self.log(f"    [SUCCESS] Final Output Generated: {final_path.name}")
        else:
            self.log("    [ERROR] mkvmerge encountered a failure during remuxing.")
            if debug_mode:
                debug_info = write_result.stderr.strip() if write_result.stderr.strip() else write_result.stdout.strip()
                self.log(f"    [DEBUG] {debug_info}")
            if temp_path.exists(): temp_path.unlink()

    def optimize_phantom(self, file_path: Path, debug_mode: bool) -> None:
        """The Phantom Pipeline: Uses FFmpeg to rip and reconstruct ADTS headers natively."""
        data = self.parse_telemetry(file_path)
        if not data:
            self.log(f"    [ERROR] Failed to read JSON telemetry for {file_path.name}")
            return
            
        tracks: List[Dict[str, Any]] = data.get("tracks", [])
        video_tracks = [t for t in tracks if t.get("type") == "video"]
        audio_tracks = [t for t in tracks if t.get("type") == "audio"]
        sub_tracks = [t for t in tracks if t.get("type") == "subtitles"]

        if not audio_tracks:
            self.log("    [ERROR] No audio tracks found. Skipping file.")
            return

        best_audio_by_lang: Dict[str, Dict[str, Any]] = {}
        for track in audio_tracks:
            score = 0
            props = track.get("properties", {})
            track_name = props.get("track_name", "").lower()
            codec = track.get("codec", "").lower()
            lang = props.get("language", "").lower()
            
            is_jp = "jpn" in lang or "japanese" in track_name
            is_en = "eng" in lang or "english" in track_name
            lang_key = "jpn" if is_jp else ("eng" if is_en else "und")

            if "hifi" in track_name or "opus" in codec or "flac" in codec: score += 300
            elif "dolby" in track_name or "ac-3" in codec or "eac3" in codec: score += 200
            elif "aac" in track_name or "aac" in codec: score += 100
            score += (props.get("audio_channels", 2) * 10)

            assigned_name = ""
            if "hifi" in track_name: assigned_name = "HIFI 2.1"
            elif "dolby" in track_name: assigned_name = "Dolby 2.0"
            elif "aac lc" in track_name: assigned_name = "AAC LC 2.0"
            
            track["calculated_score"] = score
            track["assigned_name"] = assigned_name
            track["detected_lang"] = props.get("language", "und")

            if lang_key not in best_audio_by_lang or score > best_audio_by_lang[lang_key]["calculated_score"]:
                best_audio_by_lang[lang_key] = track

        valid_audio_tracks = list(best_audio_by_lang.values())
        dropped_count = len(audio_tracks) - len(valid_audio_tracks)
        has_jp = "jpn" in best_audio_by_lang
        has_en = "eng" in best_audio_by_lang

        sub_default_id = None; sub_signs_id = None; sub_sdh_id = None
        for sub in sub_tracks:
            tid = sub["id"]
            props = sub.get("properties", {})
            name = props.get("track_name", "").lower()
            lang = props.get("language", "").lower()

            if "eng" in lang or "english" in name:
                if "sign" in name or "song" in name or "forced" in name:
                    if sub_signs_id is None: sub_signs_id = tid
                elif "sdh" in name:
                    if sub_sdh_id is None: sub_sdh_id = tid
                else:
                    if sub_default_id is None: sub_default_id = tid

        if sub_default_id is None and sub_sdh_id is not None: sub_default_id = sub_sdh_id

        # --- STEP 1: CREATE WORKSPACE ---
        workspace = file_path.parent / f"{file_path.stem}_PHANTOM_RAW"
        workspace.mkdir(exist_ok=True)
        self.log(f"    [PHANTOM] Workspace created. Extracting naked streams via FFmpeg...")

        try:
            vid_path = workspace / "raw_video.mkv"
            subprocess.run([
                str(self.ffmpeg_exe), "-y", "-hide_banner", "-loglevel", "error", 
                "-i", str(file_path), "-map", f"0:{video_tracks[0]['id']}", 
                "-c:v", "copy", "-map_metadata", "-1", str(vid_path)
            ], capture_output=True, text=True, check=True)

            extracted_audios = []
            for idx, aud in enumerate(valid_audio_tracks):
                codec = aud.get("codec", "").lower()
                if "aac" in codec: ext = "aac"
                elif "ac3" in codec or "ac-3" in codec: ext = "ac3"
                elif "eac3" in codec: ext = "eac3"
                elif "opus" in codec: ext = "opus"
                elif "flac" in codec: ext = "flac"
                else: ext = "mka"
                
                a_path = workspace / f"raw_audio_{idx}.{ext}"
                subprocess.run([
                    str(self.ffmpeg_exe), "-y", "-hide_banner", "-loglevel", "error",
                    "-i", str(file_path), "-map", f"0:{aud['id']}", "-c:a", "copy", str(a_path)
                ], capture_output=True, text=True, check=True)
                extracted_audios.append({"path": a_path, "meta": aud})

            extracted_subs = []
            for sub in sub_tracks:
                tid = sub["id"]
                codec = sub.get("codec", "").lower()
                if "ass" in codec or "ssa" in codec or "substation" in codec: ext = "ass"
                elif "srt" in codec or "subrip" in codec: ext = "srt"
                else: ext = "mks"
                
                s_path = workspace / f"raw_sub_{tid}.{ext}"
                subprocess.run([
                    str(self.ffmpeg_exe), "-y", "-hide_banner", "-loglevel", "error",
                    "-i", str(file_path), "-map", f"0:{tid}", "-c:s", "copy", str(s_path)
                ], capture_output=True, text=True, check=True)
                extracted_subs.append({"path": s_path, "meta": sub, "tid": tid})

            self.log("    [PROCESS] Streams isolated. Rebuilding pristine container via MKVMerge...")
            temp_final = file_path.with_name(f"{file_path.stem}_TEMP{file_path.suffix}")
            
            cmd = [str(self.mkvmerge_exe), "-o", str(temp_final)]
            cmd.extend(["--track-name", "0:", str(vid_path)])
            
            if has_jp and has_en: self.log(f"    [AUDIO LOGIC] Dual-Audio (JP/EN) configured. Dropped {dropped_count} inferior duplicates.")
            else: self.log(f"    [AUDIO LOGIC] Kept {len(valid_audio_tracks)} optimal track(s). Dropped {dropped_count} inferior duplicates.")

            for ext_aud in extracted_audios:
                aud = ext_aud["meta"]
                a_path = ext_aud["path"]
                assigned = aud["assigned_name"]
                
                is_default = "no"
                if has_jp and has_en:
                    if "jpn" in aud.get("properties", {}).get("language", "").lower() or "japanese" in aud.get("properties", {}).get("track_name", "").lower():
                        is_default = "yes"
                else:
                    if ext_aud == extracted_audios[0]: is_default = "yes"

                name_flag = assigned if assigned else ""
                cmd.extend([
                    "--track-name", f"0:{name_flag}", 
                    "--language", f"0:{aud['detected_lang']}",
                    "--default-track", f"0:{is_default}", 
                    str(a_path)
                ])

            for ext_sub in extracted_subs:
                sub = ext_sub["meta"]
                s_path = ext_sub["path"]
                tid = ext_sub["tid"]
                
                props = sub.get("properties", {})
                name = props.get("track_name", "").lower()
                lang = props.get("language", "und").lower()
                is_eng = "eng" in lang or "english" in name
                
                is_default = "yes" if tid == sub_default_id else "no"
                is_forced = "yes" if tid == sub_signs_id else "no"
                
                if is_eng:
                    if tid == sub_signs_id: name_flag = "English (Signs & Songs)"
                    elif tid == sub_sdh_id: name_flag = "English (SDH)"
                    else: name_flag = "English"
                else:
                    name_flag = ""

                cmd.extend([
                    "--track-name", f"0:{name_flag}",
                    "--language", f"0:{lang}",
                    "--default-track", f"0:{is_default}",
                    "--forced-track", f"0:{is_forced}",
                    str(s_path)
                ])

                if is_default == "yes": self.log(f"    [SUB LOGIC] Standard English mapped to Default.")
                if is_forced == "yes": self.log(f"    [SUB LOGIC] English Signs/Songs mapped to Forced.")

            write_result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
            
            if write_result.returncode in (0, 1):
                if self.append_crc:
                    self.log("    [PROCESS] Calculating CRC32 hash (this may take a moment)...")
                    crc_hash = self.calculate_crc32(temp_final)
                    final_path = file_path.with_name(f"{file_path.stem}_({crc_hash}){file_path.suffix}")
                else:
                    kage_dir = file_path.parent / "KageMuxed"
                    kage_dir.mkdir(exist_ok=True)
                    final_path = kage_dir / file_path.name
                
                if final_path.exists(): final_path.unlink()
                temp_final.rename(final_path)
                self.log(f"    [SUCCESS] Final Output Generated: {final_path.name}")
            else:
                self.log("    [ERROR] MKVMerge encountered a failure during remuxing.")
                if debug_mode:
                    self.log(f"    [DEBUG] {write_result.stderr.strip()}")
                if temp_final.exists(): temp_final.unlink()
                
        except subprocess.CalledProcessError as e:
            self.log("    [CRITICAL ERROR] FFmpeg extraction failed.")
            if debug_mode:
                err_text = e.stderr.strip() if e.stderr else e.stdout.strip()
                self.log(f"    [DEBUG] {err_text}")
        finally:
            if workspace.exists():
                shutil.rmtree(workspace, ignore_errors=True)

    def execute_batch(self, target_dir_path: str, use_phantom: bool = False, debug_mode: bool = False) -> None:
        if not self.verify_environment(require_ffmpeg=use_phantom): return
            
        target_dir: Path = Path(target_dir_path)
        mkv_files: List[Path] = list(target_dir.rglob("*.mkv"))
        
        crc_pattern = re.compile(r"_\([A-Fa-f0-9]{8}\)$")
        source_files = []
        
        for f in mkv_files:
            if "KageMuxed" in f.parts: continue
            if crc_pattern.search(f.stem): continue
            if "_TEMP" in f.stem or "_PHANTOM_RAW" in f.stem: continue
            
            # Prevent picking up manual FFmpeg extraction artifacts
            if f.stem.endswith("_video") or f.stem.endswith("_audio") or f.stem.endswith("_subs"): continue
            
            source_files.append(f)
        
        if not source_files:
            self.log(f"\n[INFO] No valid source MKV files found in {target_dir}.")
            return
            
        for file_path in source_files:
            if use_phantom:
                self.log(f"\n[PHANTOM RECONSTRUCT] Engaging Engine on: {file_path.name}")
                self.optimize_phantom(file_path, debug_mode)
            else:
                self.log(f"\n[SCANNING] {file_path.name}")
                self.optimize_container(file_path, debug_mode)
            
        if use_phantom:
            self.log("\n[ATTENTION] Phantom Reconstruct complete!")
            self.log(" -> IMPORTANT: When encoding these phantom-reconstructed files in StaxRip:")
            self.log(" -> 1. You can leave the Source Filter set to 'Automatic'.")
            self.log(" -> 2. Open NVEncC Options (under the encoder dropdown).")
            self.log(" -> 3. Change the Input/Output Decoder from 'NVenc Hardware' to 'AviSynth/VapourSynth'.")
        else:
            self.log("\n[INFO] Batch processing complete!")


class OptimizerGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("KageMux: Advanced Container Optimizer v0.3")
        
        # Determine screen center and spawn window
        window_width = 850
        window_height = 650
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        
        self.bg_color = "#1E1E2E"       
        self.card_color = "#313244"     
        self.fg_color = "#CDD6F4"       
        self.accent_color = "#89B4FA"   
        self.accent_hover = "#B4BEFE"   
        self.secondary_color = "#45475A" 
        self.secondary_hover = "#585B70" 
        
        self.root.configure(bg=self.bg_color, padx=25, pady=25)
        
        style = ttk.Style(self.root)
        style.theme_use("clam") 
        
        style.configure("TFrame", background=self.bg_color)
        style.configure("TLabel", background=self.bg_color, foreground=self.fg_color, font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 11, "bold"), padding=(0, 0, 0, 8))
        
        style.configure("TCheckbutton", background=self.bg_color, foreground=self.fg_color, font=("Segoe UI", 10), focuscolor=self.bg_color)
        style.map("TCheckbutton", background=[("active", self.bg_color)])
        
        style.configure("TButton", background=self.card_color, foreground=self.fg_color, font=("Segoe UI", 10), borderwidth=0, padding=6)
        style.map("TButton", background=[("active", self.secondary_hover)])
        
        style.configure("Primary.TButton", background=self.accent_color, foreground="#11111B", font=("Segoe UI", 10, "bold"), borderwidth=0, padding=8)
        style.map("Primary.TButton", background=[("active", self.accent_hover)])
        
        style.configure("Secondary.TButton", background=self.secondary_color, foreground=self.fg_color, font=("Segoe UI", 10, "bold"), borderwidth=0, padding=8)
        style.map("Secondary.TButton", background=[("active", self.secondary_hover)])

        # Apply icon via the new resource path helper
        icon_path = get_resource_path("icon.ico")
        if icon_path.exists():
            try:
                self.root.iconbitmap(str(icon_path))
            except Exception: pass 
        
        self.config = load_config()
        self.target_directory = tk.StringVar()
        self.use_crc = tk.BooleanVar(value=True)
        self.use_debug = tk.BooleanVar(value=False)
        
        # --- UI LAYOUT ---
        top_bar = ttk.Frame(self.root)
        top_bar.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(top_bar, text="Target Directory:", style="Header.TLabel").pack(side=tk.LEFT)
        self.btn_armory = ttk.Button(top_bar, text="⚙️ Configure Armory", command=self.open_armory)
        self.btn_armory.pack(side=tk.RIGHT)
        
        path_frame = ttk.Frame(self.root)
        path_frame.pack(fill=tk.X, pady=(0, 8))
        
        self.path_entry = ttk.Entry(path_frame, textvariable=self.target_directory, state="readonly", font=("Segoe UI", 10))
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=4)
        
        self.btn_browse = ttk.Button(path_frame, text="📂 Browse", command=self.browse_folder)
        self.btn_browse.pack(side=tk.RIGHT)
        
        options_frame = ttk.Frame(self.root)
        options_frame.pack(fill=tk.X)
        
        self.chk_crc = ttk.Checkbutton(
            options_frame, 
            text="Calculate & Append CRC32 Hash to filename (Uncheck to output to 'KageMuxed' folder)", 
            variable=self.use_crc
        )
        self.chk_crc.pack(anchor=tk.W)

        self.chk_debug = ttk.Checkbutton(
            options_frame, 
            text="Enable Debug Logging (Show raw console errors for troubleshooting)", 
            variable=self.use_debug
        )
        self.chk_debug.pack(anchor=tk.W, pady=(4, 0))
        
        ttk.Label(self.root, text="Terminal Output:", style="Header.TLabel").pack(anchor=tk.W, pady=(15, 0))
        self.console_text = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, font=("Consolas", 9), 
            bg="#11111B", fg="#A6ADC8", borderwidth=0, highlightthickness=1, highlightbackground=self.card_color
        )
        self.console_text.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        self.console_text.config(state=tk.DISABLED)
        
        bottom_frame = ttk.Frame(self.root)
        bottom_frame.pack(fill=tk.X)
        
        self.btn_phantom = ttk.Button(bottom_frame, text="🛠️ Phantom Reconstruct", style="Secondary.TButton", command=lambda: self.start_processing(use_phantom=True))
        self.btn_phantom.pack(side=tk.LEFT, ipadx=5)

        self.btn_start = ttk.Button(bottom_frame, text="⚡ Engage ShadowForge", style="Primary.TButton", command=lambda: self.start_processing(use_phantom=False))
        self.btn_start.pack(side=tk.RIGHT, ipadx=10)
        
        self.log("Welcome to KageMux v0.3.")
        
        if not self.config.get("mkvmerge_exe") or not self.config.get("ffmpeg_exe"):
            self.log("[ATTENTION] Please click '⚙️ Configure Armory' to set up the tool before your first run.\n")
        else:
            self.log("Select a folder containing MKV files to begin.\n")

    def open_armory(self) -> None:
        """Opens a Toplevel window to configure MKVToolNix and FFmpeg paths."""
        armory_window = tk.Toplevel(self.root)
        armory_window.title("Armory Configuration")
        
        # Center the Armory Window
        window_width = 600
        window_height = 250
        screen_width = armory_window.winfo_screenwidth()
        screen_height = armory_window.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))
        armory_window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        
        # Apply the app icon to remove the default Tkinter feather
        icon_path = get_resource_path("icon.ico")
        if icon_path.exists():
            try:
                armory_window.iconbitmap(str(icon_path))
            except Exception: pass

        armory_window.configure(bg=self.bg_color, padx=20, pady=20)
        armory_window.grab_set() 

        ttk.Label(armory_window, text="MKVToolNix Path (mkvmerge.exe):", style="Header.TLabel").pack(anchor=tk.W)
        mkv_frame = ttk.Frame(armory_window)
        mkv_frame.pack(fill=tk.X, pady=(0, 15))
        
        mkv_var = tk.StringVar(value=self.config.get("mkvmerge_exe", ""))
        mkv_entry = ttk.Entry(mkv_frame, textvariable=mkv_var, font=("Segoe UI", 9))
        mkv_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=3)
        ttk.Button(mkv_frame, text="Locate", command=lambda: mkv_var.set(filedialog.askopenfilename(filetypes=[("Executable", "*.exe")]))).pack(side=tk.RIGHT)

        ttk.Label(armory_window, text="FFmpeg Path (ffmpeg.exe):", style="Header.TLabel").pack(anchor=tk.W)
        ff_frame = ttk.Frame(armory_window)
        ff_frame.pack(fill=tk.X, pady=(0, 20))
        
        ff_var = tk.StringVar(value=self.config.get("ffmpeg_exe", ""))
        ff_entry = ttk.Entry(ff_frame, textvariable=ff_var, font=("Segoe UI", 9))
        ff_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=3)
        ttk.Button(ff_frame, text="Locate", command=lambda: ff_var.set(filedialog.askopenfilename(filetypes=[("Executable", "*.exe")]))).pack(side=tk.RIGHT)

        def save_and_close():
            self.config["mkvmerge_exe"] = mkv_var.get()
            self.config["ffmpeg_exe"] = ff_var.get()
            save_config(self.config)
            self.log("[SYSTEM] Armory paths updated and saved.")
            armory_window.destroy()

        ttk.Button(armory_window, text="Save Configuration", style="Primary.TButton", command=save_and_close).pack(fill=tk.X)

    def log(self, message: str) -> None:
        self.console_text.config(state=tk.NORMAL)
        self.console_text.insert(tk.END, message + "\n")
        self.console_text.see(tk.END)
        self.console_text.config(state=tk.DISABLED)
        self.root.update_idletasks()

    def browse_folder(self) -> None:
        folder_selected = filedialog.askdirectory(title="Select MKV Directory")
        if folder_selected:
            self.target_directory.set(folder_selected)
            self.log(f"[DIRECTORY SELECTED] {folder_selected}")

    def start_processing(self, use_phantom: bool) -> None:
        dir_path = self.target_directory.get()
        if not dir_path:
            self.log("[WARNING] Please select a directory first.")
            return

        self.btn_browse.config(state=tk.DISABLED)
        self.btn_start.config(state=tk.DISABLED)
        self.btn_phantom.config(state=tk.DISABLED)
        self.btn_armory.config(state=tk.DISABLED)
        self.chk_crc.config(state=tk.DISABLED)
        self.chk_debug.config(state=tk.DISABLED)
        
        if use_phantom:
            self.log("\n[SYSTEM] Initializing Engine with PHANTOM RECONSTRUCT active...")
        else:
            self.log("\n[SYSTEM] Initializing standard SHADOWFORGE Engine...")

        thread = threading.Thread(target=self.run_engine, args=(dir_path, self.use_crc.get(), use_phantom, self.use_debug.get()), daemon=True)
        thread.start()

    def run_engine(self, dir_path: str, append_crc: bool, use_phantom: bool, debug_mode: bool) -> None:
        engine = UnifiedMKVEngine(log_callback=self.log, append_crc=append_crc, config=self.config)
        engine.execute_batch(dir_path, use_phantom=use_phantom, debug_mode=debug_mode)
        self.root.after(0, self.reset_ui)

    def reset_ui(self) -> None:
        self.btn_browse.config(state=tk.NORMAL)
        self.btn_start.config(state=tk.NORMAL)
        self.btn_phantom.config(state=tk.NORMAL)
        self.btn_armory.config(state=tk.NORMAL)
        self.chk_crc.config(state=tk.NORMAL)
        self.chk_debug.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = OptimizerGUI(root)
    root.mainloop()