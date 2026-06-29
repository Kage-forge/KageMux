# KageMux: The Advanced Container Optimizer ⚡

![Version](https://img.shields.io/badge/version-0.3-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg) ![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

**KageMux** is an industrial-grade, automated MKV grooming tool forged for media encoders, anime archivists, and data hoarders. It operates in the shadows to surgically repair, score, and optimize video containers before they ever touch your encoding pipeline.

### The Problem it Solves
The modern internet is filled with inconsistently muxed and corrupted MKV files. Many contain bloated audio tracks, messy subtitle flags, and broken metadata that cause media servers and encoding tools (like StaxRip or Handbrake) to crash instantly. KageMux acts as the ultimate filter. 

**ShadowForge** automatically cleanses, scores, and structures healthy files to ensure playback perfection. **Phantom Reconstruct** forcefully resurrects deeply corrupted files that standard multiplexers reject.

---

## ⚔️ The Arsenal (Features)

### 1. ShadowForge (Standard Pipeline)
For 99% of your library, KageMux utilizes MKVToolNix to perform a lossless, blazing-fast structural sweep:
* **Smart Audio Grouping:** Detects, scores, and isolates the highest-quality audio tracks while actively purging inferior duplicates.
* **Dual-Audio Routing:** Automatically sets Japanese audio to Default if both English and Japanese tracks survive the purge.
* **Surgical Subtitles:** Scrubs messy ripper defaults, dynamically detects Signs & Songs vs. standard SDH dialogue, and natively applies the correct `Default` and `Forced` Matroska flags.
* **Metadata Purging:** Strips embedded cover art and junk flags while safely copying all attached fonts.

### 2. Phantom Reconstruct (Hybrid Engine)
For the 1% of files that are so mangled that standard tools crash, KageMux deploys the Phantom Reconstruct protocol:
* It violently tears the broken container apart using FFmpeg.
* It mathematically reconstructs missing AAC and ADTS audio headers from scratch.
* It feeds the newly sanitized raw streams back into MKVToolNix, weaving them into a pristine, mathematically perfect Matroska container ready for modern encoding.

### 3. Automated CRC32 Hashing
Automatically calculates and appends the standard anime 8-character CRC32 hash to your final filenames `_(XXXXXXXX).mkv`.

---

## 🔗 Prerequisites (The Dependencies)
While KageMux itself is a standalone portable executable, it acts as a central brain that commands two distinct open-source engines. **You must have both of these installed on your Windows machine to use KageMux.**

### MKVToolNix (The Container Engine)
* **What it does:** Losslessly parses, builds, and edits Matroska (`.mkv`) files.
* **Where to get it:** Download the Windows installer from the [Official MKVToolNix Site](https://mkvtoolnix.download/downloads.html#windows).

### FFmpeg (The Phantom Extraction Engine)
* **What it does:** Handles raw stream extraction and audio header reconstruction.
* **Where to get it:** Download the latest Windows essential build from [Gyan.dev](https://www.gyan.dev/ffmpeg/builds/) or the [Official FFmpeg Site](https://ffmpeg.org/download.html#build-windows). Extract the `.zip` and locate `ffmpeg.exe` inside the `bin` folder. (Note: If you use StaxRip, you already have FFmpeg installed in your StaxRip Apps folder!)

---

## 🛠️ Installation & Setup
1. Navigate to the **Releases** tab on the right side of this GitHub page.
2. Download the latest `KageMux.exe` file. (No installation required; it is completely portable).
3. Place `KageMux.exe` in any folder on your computer and double-click to launch.

### Configuring The Armory (First Time Setup)
Upon launching KageMux for the first time, you must link it to your dependencies.
1. Click the **⚙️ Configure Armory** button at the top of the KageMux UI.
2. Click **Locate** and navigate to where you installed MKVToolNix (select `mkvmerge.exe`).
3. Click **Locate** and navigate to your FFmpeg bin folder (select `ffmpeg.exe`).
4. Click **Save Configuration**. You never have to do this again.

---

## 🚀 How to Use
1. Click **Browse** and select a folder containing your messy MKV files.
2. Check or uncheck the **CRC32** box depending on your naming preferences.
3. Choose your operation:
   * **⚡ Engage ShadowForge:** Click this for standard files to perfectly prep them for your media server or encoder.
   * **🛠️ Phantom Reconstruct:** Click this ONLY if your files are deeply corrupted and failing to encode in other software.

---

## 🐛 Feedback & Bug Reports
Found a bug, have a feature request, or need help with a specific file? Please navigate to the **Issues** tab at the top of this GitHub page and open a new ticket. Include as much detail as possible (and check the "Enable Debug Logging" box in KageMux to provide error logs).

---

## ☕ Support the Forge
KageMux is completely free and open-source. If this tool has saved your encoding queue (and your sanity), consider supporting the development!
* [Support via Ko-fi](https://ko-fi.com/kageforge)

---

## 📜 License
This project is open-source and licensed under the MIT License. Feel free to fork, modify, and enhance the KageMux arsenal.
