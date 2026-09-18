# Firmware binary policy

The initial repository policy is metadata-first.

## Allowed in Git

- Markdown documentation;
- YAML/JSON metadata;
- checksums;
- small scripts;
- links to official sources;
- user-supplied factual compatibility reports.

## Not committed by default

- BIOS binaries;
- EC binaries;
- vendor flashing executables;
- vendor packages containing copyrighted firmware.

If binary redistribution is later adopted, files should preferably be attached to GitHub Releases rather than committed into Git history. Each release should contain source provenance, checksum information, model applicability, and a clear third-party-rights notice.
