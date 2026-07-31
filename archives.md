# ⚡ The ShadowForge Archives: Project Milestones

This ledger tracks the architectural evolution of KageMux. From its origins as a rudimentary command-line wrapper to a fully autonomous, kinetic media workspace, each milestone represents a calculated upgrade in container optimization and pipeline automation.

---

### KageMux v0.8.16 (The TimeWeaver Unification Update)
This release bridged secondary toolsets into the global application parameters and resolved critical graphical interface anomalies within the Windows Shell.

* **TimeWeaver Pipeline Unification:** Integrated synchronization outputs directly into global pathing rules. The engine now automatically calculates and appends CRC32 checksums or routes processed files to a dedicated `KageMuxed` directory based on the primary user configuration.
* **Persistent Taskbar Branding:** Resolved a Windows API anomaly triggered by drag-and-drop modules. By declaring a default global icon sequence, the system prevents the OS from reverting to default system visual assets across spawned child windows.
* **Transient Modal Architecture:** Engineered child dialog boxes to act as transient dependents of the main interface. This architectural shift unlocked localized drag-and-drop mechanics for internal text fields and improved taskbar window grouping.
* **Streamlined Nomenclature:** Stripped redundant "VFR" branding across all graphical and terminal surfaces to establish a cleaner, more definitive "TimeWeaver" feature identity.

### KageMux v0.8.14 (The Synchronization Milestone)
This major update deployed precision synchronization tools and completely overhauled subtitle metadata adherence to eliminate playback paradoxes across advanced splitters.

* **VFR TimeWeaver Module:** Deployed a dedicated dual-directory synchronization tool. The engine utilizes `mkvextract` to rip native Variable Frame Rate (VFR) timecodes from a source folder and injects them directly into re-encoded outputs, perfectly restoring duration and lip-sync without terminal commands.
* **Strict SDH Inclusivity:** Rebuilt the subtitle parser to prioritize Subtitles for the Deaf and Hard of Hearing. The engine automatically assigns `Default` and `Hearing Impaired` flags strictly to the SDH track, ensuring automatic playback across all platforms.
* **Standardized Forced Flags:** Resolved LAV Splitter logic conflicts by explicitly reserving the `Forced Display` flag solely for isolated "Signs & Songs" tracks, mathematically aligning the output with official MKVToolNix specifications.
* **Pristine Core Resonance Logging:** Silenced redundant progress text from the terminal output. The engine compiles files silently in the background, relying entirely on the graphical progress bar and generating clean, uninterrupted terminal reports.

### KageMux v0.8.10 (The Paradox Protocol)
* **Metadata Singularity Enforcement:** Replicated the internal logic of the MKVToolNix GUI by forcing the application to explicitly strip residual `Default` flags from all secondary audio and video streams. This ensures a solitary default path, preventing player confusion and incorrect subtitle selection.
* **Forced Display Overrides:** Transitioned the subtitle multiplexing syntax from legacy parameters to the modernized `--forced-display-flag` for total hardware compatibility.

### KageMux v0.8.5 (The Inclusivity Override)
* **SDH Exclusivity Targeting:** Adjusted the subtitle scanning logic to halt standard English track selection if an SDH or CC track is detected in the telemetry, forcing accessibility directly into the primary path.
* **Metadata Protection Ring:** Re-engineered the subtitle tagging script to strictly preserve unique ripper group identifiers and codec strings instead of aggressively overwriting them with normalized base languages.

### KageMux v0.8.0 (The Kinetic Telemetry Milestone)
This release elevated the application into an OS-aware workspace, drastically reducing user friction and expanding batch processing fluidity.

* **Kinetic Drag and Drop Engine:** Users can now drag single files or massive television batch directories directly from Windows Explorer into the application for instantaneous pathing.
* **Intelligent Dependency Detection:** The engine automatically hunts for required software dependencies (MKVToolNix and FFmpeg) in default system paths upon startup, entirely bypassing the need for manual configuration.
* **Native Taskbar Identity:** Hooked directly into the Windows Shell API to display proprietary KageMux branding on the taskbar.
* **UI State Synchronization:** Progress bars and telemetry spinners automatically snap back to zero the moment a new target is queued.

### KageMux v0.7.2 (The Environment Integration Update)
* **Automated Armory Paths:** Laid the groundwork for intelligent startup scanning, allowing the application to autonomously verify background dependencies using Windows PATH variables.

### KageMux v0.7.1 (The Metadata Fallback Patch)
This patch introduced critical resilience mechanics to prevent data loss when processing catastrophically malformed source files.

* **Advanced Tie-Breaker Protocol:** When the scoring engine detects two duplicate audio codecs of identical quality, it now evaluates the physical length of the tracks. The engine automatically preserves the full-length audio stream while purging truncated samples or isolated theme songs.
* **Corrupt Header Fallbacks:** If a source file is missing standard duration metadata, the engine executes an aggressive secondary scan to calculate track length via embedded byte and frame tags.
* **Lore-Accurate Telemetry:** The terminal was updated to dynamically rebrand the final summary block based on the active pipeline (outputting either **THE SHADOWFORGED REPORT** or **THE PHANTOM-RECONSTRUCTED REPORT**).

### KageMux v0.7.0 (The Architectural Refactor)
* **Unified Scoring Matrix:** Streamlined the underlying track evaluation logic to increase processing speed, reduce memory footprint, and guarantee stability across both optimization pipelines.
* **Core Resonance Summaries:** Eliminated terminal text spam during multiplexing. The application now silently aggregates all track removals in the background and prints a highly readable, file-by-file summary report at the end of the batch.

### KageMux v0.6.3 (The Omni-Linguist Patch)
* **Intelligent Subtitle Parsing:** The engine dynamically standardizes complex subtitle tags while actively preserving critical VOD source acronyms (e.g., `[CR]`, `[AMZN]`, `[HIDIVE]`).
* **Serialized Subtitle Metadata:** Unified custom subtitle attributes into clean, standardized naming conventions (such as `(Signs & Songs)`, `(SDH)`, and `(Korean Names)`).
* **Tactical Visual Overhaul:** Deployed a dark, low-contrast visual theme across the entire interface to reduce eye strain during extended encoding sessions.

### KageMux v0.6.2 (The Core Engine Baseline)
This was the foundational release that established the overarching ShadowForge architecture and introduced advanced automated logic.

* **The ShadowForge Engine:** Introduced the primary audio scoring matrix to rank and filter audio tracks by codec hierarchy (prioritizing FLAC/Opus over Dolby Digital, and Dolby Digital over AAC) and channel configurations.
* **The Phantom Reconstruct Pipeline:** Built the emergency fallback routine to fix corrupt headers and desynchronized audio. This pipeline brutally extracts raw streams via FFmpeg and rebuilds them into pristine containers via MKVMerge.
* **Dual-Audio Routing:** Enabled automatic detection of Japanese and English audio streams to dynamically map Default and Forced subtitle flags for anime releases.
* **Automated Hash Generation:** Added CRC32 checksum calculations, automatically appending verification tags to finalized filenames.
* **The Armory Configuration:** Introduced a dedicated UI modal for users to manually link and test the required backend executables.

### KageMux v0.3 Release (Initial Prototype)
* **CLI Engine Wrapper:** The original proof-of-concept interface that bridged raw command-line tools into a basic graphical environment.
* **Basic Batch Automation:** Enabled foundational folder parsing to eliminate the need for manual track selection on a file-by-file basis.
