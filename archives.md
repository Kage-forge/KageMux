# ⚡ The ShadowForge Archives: Project Milestones

This document records the architectural progression of KageMux. From its beginning as a basic command-line script to a fully autonomous kinetic media workspace, each logged milestone represents a calculated enhancement in pipeline automation and container optimization.

***

### KageMux v1.2.0 (The Nexus Assembler Update)
This major architectural deployment transitions the application from a strict subtractive container optimizer into a universal media assembly workspace.
* **The Nexus Assembler Module:** Integrated a universal multi-track multiplexing engine directly into the graphical interface. The system executes an agnostic recursive scan to locate base video files and seamlessly absorbs identically named external audio streams, subtitle scripts, and global fonts into a unified master container.
* **Dynamic Language Inference:** Engineered an automated parsing routine within the Nexus loop. The engine actively reads folder nomenclature to assign the correct ISO 639-2 language tags to external assets during the injection process.
* **Omni-Linguist Matrix Refinement:** Restructured the subtitle parsing matrix to mathematically score all duplicate SDH and Signs & Songs tracks. The engine now routes all isolated subsets through the full codec hierarchy, ensuring that superior formats like `.ass` or `.srt` permanently capture the forced designation over weaker retail streams like `.pgs`.
* **Fused Tag Extraction:** Enhanced the Shroud Designation Engine to seamlessly bypass fused season integers (such as S01 or S2). This allows the system to accurately isolate embedded media tags (including OP, ED, OVA, and SP) without breaking the alphanumeric episode sequence or triggering zero-state fallbacks.

### KageMux v1.1.9 (Matrix Decoupling & Interface Polish)
This structural revision optimized the graphical interface for a logical top-to-bottom workflow and purged native Windows rendering artifacts.
* **ShadowSight Intercept Integration:** Officially renamed the interactive pre-flight window and moved it higher in the visual hierarchy to ensure a proper sequential setup.
* **Decoupled Output Routing:** Detached the CRC32 hashing mechanism from the directory pathing logic. Operators can now append hashes independently and skip the `KageMuxed` directory to output files right next to the source files.
* **State Machine Locking:** Built an autonomous lock that visually disables the standalone CRC checkbox the moment the Shroud Engine is armed, stopping conflicting hashing loops.
* **Interface Rendering Polish:** Applied strict QSS transparency rules to the `QScrollArea` to override default operating system graphics, injecting a modern rounded scrollbar. Additionally, removed redundant text from progress labels to let native PyQt6 bars handle numerical tracking.

### KageMux v1.1.8 (The ShadowSight Intercept Protocol)
This update deployed a manual override function to bypass automated mathematical track evaluations.
* **Interactive Pre-Flight Scan:** Integrated a thread-safe intercept that pauses the background processor before multiplexing initiates. The engine parses the first MKV file and generates a graphical modal displaying all available subtitle streams.
* **Mathematical Obliteration:** Modified the subtitle matrix to accept manual commands. The system now assigns a 500,000-point override to the user's targeted track, safely ignoring standard tie-breaker algorithms (like ASS versus SRT comparisons).
* **Nameless Track Synchronization:** Built a metadata fallback that applies "Unknown Track" to empty subtitle streams in both the UI and the core engine, ensuring forced selections never fail from string matching errors.

### KageMux v1.1.7 (The Recursive Blindness Patch)
This logic update hardened the batch renaming sequence against internal string processing failures.
* **Underscore Delimiter Integration:** Restructured the Shroud episode extraction logic to natively accept underscores (`_`) as valid data boundaries.
* **Word Boundary Elimination:** Removed strict `\b` regex limitations that previously forced the engine to output episode `00` when processing files previously named by KageMux. The application can now safely loop its own naming outputs without dropping sequence numbers.

### KageMux v1.1.6 (The Absolute Pathing Hotfix)
This urgent patch protected the core configuration file from temporary data corruption during shell launches.
* **Current Working Directory Anchor:** Fixed a configuration reset error caused by the Windows Context Menu integration. The engine now finds its installation path using an absolute `sys.executable` command instead of relying on the volatile Windows shell CWD.
* **Rogue File Prevention:** This pathing anchor permanently stops the application from dropping blank `kagemux_config.json` templates into media folders during right-click execution.

### KageMux v1.1.5 (The OS Integration Update)
This release elevated the application from a standalone tool into a deeply embedded Windows media workspace.
* **Windows Context Menu Injection:** Built native operating system integration. Operators can toggle system integration inside the Armory Configuration to generate a local registry key, granting them the ability to right-click any folder to launch the workspace with the path pre-loaded.
* **The Karasu Nomenclature Override:** Adjusted the Karasu courier to permanently fix Windows Shell version drift. The updater now takes the old versioned file just to delete it, outputting the new binary specifically as `KageMux.exe` so local shortcuts never break.

### KageMux v1.1.4 (The URL Sanitization Patch)
This update broadened the Shroud Designation validation matrix to stop URL-breaking characters prior to file creation.
* **Expanded Character Ban:** Automatically blocks brackets (`[` and `]`), ampersands (`&`), and plus signs (`+`) from user inputs to prevent URL encoding errors and storage API routing crashes.
* **Automated Failsafe Scrubbing:** Replicated the validation array inside the core renaming code to autonomously remove illegal characters in the background if the GUI checks are bypassed.

### KageMux v1.1.3 (The B2 Routing Override)
This hotfix implemented strict input cleaning to fix routing conflicts with external cloud platforms and URL shorteners.
* **Comma Neutralization:** Built a GUI intercept to immediately stop execution and trigger a warning modal if a comma (`,`) is found in the Show Title or Fansub Group text boxes.
* **Database Integrity:** Modified the core formatting engine to automatically strip commas from the final string, ensuring structural compliance with B2 storage systems.

### KageMux v1.1.2 (The Decimal Decoupling Hotfix)
This rapid logic update overhauled the regex targeting matrix to fix episode extraction bugs triggered by alphanumeric formats and dot-delimited text.
* **Alphanumeric OP/ED Capture:** Improved the capture groups to seamlessly handle alphanumeric theme variations (such as `NCED01`), fixing a boundary error that defaulted these media files to `00`.
* **Resolution Tag Bleed:** Separated base integers from following decimals via a `clean_decimal` function. This explicitly ignores video resolution tags (like `.1080` or `.264`), preventing them from contaminating the fractional episode syntax.

### KageMux v1.1.1 (The Nomenclature Patch)
This update refined the Shroud episode extraction logic to isolate irregular release formats without catching excess metadata.
* **Irregular Format Isolation:** Improved the regex engine to target `OVA`, `ONA`, `Special`, and `SP` variables. The system flawlessly grabs these tags and their integers while dropping trailing resolution metadata like `(BD_1080p)`.
* **Season 0 Preservation Protocol:** Built an explicit bypass for `S00` metadata anomalies. Rather than stripping the season tag and forcing a collision with standard episodes, the system safely preserves the `S00Exx` string for prequels and specials.

### KageMux v1.1.0 (The Courier Protocol)
This significant deployment established fully autonomous updating mechanics and delivered major UI aesthetic optimizations.
* **The Karasu Handoff Protocol:** Built a headless background executable (`karasu.exe`) to bypass Windows file locks. KageMux downloads the payload asynchronously, hands the file to Karasu, and terminates itself. Karasu handles the binary swap, deletes the `.old` file, and reboots the application.
* **Bilateral Control Layout:** Split the top navigation bar into a dynamically stretched format. Theme and Armory settings are anchored left, while the Update checker and Ko-fi portal are anchored right for perfect geometric balance.
* **Shroud Designation UI Polish:** Rebalanced UI proportions by granting 75% space to the Title input and 25% to the Group input. Added an 8-pixel top margin to visually detach inputs from the activation switch.

### KageMux v1.0.3 (The Shroud Fortification)
This rapid update fortified the Shroud Designation Engine to fix Windows pathing errors and deploy intelligent fractional episode padding.
* **Fractional Episode Synchronization:** Built dynamic integer padding for decimal formats. When a fractional episode is detected (like `05.5`), it zero-pads the base integer (`05.0`) to guarantee correct alphanumeric sorting in Windows.
* **Nomenclature Preservation:** Calibrated regex parameters to capture accurate OP and ED string variations instead of aggressively replacing them with generic tags.
* **Strict Character Sanitization:** Hardened the naming logic to actively purge illegal Windows characters (`< > : " / \ | ? *`), completely preventing `[WinError 123]` crashes.
* **Extraction Failsafes:** Modified extraction parameters with strict word boundaries to stop the engine from misidentifying hex CRC values as episode numbers.

### KageMux v1.0.0 (The Architectural Ascension)
This major milestone transitioned KageMux from a basic script into a high-performance Python app by adopting PyQt6 and standardized naming systems.
* **PyQt6 Framework Migration:** Completely overhauled the graphical interface with native PyQt6. Deployed dynamic QSS styling with two aesthetic profiles (ShadowForge Dark and Obsidian Ronin) and thread-safe background processing.
* **Shroud Designation Engine:** Added an autonomous batch renaming protocol to synthesize show titles, resolutions, and fansub groups into a strict format (`(Hi10)_Title_-_01_(1080p)_(Group)_(CRC).mkv`).
* **Omni-Linguist Subtitle Fail-Safe:** Improved the subtitle matrix to intercept blank or `und` metadata, guaranteeing disguised "Signs and Songs" tracks never hijack the default MKV path.
* **Void-State Diagnostics:** Added a diagnostic toggle to the terminal. When armed, the engine catches fatal memory faults and prints raw Python stack traces for rapid debugging.
* **Cyclic Redundancy Bypass:** Rebuilt the batch filter to safely ingest MKV files containing preexisting CRC hashes while maintaining a strict anti-loop barrier for `KageMuxed` directories.

### KageMux v0.9.1 (The Global Routing Update)
This release deployed global audio routing, tightened fallback parameters, and modernized the interface visuals.
* **Global Audio Routing Matrix:** Added a native dropdown to define target languages (Chinese, Korean, English, or Auto) before batch execution. The system dynamically assigns the MKV `Default` flag to the chosen stream.
* **Intelligent Fallback Parameters:** Built a non-blocking fallback loop. If a file lacks the targeted language, the system defaults to Japanese routing to guarantee uninterrupted processing.
* **Missing Tag Inference:** Improved the parsing logic to handle undefined audio streams by reading raw track titles to infer and map the correct ISO 639-2 tags.
* **Modernized UI Rendering:** Bypassed Windows rendering limits on dropdown menus by applying custom X11 styling declarations to match the proprietary dark theme perfectly.

### KageMux v0.8.17 (The Telemetry & Metadata Patch)
This update fixed aggressive metadata erasure bugs and introduced smart language telemetry harvesting.
* **Intelligent Telemetry Harvesting:** The audio engine was upgraded to intercept embedded ISO 639-2 MKV tags, running them through an internal dictionary to output clean, standardized track data.
* **Metadata Preservation Protocol:** Fixed a logic bug that assigned blank text to non-standard audio streams. The engine gracefully falls back to original track names to prevent media players from displaying generic placeholders.
* **Strict Language Flagging:** The engine now explicitly forces the `--language` command flag across all audio tracks to ensure perfect hardware player recognition.

### KageMux v0.8.16 (The TimeWeaver Unification Update)
This patch bridged secondary tools into the global pathing rules and fixed graphical UI anomalies.
* **TimeWeaver Pipeline Unification:** Connected synchronization outputs directly to global routing logic. The system now automatically calculates CRC32 checksums or targets the `KageMuxed` directory based on main user settings.
* **Persistent Taskbar Branding:** Fixed a Windows API bug triggered by drag-and-drop actions by declaring a default global icon sequence for all spawned windows.
* **Transient Modal Architecture:** Configured child dialog boxes to act as transient dependents of the main interface, unlocking local drag-and-drop mechanics for internal text boxes.
* **Streamlined Nomenclature:** Removed redundant "VFR" phrasing across all graphical surfaces to build a cleaner "TimeWeaver" feature identity.

### KageMux v0.8.14 (The Synchronization Milestone)
This major update deployed synchronization tools and overhauled subtitle metadata handling for advanced splitters.
* **VFR TimeWeaver Module:** Added a dual-directory sync tool. The engine uses `mkvextract` to rip Variable Frame Rate timecodes from a source folder and injects them into new encodes, restoring lip-sync automatically.
* **Strict SDH Inclusivity:** Rebuilt the subtitle engine to prioritize Hearing Impaired tracks. The system assigns `Default` and `Hearing Impaired` flags directly to the SDH track for immediate accessibility playback.
* **Standardized Forced Flags:** Fixed LAV Splitter logic issues by reserving the `Forced Display` flag exclusively for "Signs & Songs" tracks, strictly matching MKVToolNix guidelines.
* **Pristine Core Resonance Logging:** Muted raw progress spam from the terminal, allowing the engine to compile files silently while generating clean final reports.

### KageMux v0.8.10 (The Paradox Protocol)
* **Metadata Singularity Enforcement:** Mirrored the internal MKVToolNix GUI logic by forcing the app to strip leftover `Default` flags from secondary streams, ensuring a single default path.
* **Forced Display Overrides:** Shifted subtitle multiplexing parameters from outdated syntax to the modernized `--forced-display-flag` for maximum hardware support.

### KageMux v0.8.5 (The Inclusivity Override)
* **SDH Exclusivity Targeting:** Modified the subtitle logic to stop standard English selection if an SDH track is detected, placing accessibility in the primary slot.
* **Metadata Protection Ring:** Rebuilt the tagging script to preserve unique ripper group identifiers rather than overwriting them with generic normalized languages.

### KageMux v0.8.0 (The Kinetic Telemetry Milestone)
This release drastically reduced user friction by adding OS-aware drag-and-drop processing.
* **Kinetic Drag and Drop Engine:** Operators can drag single files or massive TV batch folders directly from Windows Explorer into the UI for instant pathing.
* **Intelligent Dependency Detection:** The system automatically hunts for MKVToolNix and FFmpeg in default system directories during startup, bypassing manual configuration completely.
* **Native Taskbar Identity:** Hooked into the Windows Shell API to display proprietary branding on the local taskbar.
* **UI State Synchronization:** Progress bars automatically reset to zero the moment a new target is processed.

### KageMux v0.7.2 (The Environment Integration Update)
* **Automated Armory Paths:** Established the foundation for intelligent startup scanning, letting the system verify background dependencies using Windows PATH variables.

### KageMux v0.7.1 (The Metadata Fallback Patch)
This update brought critical resilience mechanics to stop data loss when handling malformed source files.
* **Advanced Tie-Breaker Protocol:** When two duplicate audio codecs of exact quality tie in points, the engine checks physical track length to preserve the full stream while purging truncated samples.
* **Corrupt Header Fallbacks:** If a media file lacks standard duration metadata, the engine runs an aggressive secondary scan to calculate length via embedded byte tags.
* **Lore-Accurate Telemetry:** Updated the terminal to dynamically alter the final summary header based on the active processing pipeline.

### KageMux v0.7.0 (The Architectural Refactor)
* **Unified Scoring Matrix:** Streamlined audio evaluation logic to boost processing speed, lower memory use, and ensure stability across both pipelines.
* **Core Resonance Summaries:** Stopped terminal text spam during multiplexing. The app silently aggregates removals and prints a clean file-by-file summary report at completion.

### KageMux v0.6.3 (The Omni-Linguist Patch)
* **Intelligent Subtitle Parsing:** The system standardizes complex subtitle tags while keeping critical source acronyms intact (like `[CR]`, `[AMZN]`).
* **Serialized Subtitle Metadata:** Unified custom text attributes into clean naming conventions (`(Signs & Songs)`, `(SDH)`).
* **Tactical Visual Overhaul:** Deployed a dark visual aesthetic across the entire interface to lower eye strain during encoding workflows.

### KageMux v0.6.2 (The Core Engine Baseline)
This foundational release established the ShadowForge architecture and advanced automated logic.
* **The ShadowForge Engine:** Deployed the primary audio matrix to filter tracks by codec tier and channel arrays.
* **The Phantom Reconstruct Pipeline:** Added the emergency fallback protocol to repair corrupt headers by extracting naked streams via FFmpeg and rebuilding them.
* **Dual-Audio Routing:** Added automatic recognition of Japanese and English audio to map Default and Forced subtitle flags.
* **Automated Hash Generation:** Injected CRC32 checksum generation to automatically append verification numbers to final filenames.
* **The Armory Configuration:** Added a UI window for operators to manually link backend executable files.

### KageMux v0.3 Release (Initial Prototype)
* **CLI Engine Wrapper:** The foundational proof-of-concept interface that wrapped raw command-line utilities into a basic graphical container.
* **Basic Batch Automation:** Enabled simple folder parsing to negate the need for file-by-file manual track isolation.
