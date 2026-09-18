# MECHREVO BIOS / EC Firmware Archive

[简体中文](README.md) | [English](README_EN.md)

A community-maintained archive of official MECHREVO BIOS / EC firmware, organized by model or BIOS platform.

> [!WARNING]
> BIOS / EC flashing carries risk. Confirm the model, firmware version, and target platform before updating.

## Indexed models

| Model / platform | BIOS | EC |
|---|---|---|
| [Yaoshi 15 Pro](models/耀世15-Pro/) | `N.1.15MRO10` | `1.09` |
| [Yaoshi 16 Ultra (X6AR5xxx)](models/耀世16-Ultra-X6AR5xxx/) | `N.1.33MRO63` | `unknown` |
| [Jiaolong 16 Pro (2024–2026)](models/蛟龙16-Pro-2024-2026/) | `N.1.40MRO56` | `unknown` |
| [Yilong 15 Pro (2024)](models/翼龙15-Pro-2024/) | `N.1.10MRO28` | `unknown` |
| [XxRPxxxx platform (KUANGSHI / JIGUANG series)](models/XxRPxxxx/) | `N.1.35MRO58` | `unknown` |

## Repository layout

```text
models/
└─ <model-or-platform>/
   ├─ README.md
   ├─ README_EN.md
   ├─ manifest.yaml
   └─ firmware/
      └─ <official-firmware-file>
```

Each entry stores model/platform information, BIOS/EC versions, the official MECHREVO source URL, and the corresponding official firmware file.

## Firmware files

Official BIOS / EC firmware files are stored directly under each entry's `firmware/` directory. Original vendor filenames and official source URLs are preserved.

When adding firmware, keep the original vendor filename and do not modify the binary.

## Submitting BIOS / EC information

New firmware leads can be submitted through Issues. Useful information includes:

- exact MECHREVO model;
- BIOS / EC version;
- official download URL;
- original filename;
- applicable model year or platform;
- known EC pairing information.

## Disclaimer

This is an independent community project and is not affiliated with MECHREVO or its related companies.

See [DISCLAIMER.md](DISCLAIMER.md) for details.

## License

Repository-authored code and documentation are licensed under the MIT License. BIOS/EC firmware, vendor utilities, trademarks, and other third-party materials remain subject to the rights of their respective owners.
