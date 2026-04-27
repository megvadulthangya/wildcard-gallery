## [Unreleased]

### Added
- **Visibility Manager:** New "Visibility Mode" toggle on the Wildcards Filter tab adds Hide / Unhide / Show Hidden Only / Show All (excl. hidden) actions. Hidden wildcards are persisted to `metadata/hidden_wildcards.json` and are also excluded from the txt2img/img2img *Wildcards* Extra Networks tab. While Visibility Mode is active, clicking a card no longer inserts it into the prompt so bulk hide/unhide selection is safe.

### Removed
- **Dead whitelist/blacklist code:** Removed the obsolete `wcc_wildcards_whitelist` and `wcc_wildcards_blacklist` settings page options and the associated dead-code path in `unpack_wildcard_pack()` that wrote imported YAML names back into the whitelist.

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
