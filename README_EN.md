# MECHREVO BIOS / EC Firmware Archive

[简体中文](README.md) | [English](README_EN.md)

As MECHREVO has not provided a unified, comprehensive **public BIOS / EC firmware download index**, this community-maintained repository collects, organizes, and archives official firmware, download links, and version information for MECHREVO models to make firmware easier to find and obtain.

> [!WARNING]
> **Flashing BIOS / EC firmware carries a risk of making the device unbootable.**
>
> Confirm the model, firmware version, and target platform before updating, and keep the device on stable AC power throughout the process.

> [!NOTE]
> **A practical way to look for newer BIOS releases**
>
> The directory structure and filename pattern used by MECHREVO's official BIOS downloads are now relatively predictable. When looking for a newer BIOS, you can first find the corresponding or same-chassis model from **XMG**, use its newer BIOS version as a version-number reference, and then try replacing the version number in an existing MECHREVO official download URL to check whether a corresponding newer file already exists on MECHREVO's server.

## BIOS update precautions

The following precautions and update steps are based on instructions provided by MECHREVO customer support.

1. A BIOS update may trigger BitLocker recovery-key verification. Before updating, make sure you know the Microsoft account used to sign in to Windows. You may also disable Device Encryption beforehand. In Windows 11, go to **Start → Settings → Privacy & security → Device encryption**, or search for “Device encryption” from Windows Search.
2. Before running the BIOS updater, exit third-party PC management, security, or protection software to avoid conflicts or blocking.

## BIOS update steps

1. If the download is an archive, right-click it and choose **Extract All** first. If the download is already a `.EXE` BIOS updater, proceed directly to the next step.
2. Make sure the AC adapter is connected, then right-click the BIOS update application and choose **Run as administrator**.
3. Wait for the progress in the updater window to complete, then enter **Y** when prompted to confirm the restart.
4. The computer will restart automatically and complete the BIOS update. Do not use the keyboard or mouse, and do not disconnect power during the update. Wait until the process finishes and Windows starts again automatically.

## Indexed models

This index is organized by product series. Select a model to open its detail page for configurations, firmware files, official download URLs, and overseas reference models. CPU, motherboard model, and BIOS platform are listed separately. **“Not confirmed” means the available archive contains no reliable information; a BIOS platform or filename prefix is not necessarily the motherboard model.**

### Wujie Series

| Model | Processor | Motherboard | BIOS platform | BIOS | EC |
|---|---|---|---|---|---|
| [Wujie 14XA / Wujie 14X (AMD)](models/无界14XA-8845HS/) | AMD Ryzen 7 8845HS | Not confirmed | `GXxHXxx` (filename prefix) | `N.1.14MRO50` | Not confirmed |

### Yaoshi Series

| Model | Processor | Motherboard | BIOS platform | BIOS | EC |
|---|---|---|---|---|---|
| [Yaoshi 15 Pro](models/耀世15-Pro/) | Core Ultra 9 255H / Core Ultra 7 155H / Core i7-14650HX | `GM5IX0A` (14650HX; other variants not confirmed) | `X6AR45xU` / `XxMT4xxx` / `GMxIX7x` | `N.1.15MRO10` (255H) / `N.1.07MRO12` (155H) / `N.1.07MRO15` (14650HX) | `1.09` (255H); others not confirmed |
| [Yaoshi 16 Pro](models/耀世16-Pro/) | Intel Core i7-14650HX | `GM6IX7B` | `GMxIX7x` | `N.1.07MRO15` | Not confirmed |
| [Yaoshi 16 Ultra](models/耀世16-Ultra-X6AR5xxx/) | Intel Core Ultra 7 255HX | Not confirmed | `X6AR5xxx` | `N.1.33MRO63` | Not confirmed |

### Jiaolong Series

| Model | Processor | Motherboard | BIOS platform | BIOS | EC |
|---|---|---|---|---|---|
| [Jiaolong 5](models/蛟龙5/) | Not confirmed | Not confirmed | Not confirmed | Not confirmed (official ZIP URL indexed) | Not confirmed |
| [Jiaolong 16K](models/蛟龙16K/) | Not confirmed | Not confirmed | Not confirmed | `N.1.26MRO24` (official ZIP URL indexed) | Not confirmed |
| [Jiaolong 16 Pro](models/蛟龙16-Pro/) | Multiple configurations; see model page | Not confirmed | `MRID6-23` / `X6DR5xxK` / `X6FR55xx` | `MRID6_23_V40` / `N.1.49MRO58` / `N.1.39MRO55` | Not confirmed |
| [Jiaolong 16S](models/GMxHGxx/) | Not confirmed | Not confirmed | `GMxHGxx` | `N.1.10MRO28` | Not confirmed |

### Yilong Series

| Model | Processor | Motherboard | BIOS platform | BIOS | EC |
|---|---|---|---|---|---|
| [Yilong 15 Pro (2024)](models/GMxHGxx/) | Not confirmed | Not confirmed | `GMxHGxx` | `N.1.10MRO28` | Not confirmed |

> Yilong 15 Pro (2024) and Jiaolong 16S share the `GMxHGxx` firmware entry. Both links point to the same directory; the firmware binary is archived only once.

### Kuangshi Series

| Model | Processor | Motherboard | BIOS platform | BIOS | EC |
|---|---|---|---|---|---|
| [Kuangshi 16 Pro](models/旷世16-Pro/) | Intel Core i9-13900HX | `GM6PX0X` | `GMxPX7x` | `N.1.09MRO15` | Not confirmed |
| [Kuangshi X](models/耀世16-Ultra-X6AR5xxx/) | Intel Core Ultra 7 255HX | Not confirmed | `X6AR5xxx` | `N.1.33MRO63` | Not confirmed |

> Kuangshi X and Yaoshi 16 Ultra share the same `X6AR5xxx` BIOS entry. See the corresponding page under Yaoshi Series for details.

### Jiguang Series

| Model | Processor | Motherboard | BIOS platform | BIOS | EC |
|---|---|---|---|---|---|
| [Jiguang X Pro](models/XxRPxxxx/) | Not confirmed | Not confirmed | `XxRPxxxx` | `N.1.35MRO58` | Not confirmed |

## Repository layout

```text
models/
└─ <model-or-platform>/
   ├─ README.md
   ├─ README_EN.md
   ├─ manifest.yaml
   └─ firmware/
      └─ <firmware-file>
```

Each entry stores model/platform information, BIOS/EC versions, the original MECHREVO source URL when known, and the archived firmware file.

## Firmware files

BIOS / EC firmware files are stored under each entry's `firmware/` directory with the original MECHREVO filename preserved. The original source URL is recorded when known.

Do not modify firmware binaries before committing them.

## Submitting BIOS / EC information

New firmware leads can be submitted through Issues. Useful information includes:

- exact MECHREVO model;
- BIOS / EC version;
- official download URL, if available;
- original filename;
- applicable model year or platform;
- known EC pairing information.

## Disclaimer

This is an independent community project and is not affiliated with MECHREVO or its related companies, and it does not represent official MECHREVO technical support.

Flashing BIOS / EC firmware is a high-risk operation. Before using firmware from this repository, verify the model, hardware variant, platform, and firmware version, and retain important data and the BitLocker recovery key. Users assume the risks associated with flashing, upgrading, or downgrading firmware.

See [DISCLAIMER.md](DISCLAIMER.md) for the full disclaimer.

## License

Repository-authored code and documentation are licensed under the MIT License. MECHREVO BIOS/EC firmware, flashing utilities, trademarks, and other vendor materials remain subject to the rights of their respective owners.
