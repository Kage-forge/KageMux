# ⚡ KageMux: The Advanced Container Optimizer

[![Version](https://img.shields.io/badge/Version-v0.8.0-blue.svg)](#) 
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](#)

KageMux is a proprietary freeware utility designed for media archivists and encoders. It acts as an intelligent, automated bridge between your raw MKV files and your encoding software (like StaxRip or HandBrake). 

By leveraging the raw power of MKVToolNix and FFmpeg in the background, KageMux surgically cleans, scores, and restructures your media containers before you encode them. This completely eliminates the tedious manual track selection process for massive television batches.

> **Repository Notice:** This repository is utilized exclusively for official KageMux binary releases, documentation, and issue tracking. The core application source code is proprietary and is not published here.

---

## 🚀 Core Arsenal

* **Kinetic Targeting:** Drop single files or entire batch folders directly into the GUI for instantaneous pathing and execution.
* **The ShadowForge Engine:** Automatically scans and scores audio tracks, keeping the highest quality streams (Prioritizing FLAC/Opus > Dolby > AAC) while dropping inferior duplicates. 
* **Omni-Linguist Subtitle Parser:** Dynamically detects, preserves, and tags international subtitles (e.g., Japanese, Arabic, Spanish). The engine intelligently hunts for bracketed tags like `(Korean Names)` or `[Dubtitle]`, and actively preserves critical VOD source acronyms like `[CR]` and `[AMZN]` to create perfectly clean, serialized English metadata.
* **Dual-Audio Routing:** Flawlessly configures Default and Forced flags for standard Dual-Audio (JP/EN) anime releases based on audio presence.
* **The Phantom Reconstruct:** A specialized fallback pipeline that completely disassembles broken MKV files into raw streams via FFmpeg and reconstructs them into pristine containers. This is crucial for fixing "ADTS Header" errors or severe desync issues in catastrophic rips.
* **Live Telemetry:** Features a sleek, Material-inspired GUI with live terminal outputs, dynamic hardware-accelerated spinners, native Windows taskbar branding, and precise batch progress tracking. The engine concludes every batch run with a highly detailed, lore-accurate summary (**THE SHADOWFORGED REPORT** or **THE PHANTOM-RECONSTRUCTED REPORT**) detailing exact track retention data.

---

## 🧩 The Dependency Matrix

KageMux is designed as a graphical "brain" that commands industry-standard CLI tools. To function, it requires two external dependencies installed on your system.

### 1. MKVToolNix (Required)
* **Purpose:** Powers the core ShadowForge engine. KageMux uses `mkvmerge.exe` to read the JSON telemetry of your files, strip out junk attachments, and execute the final, clean multiplexing phase.
* **Download:** [MKVToolNix Official Site](https://mkvtoolnix.download/)

### 2. FFmpeg (Required for Phantom Reconstruct)
* **Purpose:** Powers the Phantom pipeline. KageMux uses `ffmpeg.exe` to brutally extract naked audio, video, and subtitle streams from catastrophically broken containers before pushing them back to MKVMerge for rebuilding.
* **Download:** [FFmpeg Official Windows Builds](https://gyan.dev/ffmpeg/builds/) (We recommend the `ffmpeg-git-full.7z` release).

---

## 🛠️ Installation & Deployment

1. Navigate to the **Releases** tab on the right side of this GitHub page.
2. Download the latest `KageMux.exe` file. (No installation required; it is completely portable).
3. Place `KageMux.exe` in a dedicated folder on your computer and double-click to launch.

*(Note: Because this is a compiled Python executable, Windows SmartScreen or Windows Defender may display a "Windows protected your PC" warning. This is a standard false positive for new standalone binaries. Simply click "More info" and "Run anyway".)*

---

## ⚙️ Configuring The Armory (First Time Setup)

To protect your system from executing blank paths, KageMux locks all primary action buttons upon first launch. 

1. Launch KageMux. The application will attempt to auto-detect MKVToolNix and FFmpeg in your standard system directories or PATH variables. If successful, the engine will unlock automatically.
2. If auto-detection fails, click the **⚙️ Configure Armory** button at the top right of the UI.
3. Click **Locate** and navigate to your `mkvmerge.exe` and `ffmpeg.exe` binaries explicitly. Ensure you select the `.exe` files, not the folders.
4. Click **Save Configuration**. The UI will verify the paths, unlock the action buttons, and save your settings permanently to a local `.json` configuration file.

---

## 🧠 Understanding the Track Scoring Logic

When KageMux evaluates a media file with multiple audio tracks of the same language, it assigns a mathematical score to each track based on its codec and properties. It then discards the losers. 

**The Hierarchy:**
1. **Uncompressed / Lossless (300 points):** FLAC, TrueHD, DTS-HD MA, Opus.
2. **High-Quality Surround (200 points):** AC-3, E-AC-3, Standard Dolby Digital.
3. **Standard Audio (100 points):** AAC, AAC-LC.
4. **Channel Multiplier (+10 points per channel):** A 5.1 surround track will automatically beat a 2.0 stereo track of the same codec.
5. **Duration Tie-Breaker:** If two duplicate audio tracks tie in points, the engine reads the `duration_ns` telemetry or embedded string tags (e.g., `tag_duration`, `tag_number_of_frames`) to retain the longest, most complete stream while purging the fragmented file.

---

## ☕ Support the Forge

KageMux is completely free and actively maintained. If this tool has saved you hours of manual track selection or rescued a broken batch of files, consider supporting the development.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/kageforge)

---

## 📜 License & Usage

KageMux is proprietary freeware. You are free to download, use, and share the compiled Windows executable for personal or commercial media encoding workflows. 

However, the core Python engine remains closed-source. Reverse engineering, decompiling, or repackaging the binary for unauthorized commercial distribution is strictly prohibited.

---

## 📜 The ShadowForge Archives

Curious about how KageMux evolved from a basic CLI wrapper into a kinetic batch automation workspace? Review the complete development history, feature deployments, and architectural upgrades in the [Project Milestones](ARCHIVES.md).
