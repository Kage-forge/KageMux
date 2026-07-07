# ⚡ KageMux: The Advanced Container Optimizer

[![Version](https://img.shields.io/badge/Version-v0.6.2-blue.svg)](#) 
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)](#)

KageMux is a proprietary freeware utility designed for media archivists and encoders. It acts as an intelligent, automated bridge between your raw MKV files and your encoding software (like StaxRip or HandBrake). 

By leveraging MKVToolNix and FFmpeg in the background, KageMux surgically cleans, scores, and restructures your media containers before you encode them, saving you from tedious manual track selection.

> **Repository Notice:** This repository is utilized exclusively for official KageMux binary releases, documentation, and issue tracking. The core application source code is proprietary and is not published here.

---

## 🚀 Core Arsenal

* **The ShadowForge Engine:** Automatically scans and scores audio tracks, keeping the highest quality streams (Prioritizing FLAC/Opus > Dolby > AAC) while dropping inferior duplicates.
* **Omni-Linguist Subtitle Parser:** Dynamically detects, preserves, and tags international subtitles (e.g., Japanese, Arabic, Spanish) while automatically identifying and flagging English "Dubtitles," "SDH," and "Signs & Songs."
* **Dual-Audio Routing:** Flawlessly configures Default and Forced flags for standard Dual-Audio (JP/EN) anime releases.
* **The Phantom Reconstruct:** A specialized fallback pipeline that completely disassembles broken MKV files into raw streams via FFmpeg and reconstructs them into pristine containers. Crucial for fixing "ADTS Header" errors or desync issues in catastrophic rips.
* **Live Telemetry:** Features a sleek, Material-inspired GUI with live terminal outputs, dynamic hardware-accelerated spinners, and precise batch progress tracking.

---

## 🛠️ Installation & Setup

### For Windows Users
1. Navigate to the **Releases** tab on the right side of this GitHub page.
2. Download the latest `KageMux.exe` file. (No installation required; it is completely portable).
3. Place `KageMux.exe` in any folder on your computer and double-click to launch.

*(Note: Because this is a newly compiled tool, Windows SmartScreen or Windows Defender may display a "Windows protected your PC" warning. This is a standard false positive for new PyInstaller executables. Simply click "More info" and "Run anyway".)*

### For Linux Users
KageMux natively supports POSIX environments via a standalone ELF binary.
1. Download the `KageMux-Linux-x86_64` file from the **Releases** tab.
2. Open your terminal and install the required dependencies (FFmpeg, MKVToolNix, and Tkinter):
   * **Debian/Ubuntu:** `sudo apt update && sudo apt install mkvtoolnix ffmpeg python3-tk`
   * **Arch:** `sudo pacman -Syu mkvtoolnix-cli ffmpeg tk`
3. Make the binary executable: `chmod +x KageMux-Linux-x86_64`
4. Run the application: `./KageMux-Linux-x86_64`

---

## ⚙️ Configuring The Armory (First Time Setup)

Upon launching KageMux for the first time, the primary action buttons will be locked. You must link KageMux to your underlying tools.

1. Click the **⚙️ Configure Armory** button at the top right of the KageMux UI.
2. Click **Locate** and navigate to your `mkvmerge.exe` file (usually in `C:\Program Files\MKVToolNix\`). Ensure you select the `.exe` file, not just the folder.
3. Click **Locate** and navigate to your `ffmpeg.exe` file.
4. Click **Save Configuration**. The UI will unlock, and you never have to do this again.

---

## 📜 License & Usage
KageMux is proprietary freeware. You are free to download, use, and share the compiled executables for personal or commercial media encoding workflows. 

However, the core Python engine remains closed-source. Reverse engineering, decompiling, or repackaging the binary for unauthorized commercial distribution is strictly prohibited.
