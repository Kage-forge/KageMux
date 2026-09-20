# ⚡ The ShadowForge Archives: Project Milestones

This ledger tracks the architectural evolution of KageMux. From its origins as a rudimentary command-line wrapper to a fully autonomous, kinetic media workspace, each milestone represents a calculated upgrade in container optimization and pipeline automation.

***

### KageMux v1.1.9 (The Matrix Decoupling & UI Polish Update)
This structural update reorganized the graphical user interface for a logical, top-to-bottom workflow and eliminated native Windows rendering artifacts.
* **ShadowSight Intercept Integration:** Formally rebranded the interactive pre-flight modal and shifted it up the visual hierarchy to guarantee a sequential workflow configuration.
* **Decoupled Output Routing:** Separated the CRC32 hashing protocol from the directory routing logic. Users can now independently append standalone hashes and bypass the `KageMuxed` folder entirely to output directly alongside source files.
* **State Machine Locking:** Engineered an autonomous locking mechanism that visually checks and disables the standalone CRC checkbox the moment the Shroud Designation Engine is armed, preventing conflicting hashing loops.
* **Interface Rendering Polish:** Injected strict QSS transparency declarations into the `QScrollArea` to override legacy Windows operating system graphics, deploying a modern, rounded scrollbar handle. Additionally, stripped redundant text from the overarching progress labels to safely delegate numerical percentage tracking to the native PyQt6 progress bars.

### KageMux v1.1.8 (The ShadowSight Intercept Protocol)
This feature deployment introduced a manual override capability to bypass standard mathematical track scoring.
* **Interactive Pre-Flight Scan:** Deployed a synchronous, thread-safe intercept that halts the background worker before multiplexing begins. The engine scans the first MKV file and populates a graphical modal containing all available subtitle tracks.
* **Mathematical Obliteration:** Upgraded the subtitle scoring matrix to accept manual inputs. The engine now assigns a massive 500,000-point override to the user's selected track signature, cleanly bypassing standard tie-breaker logic (such as ASS versus SRT codec comparisons).
* **Nameless Track Synchronization:** Engineered a strict metadata fallback that explicitly assigns "Unknown Track" to blank subtitle streams across both the user interface and the core engine, guaranteeing that forced selections never fail due to string mismatches.

### KageMux v1.1.7 (The Recursive Blindness Patch)
This logic hotfix fortified the batch renamer against internal string failures.
* **Underscore Delimiter Integration:** Rebuilt the Shroud Designation Engine's episode extraction matrix to natively recognize underscores (`_`) as valid metadata boundaries.
* **Word Boundary Elimination:** Stripped the strict `\b` regex constraints that previously caused the engine to default to episode `00` when processing files that were already formatted by KageMux. The tool can now safely re-process its own naming outputs without losing sequence integers.

### KageMux v1.1.6 (The Absolute Pathing Hotfix)
This rapid deployment secured the core configuration file against temporary data loss during external shell launches.
* **Current Working Directory Anchor:** Resolved a critical configuration amnesia bug triggered by the Windows Context Menu integration. The engine now queries its exact installation path using an absolute `sys.executable` resolver rather than relying on the volatile Windows shell CWD.
* **Rogue File Prevention:** This absolute anchoring permanently prevents the application from mistakenly dropping blank `kagemux_config.json` files into target media directories during right-click context menu launches.

### KageMux v1.1.5 (The OS Integration Update)
This deployment transitioned the application from a standalone utility into a deeply integrated Windows media workspace by standardizing the deployment architecture.[cite: 23]
* **Windows Context Menu Injection:** Engineered native operating system integration. Users can now toggle system integration within the Armory Configuration to write a localized registry key, allowing them to right-click any directory in Windows Explorer to instantly launch the workspace with the target path natively queued.[cite: 23]
* **The Karasu Nomenclature Override:** Re-engineered the Karasu background courier to permanently resolve Windows Shell version drift. The updater now accepts the old versioned filename strictly for deletion and outputs the new binary exclusively as `KageMux.exe`, guaranteeing the local executable name perfectly matches the internal GUI version.[cite: 23]

### KageMux v1.1.4 (The URL Sanitization Patch)
This update expanded the Shroud Designation Engine's validation matrix to neutralize URL-breaking characters before file generation.[cite: 23]
* **Expanded Character Ban:** Actively intercepts and blocks brackets (`[` and `]`), ampersands (`&`), and plus signs (`+`) in user inputs to completely prevent URL encoding standard violations and cloud storage API routing failures.[cite: 23]
* **Automated Failsafe Scrubbing:** Mirrored the expanded validation array within the core renaming logic to autonomously strip illegal characters in the background if the graphical user interface validation is somehow bypassed.[cite: 23]

### KageMux v1.1.3 (The B2 Routing Override)
This patch introduced strict input sanitization to resolve critical routing conflicts with external cloud storage providers and link shorteners.[cite: 23]
* **Comma Neutralization:** Engineered a GUI intercept to immediately halt execution and deploy a targeted modal warning if a comma (`,`) is detected in the Show Title or Fansub Group fields.[cite: 23]
* **Database Integrity:** Re-engineered the underlying formatting engine to systematically scrub commas from the final string, guaranteeing structural compatibility with B2 storage ecosystems.[cite: 23]

### KageMux v1.1.2 (The Decimal Decoupling Hotfix)
This rapid logic hotfix overhauled the regex targeting matrix to resolve episode extraction failures caused by complex alphanumeric strings and dot-delimited metadata.[cite: 23]
* **Alphanumeric OP/ED Capture:** Upgraded the capture groups to seamlessly process alphanumeric theme song variations (e.g., `NCED01`), neutralizing a boundary failure that previously defaulted these files to `00`.[cite: 23]
* **Resolution Tag Bleed:** Decoupled base integers from subsequent decimals and deployed a `clean_decimal` validation function. This explicitly filters out known video resolution or codec strings (like `.1080`, `.720`, `.264`), preventing them from bleeding into the fractional episode syntax.[cite: 23]

### KageMux v1.1.1 (The Nomenclature Patch)
This rapid logic patch refined the Shroud Designation Engine's episode extraction matrix to natively isolate irregular release formats without capturing garbage metadata.[cite: 23]

* **Irregular Format Isolation:** Upgraded the regular expression engine to actively target `OVA`, `ONA`, `Special`, and `SP` strings. The engine now flawlessly captures these tags and their associated integers (e.g., converting `OVA 01` or `SP-02` into `OVA_01` and `Special_02`) while automatically discarding trailing resolution tags or ripper metadata like `(BD_1080p)`.[cite: 23]
* **Season 0 Preservation Protocol:** Engineered an explicit bypass for `S00` metadata anomalies. Instead of stripping the season tag and forcing a collision with main series episodes, the engine safely preserves the `S00Exx` string. This isolates prequels and promotional specials, preventing batch overwrites and granting the user total control over manual bulk renaming workflows.[cite: 23]

### KageMux v1.1.0 (The Courier Protocol)
This major deployment cycle introduced fully autonomous, in-place updating capabilities alongside critical spatial layout and aesthetic optimizations.[cite: 23]

* **The Karasu Handoff Protocol:** Engineered a headless background courier (`karasu.exe`) to bypass strict Windows OS executable file locks. KageMux natively streams the binary payload via an asynchronous `DownloadWorker` thread, hands the temporary file to Karasu, and safely self-terminates. Karasu executes the binary swap, aggressively polls the OS to purge the `.old` backup file, and cleanly reboots the workspace.[cite: 23]
* **Bilateral Control Layout:** Decoupled the top navigation bar into a dynamically stretched, split layout. Theme and Armory configurations are permanently anchored left, while the Update checker and the newly integrated Ko-fi Support portal are anchored right, ensuring perfect geometric balance across varying monitor sizes.[cite: 23]
* **Shroud Designation UI Polish:** Rebalanced horizontal UI elements by allocating 3 parts (75%) of available space to the Title input and 1 part (25%) to the Group input. Injected an exact 8-pixel top margin to visually separate the input parameters from the activation toggle. Compressed the Group placeholder text to strictly read `"e.g., SubsPlease"` to entirely eliminate visual cutoff within the condensed bounding box.[cite: 23]

### KageMux v1.0.3 (The Shroud Fortification)
This rapid deployment cycle fortified the Shroud Designation Engine, resolving critical Windows pathing anomalies and introducing intelligent fractional episode synchronization.[cite: 23]

* **Fractional Episode Synchronization:** Engineered dynamic integer padding for decimal releases. When the engine detects a fractional episode (like `05.5`), it automatically zero-pads the corresponding base integer (`05.0`) to guarantee flawless alphanumeric sorting within the Windows Shell.[cite: 23]
* **Nomenclature Preservation:** Calibrated the regex extraction boundaries to capture exact OP and ED string variations (e.g., `OP2`, `ED1A`) instead of aggressively overwriting them with generic sequence tags.[cite: 23]
* **Strict Character Sanitization:** Hardened the naming matrix to actively intercept and purge illegal Windows filename characters (`< > : " / \ | ? *`), completely neutralizing `[WinError 123]` thread crashes before execution.[cite: 23]
* **Extraction Failsafes:** Re-engineered the episode extraction parameters with strict word boundaries to prevent the system from accidentally interpreting hexadecimal CRC values or video resolutions as episode integers.[cite: 23]

### KageMux v1.0.0 (The Architectural Ascension)
This major milestone fundamentally transformed KageMux from a lightweight utility into a scalable, high-performance Python application by shedding legacy frameworks and deploying strictly standardized naming protocols.[cite: 23]

* **PyQt6 Framework Migration:** Completely rebuilt the graphical interface using native PyQt6. Introduced dynamic QSS rendering with two persistent aesthetic profiles (ShadowForge Dark and Obsidian Ronin) and established thread-safe background execution via `pyqtSignal` objects.[cite: 23]
* **Shroud Designation Engine:** Integrated an autonomous batch renaming protocol. The engine automatically extracts episode integers from source files and synthesizes the show title, resolution, and fansub group into a strict, unified format (e.g., `(Hi10)_Title_-_01_(1080p)_(Group)_(CRC).mkv`), successfully bridging the gap between raw rips and standardized archival formats.[cite: 23]
* **Omni-Linguist Subtitle Fail-Safe:** Upgraded the subtitle parsing matrix to intercept catastrophically blank or undefined (`und`) language metadata. The engine now guarantees that disguised "Signs and Songs" tracks can never hijack the default MKV slot, forcefully elevating the primary dialogue track.[cite: 23]
* **Void-State Diagnostics:** Deployed a critical diagnostic toggle directly into the Core Resonance terminal. When activated, the engine intercepts fatal memory faults and exposes raw Python stack traces, transforming silent application crashes into actionable developer intelligence.[cite: 23]
* **Cyclic Redundancy Bypass:** Re-engineered the batch filtering logic. KageMux now securely ingests and processes third-party MKV files containing preexisting CRC hashes while simultaneously maintaining a strict anti-loop barrier for its own `KageMuxed` output directories.[cite: 23]

### KageMux v0.9.1 (The Global Routing Update)
KageMux crossed the 0.9.x threshold by deploying scalable global audio routing, tightening the ShadowForge fallback parameters, and completely modernizing the interface architecture.[cite: 23]

* **Global Audio Routing Matrix:** Introduced a native dropdown menu to define primary target languages (Chinese, Korean, English, or Auto) prior to batch execution. The engine dynamically scans each file and assigns the MKV `Default` flag to the selected stream.[cite: 23]
* **Intelligent Fallback Parameters:** Engineered a non-blocking fallback loop. If a queued file lacks the preferred language, the engine safely defaults to standard anime routing (Japanese, followed by English) to guarantee uninterrupted batch processing.[cite: 23]
* **Missing Tag Inference:** Upgraded the parsing matrix to handle `und` (Undefined) audio streams. The engine now scans raw track titles to infer and map the correct ISO 639-2 tag automatically, neutralizing messy ripper conventions.[cite: 23]
* **Modernized UI Rendering:** Bypassed legacy Windows rendering limitations on dropdown menus by injecting custom X11 styling declarations. The combobox lists now perfectly align with the proprietary KageMux dark theme without stark white popups.[cite: 23]

### KageMux v0.8.17 (The Telemetry & Metadata Patch)
This critical patch resolved aggressive metadata erasure bugs and introduced intelligent language telemetry harvesting.[cite: 23]

* **Intelligent Telemetry Harvesting:** The audio scoring engine was upgraded to actively intercept embedded ISO 639-2 MKV language tags (such as `chi` or `jpn`), routing them through an internal dictionary to generate clean, standardized track metadata.[cite: 23]
* **Metadata Preservation Protocol:** Resolved a logical flaw that assigned blank strings to non-standard audio streams. The engine gracefully falls back to original track names, completely preventing media players from wiping titles and displaying generic placeholders like "Audio 2".[cite: 23]
* **Strict Language Flagging:** The engine was updated to explicitly enforce the `--language` command flag across all audio outputs, guaranteeing perfect hardware and software player recognition.[cite: 23]

### KageMux v0.8.16 (The TimeWeaver Unification Update)
This release bridged secondary toolsets into the global application parameters and resolved critical graphical interface anomalies within the Windows Shell.[cite: 23]

* **TimeWeaver Pipeline Unification:** Integrated synchronization outputs directly into global pathing rules. The engine now automatically calculates and appends CRC32 checksums or routes processed files to a dedicated `KageMuxed` directory based on the primary user configuration.[cite: 23]
* **Persistent Taskbar Branding:** Resolved a Windows API anomaly triggered by drag-and-drop modules. By declaring a default global icon sequence, the system prevents the OS from reverting to default system visual assets across spawned child windows.[cite: 23]
* **Transient Modal Architecture:** Engineered child dialog boxes to act as transient dependents of the main interface. This architectural shift unlocked localized drag-and-drop mechanics for internal text fields and improved taskbar window grouping.[cite: 23]
* **Streamlined Nomenclature:** Stripped redundant "VFR" branding across all graphical and terminal surfaces to establish a cleaner, more definitive "TimeWeaver" feature identity.[cite: 23]

### KageMux v0.8.14 (The Synchronization Milestone)
This major update deployed precision synchronization tools and completely overhauled subtitle metadata adherence to eliminate playback paradoxes across advanced splitters.[cite: 23]

* **VFR TimeWeaver Module:** Deployed a dedicated dual-directory synchronization tool. The engine utilizes `mkvextract` to rip native Variable Frame Rate (VFR) timecodes from a source folder and injects them directly into re-encoded outputs, perfectly restoring duration and lip-sync without terminal commands.[cite: 23]
* **Strict SDH Inclusivity:** Rebuilt the subtitle parser to prioritize Subtitles for the Deaf and Hard of Hearing. The engine automatically assigns `Default` and `Hearing Impaired` flags strictly to the SDH track, ensuring automatic playback across all platforms.[cite: 23]
* **Standardized Forced Flags:** Resolved LAV Splitter logic conflicts by explicitly reserving the `Forced Display` flag solely for isolated "Signs & Songs" tracks, mathematically aligning the output with official MKVToolNix specifications.[cite: 23]
* **Pristine Core Resonance Logging:** Silenced redundant progress text from the terminal output. The engine compiles files silently in the background, relying entirely on the graphical progress bar and generating clean, uninterrupted terminal reports.[cite: 23]

### KageMux v0.8.10 (The Paradox Protocol)
* **Metadata Singularity Enforcement:** Replicated the internal logic of the MKVToolNix GUI by forcing the application to explicitly strip residual `Default` flags from all secondary audio and video streams. This ensures a solitary default path, preventing player confusion and incorrect subtitle selection.[cite: 23]
* **Forced Display Overrides:** Transitioned the subtitle multiplexing syntax from legacy parameters to the modernized `--forced-display-flag` for total hardware compatibility.[cite: 23]

### KageMux v0.8.5 (The Inclusivity Override)
* **SDH Exclusivity Targeting:** Adjusted the subtitle scanning logic to halt standard English track selection if an SDH or CC track is detected in the telemetry, forcing accessibility directly into the primary path.[cite: 23]
* **Metadata Protection Ring:** Re-engineered the subtitle tagging script to strictly preserve unique ripper group identifiers and codec strings instead of aggressively overwriting them with normalized base languages.[cite: 23]

### KageMux v0.8.0 (The Kinetic Telemetry Milestone)
This release elevated the application into an OS-aware workspace, drastically reducing user friction and expanding batch processing fluidity.[cite: 23]

* **Kinetic Drag and Drop Engine:** Users can now drag single files or massive television batch directories directly from Windows Explorer into the application for instantaneous pathing.[cite: 23]
* **Intelligent Dependency Detection:** The engine automatically hunts for required software dependencies (MKVToolNix and FFmpeg) in default system paths upon startup, entirely bypassing the need for manual configuration.[cite: 23]
* **Native Taskbar Identity:** Hooked directly into the Windows Shell API to display proprietary KageMux branding on the taskbar.[cite: 23]
* **UI State Synchronization:** Progress bars and telemetry spinners automatically snap back to zero the moment a new target is queued.[cite: 23]

### KageMux v0.7.2 (The Environment Integration Update)
* **Automated Armory Paths:** Laid the groundwork for intelligent startup scanning, allowing the application to autonomously verify background dependencies using Windows PATH variables.[cite: 23]

### KageMux v0.7.1 (The Metadata Fallback Patch)
This patch introduced critical resilience mechanics to prevent data loss when processing catastrophically malformed source files.[cite: 23]

* **Advanced Tie-Breaker Protocol:** When the scoring engine detects two duplicate audio codecs of identical quality, it now evaluates the physical length of the tracks. The engine automatically preserves the full-length audio stream while purging truncated samples or isolated theme songs.[cite: 23]
* **Corrupt Header Fallbacks:** If a source file is missing standard duration metadata, the engine executes an aggressive secondary scan to calculate track length via embedded byte and frame tags.[cite: 23]
* **Lore-Accurate Telemetry:** The terminal was updated to dynamically rebrand the final summary block based on the active pipeline (outputting either **THE SHADOWFORGED REPORT** or **THE PHANTOM-RECONSTRUCTED REPORT**).[cite: 23]

### KageMux v0.7.0 (The Architectural Refactor)
* **Unified Scoring Matrix:** Streamlined the underlying track evaluation logic to increase processing speed, reduce memory footprint, and guarantee stability across both optimization pipelines.[cite: 23]
* **Core Resonance Summaries:** Eliminated terminal text spam during multiplexing. The application now silently aggregates all track removals in the background and prints a highly readable, file-by-file summary report at the end of the batch.[cite: 23]

### KageMux v0.6.3 (The Omni-Linguist Patch)
* **Intelligent Subtitle Parsing:** The engine dynamically standardizes complex subtitle tags while actively preserving critical VOD source acronyms (e.g., `[CR]`, `[AMZN]`, `[HIDIVE]`).[cite: 23]
* **Serialized Subtitle Metadata:** Unified custom subtitle attributes into clean, standardized naming conventions (such as `(Signs & Songs)`, `(SDH)`, and `(Korean Names)`).[cite: 23]
* **Tactical Visual Overhaul:** Deployed a dark, low-contrast visual theme across the entire interface to reduce eye strain during extended encoding sessions.[cite: 23]

### KageMux v0.6.2 (The Core Engine Baseline)
This was the foundational release that established the overarching ShadowForge architecture and introduced advanced automated logic.[cite: 23]

* **The ShadowForge Engine:** Introduced the primary audio scoring matrix to rank and filter audio tracks by codec hierarchy (prioritizing FLAC/Opus over Dolby Digital, and Dolby Digital over AAC) and channel configurations.[cite: 23]
* **The Phantom Reconstruct Pipeline:** Built the emergency fallback routine to fix corrupt headers and desynchronized audio. This pipeline brutally extracts raw streams via FFmpeg and rebuilds them into pristine containers via MKVMerge.[cite: 23]
* **Dual-Audio Routing:** Enabled automatic detection of Japanese and English audio streams to dynamically map Default and Forced subtitle flags for anime releases.[cite: 23]
* **Automated Hash Generation:** Added CRC32 checksum calculations, automatically appending verification tags to finalized filenames.[cite: 23]
* **The Armory Configuration:** Introduced a dedicated UI modal for users to manually link and test the required backend executables.[cite: 23]

### KageMux v0.3 Release (Initial Prototype)
* **CLI Engine Wrapper:** The original proof-of-concept interface that bridged raw command-line tools into a basic graphical environment.[cite: 23]
* **Basic Batch Automation:** Enabled foundational folder parsing to eliminate the need for manual track selection on a file-by-file basis.[cite: 23]
