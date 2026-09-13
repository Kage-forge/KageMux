# ⚡ KageMux: The Smart MKV Batch Optimizer & Renamer

[![Version](https://img.shields.io/badge/Version-v1.0.3-blue.svg)](#) 
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](#)

KageMux is a free, automated utility built for media archivists, anime fans, and video encoders. It acts as a smart bridge between your raw MKV files and your media server (like Plex or Jellyfin) or your encoding software (like StaxRip or HandBrake). 

By utilizing MKVToolNix and FFmpeg in the background, KageMux automatically cleans up your files, selects the best audio, removes junk tracks, and standardizes your file names. This completely eliminates the boring, repetitive manual work of setting up massive TV show or anime batches.

> **Repository Notice:** This repository is utilized exclusively for official KageMux binary releases, documentation, and issue tracking. The core application source code is proprietary and is not published here.

***

## 🚀 Key Features

* **Drag-and-Drop Interface:** Drop single files or entire batch folders directly into the app for instant processing.
* **Smart Audio Filtering:** Automatically scans your files and keeps the highest quality audio streams. It prioritizes lossless formats (FLAC/Opus) over standard surround sound (Dolby), and drops unnecessary lower-quality duplicates to save hard drive space.
* **Automatic Default Audio Routing:** Select your preferred language (Auto, English, Japanese, Chinese, or Korean) in the interface. KageMux scans the hidden metadata, finds your preferred language, and sets it as the default track. If your chosen language is missing, it safely falls back to standard Japanese routing.
* **Advanced Subtitle Cleanup:** KageMux cleans up messy ripper track names and converts them into standard language tags. It smartly preserves important source tags (like `[CR]` for Crunchyroll) while actively prioritizing SDH (Deaf and Hard of Hearing) subtitles for better accessibility. It also ensures "Signs and Songs" tracks never accidentally become your default subtitle.
* **Dual-Audio Support:** Perfectly configures the "Default" and "Forced" subtitle flags for standard Dual-Audio (Japanese and English) anime releases.
* **Automated Batch Renaming:** Forget heavy external tools like PowerRename. KageMux automatically extracts episode numbers (including decimal episodes like `05.5`, OVAs, and OP/EDs) from messy files. It then standardizes them into a clean, uniform format: `(Hi10)_Show_Title_-_01_(1080p)_(FansubGroup)_(CRC32).mkv`.
* **Emergency File Repair (Phantom Reconstruct):** A specialized fallback tool that safely extracts raw video, audio, and subtitle streams from catastrophically broken MKV files and rebuilds them into healthy containers. This is perfect for fixing "ADTS Header" errors or severe playback crashes.
* **VFR Sync (TimeWeaver):** A dedicated tool that perfectly restores Variable Frame Rate (VFR) lip-sync. It rips the original timecodes from your source files and seamlessly injects them into your newly encoded outputs without requiring complicated terminal commands.
* **Modern GUI & Live Progress:** Built on a fast, modern PyQt6 framework with beautiful dark themes (ShadowForge Dark and Obsidian Ronin). It features live terminal logs, exact batch progress tracking, and a diagnostic mode for easy troubleshooting.

***

## 🧩 Required Dependencies

KageMux is designed as a graphical "brain" that commands industry-standard media tools. To function, you must have the following free tools installed on your Windows system.

### 1. MKVToolNix (Required)
* **Purpose:** Powers the core optimization engine and the TimeWeaver sync tool. KageMux uses `mkvmerge.exe` to strip out junk attachments and `mkvextract.exe` to rip variable timecodes.
* **Download:** [MKVToolNix Official Site](https://mkvtoolnix.download/)

### 2. FFmpeg (Required for Phantom Reconstruct)
* **Purpose:** Powers the emergency repair pipeline. KageMux uses `ffmpeg.exe` to forcefully extract naked streams from broken containers before rebuilding them.
* **Download:** [FFmpeg Official Windows Builds](https://gyan.dev/ffmpeg/builds/) (We recommend the `ffmpeg-git-full.7z` release).

***

## 🛠️ Installation & Setup

1. Navigate to the **Releases** tab on the right side of this GitHub page.
2. Download the latest `KageMux.exe` file. (No installation is required; the application is completely portable).
3. Place `KageMux.exe` in a dedicated folder on your computer and double-click to launch.

*(Note: Because this is a compiled Python executable, Windows SmartScreen or Windows Defender may display a "Windows protected your PC" warning. This is a standard false positive for new standalone binaries. Simply click "More info" and "Run anyway".)*

***

## ⚙️ Configuring The Armory (First Time Setup)

To protect your system from errors, KageMux locks all primary action buttons upon its first launch. 

1. Launch KageMux. The app will attempt to automatically detect MKVToolNix and FFmpeg on your system. If successful, the engine will unlock immediately.
2. If auto-detection fails, click the **⚙️ Configure Armory** button at the top right of the UI.
3. Click **Locate** and manually navigate to your `mkvmerge.exe`, `mkvextract.exe`, and `ffmpeg.exe` files. Be sure to select the `.exe` files, not the folders.
4. Click **Save Configuration**. The UI will verify the paths, unlock the main buttons, and save your settings permanently.

***

## 🧠 How Track Scoring Works

When KageMux processes a media file with multiple audio tracks of the same language, it assigns a mathematical score to each track based on its quality. It keeps the winner and discards the rest. 

**The Hierarchy:**
1. **Lossless / High-Res (300 points):** FLAC, TrueHD, DTS-HD MA, Opus.
2. **High-Quality Surround (200 points):** AC-3, E-AC-3, Standard Dolby Digital.
3. **Standard Audio (100 points):** AAC, AAC-LC.
4. **Channel Multiplier (+10 points per channel):** A 5.1 surround track will automatically beat a 2.0 stereo track of the exact same format.
5. **Duration Tie-Breaker:** If two duplicate audio tracks tie in points, the engine automatically keeps the longest, most complete stream while deleting the fragmented file.

***

## ☕ Support the Project

KageMux is completely free and actively maintained. If this tool has saved you hours of manual renaming, automated your track selections, or rescued a broken batch of files, consider supporting the development.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/kageforge)

***

## 📜 License & Usage

KageMux is proprietary freeware. You are free to download, use, and share the compiled Windows executable for personal or commercial media encoding workflows. 

However, the core Python engine remains closed-source. Reverse engineering, decompiling, or repackaging the binary for unauthorized commercial distribution is strictly prohibited.

***

## 📜 The Project Archives

Curious about how KageMux evolved from a basic command-line wrapper into an advanced batch automation workspace? Review the complete development history and feature updates in the [Project Milestones](https://github.com/Kage-forge/KageMux/blob/main/archives.md).
