# Mechrevo BIOS

Community-maintained index for MECHREVO BIOS/EC firmware information, official download sources, checksums, compatibility notes, and research records.

> [!WARNING]
> BIOS/EC flashing can render a device unbootable. Always verify the exact machine model, hardware configuration, firmware version, EC dependency, source, and checksum before flashing.

## Project scope

This repository is intended to maintain:

- BIOS and EC version indexes for MECHREVO devices;
- official firmware download links and source records;
- SHA-256 checksums and file metadata;
- known BIOS/EC pairing information;
- verified hardware/model applicability;
- changelog and known-issue notes when evidence is available;
- relationships between MECHREVO models and related ODM/chassis platforms;
- small tools for checksum generation and metadata validation.

Modified firmware is out of scope for the initial version of this repository.

## Repository status labels

| Label | Meaning |
|---|---|
| `official` | File or information originates from an official MECHREVO source. |
| `verified` | Source and/or checksum has been independently checked. |
| `tested` | A matching device has successfully used the firmware. |
| `unverified` | Information has not yet been independently verified. |
| `related` | Firmware/model appears related by chassis or ODM platform, but compatibility is not established. |

`related` never means `compatible`.

## Repository layout

```text
Mechrevo-BIOS/
├─ README.md
├─ DISCLAIMER.md
├─ CONTRIBUTING.md
├─ LICENSE
├─ models/
│  ├─ _template/
│  │  ├─ README.md
│  │  └─ manifest.yaml
│  └─ <model>/
│     ├─ README.md
│     └─ manifest.yaml
├─ docs/
│  ├─ naming.md
│  ├─ metadata.md
│  └─ firmware-policy.md
├─ tools/
│  ├─ checksum/
│  └─ validate/
└─ .github/
   ├─ ISSUE_TEMPLATE/
   └─ workflows/
```

## Adding a model

1. Copy `models/_template/` to `models/<model>/`.
2. Fill in the model README with verified hardware/model information.
3. Add firmware records to `manifest.yaml`.
4. Record the original filename and source URL exactly as published.
5. Generate a SHA-256 checksum for every archived or locally inspected file.
6. Do not claim cross-model compatibility unless it has been independently established.

## Firmware binaries

The Git repository should primarily store metadata, documentation, checksums, and tools.

Firmware binaries should **not** be committed directly to Git by default. If redistribution is later determined to be appropriate, binary archives should preferably be attached to GitHub Releases and clearly identified as third-party firmware not covered by this repository's software license.

## Verification principle

The project follows an evidence-first approach:

- do not infer compatibility from similar filenames alone;
- distinguish official source records from mirrors;
- distinguish same-chassis relationships from actual firmware compatibility;
- preserve original filenames and checksums;
- mark unknown fields as `unknown` rather than guessing.

## Disclaimer

This is an independent community project and is not affiliated with MECHREVO or its related companies. See [DISCLAIMER.md](DISCLAIMER.md).

## License

Repository-authored code and documentation are licensed under the MIT License unless otherwise stated. Third-party firmware and vendor materials remain subject to their respective rights holders' terms.
