# MECHREVO BIOS / EC Firmware Index

[简体中文](README.md) | [English](README_EN.md)

This is a community-maintained **MECHREVO BIOS / EC firmware index and archive**, covering BIOS and EC versions for different models, official download sources, file checksums, known compatibility information, and related maintenance records.

> [!WARNING]
> **Flashing BIOS / EC firmware carries a risk of making a device unbootable.**
>
> Before updating any firmware, verify:
>
> - the exact model and hardware configuration;
> - the current BIOS / EC version;
> - the target model for the firmware;
> - whether the BIOS and EC have pairing requirements;
> - the original firmware source;
> - the file's SHA-256 checksum.

## What this repository maintains

This repository collects:

- BIOS / EC versions for MECHREVO models;
- official firmware download links and source records;
- original filenames, file sizes, and SHA-256 checksums;
- known BIOS / EC pairings;
- real-device flashing verification records;
- official changelogs and known issues;
- chassis / ODM platform relationships between MECHREVO models;
- relationships with same-chassis models from other brands;
- firmware checksum and metadata validation tools.

The current focus is on **original vendor firmware**. Modified BIOS images are not maintained.

## Indexed models

| Model | BIOS | EC | Record |
|---|---|---|---|
| [耀世 15 Pro](models/耀世15-Pro/) | `N.1.15MRO10` | `1.09` | Added |
| [XxRPxxxx platform (KUANGSHI / JIGUANG Series)](models/XxRPxxxx/) | `N.1.35MRO58` | `unknown` | Added |
| [Yaoshi 16 Ultra (X6AR5xxx)](models/耀世16-Ultra-X6AR5xxx/) | `N.1.33MRO63` | `unknown` | Added |

## Status labels

Each firmware record can use one or more of the following labels:

| Status | Meaning |
|---|---|
| `official` | The file or information comes from an official MECHREVO source |
| `verified` | The source, file, or checksum has been independently verified |
| `tested` | The firmware has been flashed and verified on the corresponding model |
| `unverified` | The information has not yet been independently verified |
| `related` | Related to a model, chassis, or ODM platform, but firmware compatibility has not been established |

In particular:

> **`related` ≠ `compatible`**

For example, if a MECHREVO model uses the same chassis as an XMG, Tongfang, or other-brand model, that only establishes a platform relationship. It does not by itself establish that their BIOS firmware can be cross-flashed.

## Repository structure

```text
Mechrevo-BIOS/
├─ README.md
├─ README_EN.md
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

## Model and firmware records

Each model has its own directory:

```text
models/<model-name>/
├─ README.md
└─ manifest.yaml
```

A model page is mainly used to display:

- model name;
- hardware platform;
- chassis / ODM information;
- BIOS version history;
- EC version history;
- BIOS / EC pairings;
- official download sources;
- known issues;
- related same-chassis models.

`manifest.yaml` stores structured firmware metadata for automated indexing and consistency checks.

## Firmware files

The repository currently follows a **metadata-first** approach.

Git history mainly stores:

- firmware version information;
- official download links;
- original filenames;
- SHA-256 checksums;
- model applicability;
- BIOS / EC pairings;
- verification status;
- documentation and tools.

BIOS / EC binaries are **not committed directly to Git history by default**.

If official firmware later becomes unavailable or difficult to obtain, and redistribution is considered appropriate, GitHub Releases should be preferred for archival rather than committing binaries directly to the repository.

## SHA-256 verification

Windows PowerShell:

```powershell
.\tools\checksum\sha256.ps1 "C:\path\to\firmware.exe"
```

Linux:

```bash
./tools/checksum/sha256.sh firmware.exe
```

Where possible, each firmware record should include a SHA-256 checksum so that files from different sources can be compared byte-for-byte.

## Information verification

This project follows an evidence-first approach:

- do not infer compatibility from similar filenames;
- do not infer cross-flash compatibility solely from a shared chassis;
- clearly distinguish official sources from third-party mirrors;
- preserve the vendor's original filename;
- record SHA-256 whenever possible;
- mark unconfirmed fields as `unknown`;
- record user testing separately from official applicability information;
- preserve supporting evidence for disputed or higher-risk compatibility claims.

## Submitting BIOS / EC information

New firmware information can be submitted through **Issues**.

Please provide as much of the following as possible:

- exact MECHREVO model;
- BIOS or EC type;
- firmware version;
- original filename;
- official download URL;
- SHA-256;
- whether it has been flashed on actual hardware;
- BIOS / EC versions before and after flashing;
- any other information that helps establish the source or model applicability.

Unverified information may still be submitted, but please clearly identify which fields have not been verified.

## Disclaimer

This is an independent community project and is not affiliated with MECHREVO or its related companies.

BIOS / EC updates carry risk. Users should independently verify the device model, firmware source, and applicability before flashing.

See [DISCLAIMER.md](DISCLAIMER.md) for details.

## License

Repository-authored code and documentation are licensed under the MIT License by default.

BIOS, EC firmware, flashing utilities, trademarks, and other third-party materials remain subject to the rights of their respective owners.
