KageMux v0.3: The Advanced Container Optimizer ⚡

KageMux is an industrial-grade, automated MKV grooming tool forged for media encoders, anime archivists, and data hoarders. It operates in the shadows to surgically repair, score, and optimize video containers before they ever touch your encoding pipeline.

The Problem it Solves
The modern internet (especially platforms like Telegram) is littered with catastrophically corrupted MKV rips. These files suffer from shattered internal indices, stripped ADTS audio headers, and junk metadata. When you feed these "dead" files into standard GUI encoders (like StaxRip or Handbrake), the demuxers panic and crash, halting your batch encodes instantly.

KageMux is the cure. It brings un-muxable files back from the grave.

⚔️ The Arsenal (Features)
1. ShadowForge (Standard Pipeline)
For 99% of your library, KageMux utilizes MKVToolNix to perform a lossless, blazing-fast structural sweep:

Smart Audio Grouping: Detects, scores, and isolates the highest-quality audio tracks (HIFI > Dolby > AAC) while actively purging inferior duplicates.

Dual-Audio Routing: Automatically sets Japanese audio to Default if both English and Japanese tracks survive the purge.

Surgical Subtitles: Scrubs messy ripper defaults, dynamically detects Signs & Songs vs. standard SDH dialogue, and natively applies the correct Default and Forced Matroska flags.

Metadata Purging: Strips embedded cover art and junk flags while safely copying all attached fonts.

2. Phantom Reconstruct (Hybrid Engine)
For the 1% of files that are so mangled that standard tools crash, KageMux deploys the Phantom Reconstruct protocol.

It violently tears the broken container apart using FFmpeg.

It mathematically reconstructs missing AAC/ADTS audio headers from scratch.

It feeds the newly sanitized raw streams back into MKVToolNix, weaving them into a pristine, mathematically perfect Matroska container ready for modern encoding.

3. Automated CRC32 Hashing
Automatically calculates and appends the standard anime 8-character CRC32 hash to your final filenames _(XXXXXXXX).mkv.

🔗 Prerequisites (The Dependencies)
While KageMux itself is a standalone portable executable, it acts as a central brain that commands two distinct open-source engines. You must have both of these installed on your Windows machine to use KageMux.

MKVToolNix (The Container Engine)

What it does: Losslessly parses, builds, and edits Matroska (.mkv) files.

Where to get it: Download the Windows installer from the Official MKVToolNix Site.

FFmpeg (The Phantom Extraction Engine)

What it does: Handles raw stream extraction and audio header reconstruction.

Where to get it: Download the latest Windows essential build from Gyan.dev or the Official FFmpeg Site. Extract the .zip and locate ffmpeg.exe inside the bin folder. (Note: If you use StaxRip, you already have FFmpeg installed in your StaxRip Apps folder!)

🛠️ Installation & Setup
Navigate to the Releases tab on the right side of this GitHub page.

Download the latest KageMux.exe file. (No installation required, it is completely portable).

Place KageMux.exe in any folder on your computer and double-click to launch.

Configuring The Armory (First Time Setup)
Upon launching KageMux for the first time, you must link it to your dependencies.

Click the ⚙️ Configure Armory button at the top of the KageMux UI.

Click "Locate" and navigate to where you installed MKVToolNix (select mkvmerge.exe).

Click "Locate" and navigate to your FFmpeg bin folder (select ffmpeg.exe).

Click Save Configuration. You never have to do this again.

🚀 How to Use
Click Browse and select a folder containing your messy MKV files.

Check or uncheck the CRC32 box depending on your naming preferences.

Choose your operation:

⚡ Engage ShadowForge: Click this for standard files to perfectly prep them for your media server or encoder.

🛠️ Phantom Reconstruct: Click this ONLY if your files are deeply corrupted and failing to encode in other software.


📜 License
This project is open-source and licensed under the MIT License. Feel free to fork, modify, and enhance the KageMux arsenal.
