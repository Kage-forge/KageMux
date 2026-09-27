# ⚡ KageMux: The Advanced Matroska Optimization Workspace

[![Version](https://img.shields.io/badge/Version-v1.2.0-blue.svg)](#) 
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](#)

KageMux operates as an autonomous, zero-cost media optimization workspace engineered specifically for video encoders and media archivists. 

The application serves as an intelligent processing bridge, perfectly aligning raw MKV containers for immediate deployment to media servers (Plex, Jellyfin) or encoding pipelines (HandBrake, StaxRip). Powered by native integrations with FFmpeg and MKVToolNix, the engine autonomously sanitizes metadata, isolates optimal audio streams, purges redundant payload data, and unifies file nomenclature. This architecture entirely eradicates the repetitive manual overhead required to configure massive episodic media batches.

> **Repository Notice:** This repository is utilized exclusively for official KageMux binary releases, documentation, and issue tracking. The core application source code is proprietary and is not published here.

***

## 🚀 Key Features

* **🌌 The Nexus Assembler Module:** A universal multi-track multiplexing hub. The engine executes an agnostic recursive scan to locate base video files and seamlessly absorb identically named external audio streams, subtitle payloads, and master font directories. It employs dynamic language inference to automatically map proper ISO 639-2 tags to external assets based on folder nomenclature.
* **🛡️ Omni-Linguist Subtitle Matrix:** Mathematically evaluates all duplicate SDH and Signs & Songs tracks. The engine routes all isolated subsets through a rigorous 1,000-point codec hierarchy to ensure premium formats (`.ass`, `.srt`) permanently override weaker retail streams (`.pgs`).
* **🏷️ Shroud Designation Engine:** An autonomous batch renaming matrix. Safely steps over fused season integers (S01, S2) to securely isolate embedded metadata (OP, ED, OVA) without fracturing episode sequences. Outputs perfectly standardized formats: `(Hi10)_Title_-_EP_(Res)_(Group)_(CRC).mkv`. The engine strictly prohibits illegal cloud-routing characters (`< > : " / \ | ? * , & + [ ]`).
* **🔄 The Karasu Protocol (Autonomous Updates):** Driven by a headless background executable, the workspace securely queries the GitHub API to execute zero-friction binary swaps. To permanently eliminate Windows Shell drift, the courier dynamically consumes versioned binaries and exclusively outputs the updated engine as `KageMux.exe`.
* **🖥️ Native OS Integration:** Embed the optimizer directly into your Windows shell environment. Activating the system integration parameter within the Armory writes a localized registry key, allowing you to right-click any local directory and instantly queue the target path into the engine.
* **🔊 Intelligent Audio Routing:** Scans container telemetry to isolate and retain the highest-fidelity streams. Prioritizes lossless formats (FLAC, Opus) over standard Dolby arrays, routing the default flag to your preferred global language with automated fallback protocols.
* **👁️ ShadowSight Intercept:** An interactive pre-flight UI that pauses background processing, allowing operators to manually designate specific subtitle translations across entire batches.
* **🛠️ Phantom Reconstruct:** A fail-safe FFmpeg extraction pipeline designed to forcefully rip naked streams from corrupted MKV containers and assemble them into healthy, structurally sound files.
* **⏱️ TimeWeaver:** A dedicated VFR synchronization utility that extracts native timecodes from original media and seamlessly weaves them into newly encoded video outputs.

***

## 🧩 Required Dependencies

KageMux is designed as a graphical command matrix that relies on industry-standard processing tools. You must have the following free utilities installed on your Windows host.

### 1. MKVToolNix (Required)
* **Purpose:** Powers the core optimization engine, the Nexus Assembler, and the TimeWeaver sync tool. KageMux uses `mkvmerge.exe` to manipulate container architecture and `mkvextract.exe` to isolate native variable timecodes.
* **Download:** [MKVToolNix Official Site](https://mkvtoolnix.download/)

### 2. FFmpeg (Required for Phantom Reconstruct)
* **Purpose:** Powers the emergency repair pipeline. KageMux uses `ffmpeg.exe` to forcefully separate and isolate streams from heavily fragmented media containers.
* **Download:** [FFmpeg Official Windows Builds](https://gyan.dev/ffmpeg/builds/) (We recommend the `ffmpeg-git-full.7z` release).

***

## 🛠️ Installation & Setup

1. Navigate to the **Releases** tab on the right side of this GitHub page.
2. Download the latest release `.zip` containing both `KageMux.exe` and `karasu.exe`.
3. Extract and place both executables together in a dedicated directory on your local drive. **Do not separate these files.** The Karasu courier requires close proximity to execute automated background updates.
4. Launch `KageMux.exe` to initiate the workspace.

*(Note: Because this is a newly compiled standalone binary, Windows SmartScreen may present a standard security warning. Click "More info" and "Run anyway" to proceed.)*

***

## ⚙️ Configuring The Armory (First Time Setup)

To protect your system from executing broken command lines, KageMux locks all primary action buttons upon initialization.

1. Launch KageMux. The application will attempt an autonomous scan to detect MKVToolNix and FFmpeg directories on your local drive. If successful, the engine will unlock immediately.
2. If the autonomous scan fails, click the **⚙️ Configure Armory** button.
3. Select **Locate** to manually map the exact file paths for your `mkvmerge.exe`, `mkvextract.exe`, and `ffmpeg.exe` binaries. 
4. Click **Save Configuration**. The UI will verify the targeted binaries, permanently lock the configuration, and arm the main interface.

***

## 🧠 The Audio Scoring Hierarchy

When KageMux intercepts a media file containing multiple audio tracks of the same language, it deploys a mathematical algorithm to grade each stream. The matrix retains the highest-scoring asset and actively purges the inferior duplicates.

**The Matrix:**
1. **Lossless / High-Res (300 points):** FLAC, TrueHD, DTS-HD MA, Opus.
2. **High-Quality Surround (200 points):** AC-3, E-AC-3, Standard Dolby Digital.
3. **Standard Audio (100 points):** AAC, AAC-LC.
4. **Channel Multiplier (+10 points per channel):** A 5.1 surround configuration will mathematically overrule a 2.0 stereo track utilizing the exact same base codec.
5. **Duration Tie-Breaker:** In the event of an exact mathematical tie, the engine prioritizes the track with the longest running duration to guarantee completion.

***

## ☕ Support the Forge

KageMux is completely free and actively maintained. If this workspace has successfully automated your media deployment, corrected a broken archive, or eliminated tedious manual data entry, consider supporting the continuous development pipeline.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/kageforge)

***

## 📜 License & Usage

KageMux is proprietary freeware. You are permitted to download, operate, and share the compiled Windows executables for both personal and professional media encoding operations. 

The core Python architecture remains closed-source. Reverse engineering, decompiling, or repackaging the binary for unauthorized commercial distribution is strictly prohibited.
