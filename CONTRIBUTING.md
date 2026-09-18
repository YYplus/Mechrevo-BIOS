# Contributing

Contributions are welcome when they improve the accuracy and traceability of the firmware index.

## Evidence requirements

Please provide as much of the following as possible:

- exact MECHREVO model name;
- chassis/ODM identifier if known;
- BIOS version;
- EC version;
- original firmware filename;
- official source URL or archived source information;
- release date if documented;
- SHA-256 checksum;
- whether the firmware was actually tested on matching hardware;
- screenshots or vendor release notes when useful.

Unknown information should be written as `unknown`. Do not infer missing facts.

## Compatibility claims

Do not mark firmware as compatible with another model merely because:

- the filename looks similar;
- the BIOS version string is similar;
- the devices appear to use the same chassis;
- another brand sells a visually similar machine.

Cross-model compatibility should only be documented when there is reliable evidence.

## Binary submissions

Do not open a pull request containing firmware binaries unless the repository policy explicitly permits it. Prefer metadata, checksums, source links, and release records.
