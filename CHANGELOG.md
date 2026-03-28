## [2.1.0] - 2026-03-28

### Added
- **Recursive Directory Scanning:** Added `os.walk` to correctly index wildcards nested within subdirectories instead of just the root folder.
- **Text-only Fallback:** Wildcards without corresponding preview images (`.jpg`/`.png`) are now properly indexed and displayed as text cards in the gallery.

### Changed
- **Gradio 4.40 Compatibility:** Completely refactored UI components (`gr.File`, `gr.Dataset`, `gr.HTML`) to support Gradio 4.x and the SD WebUI Forge environment. Removed deprecated parameters like `type='file'` and `sanitize=False`.
- **Event Listeners:** Migrated dataset interactions to use Gradio 4's strict `.select()` events for proper wildcard string injection into prompts.

### Removed
- **Whitelist Enforcement:** Completely removed the obsolete whitelist checking logic that prevented wildcards from being indexed automatically.
- **Gradio 3 Dependency:** Removed warnings and legacy structures strictly tying the extension to Gradio 3.x.

## [2.0.0] - 2025-07-31

### Added
- Initial release of Webui wildcard gallery V2.
