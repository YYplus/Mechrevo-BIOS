# MECHREVO BIOS / EC Firmware Archive

[简体中文](README.md) | [English](README_EN.md)

This is a **community-maintained MECHREVO BIOS / EC firmware archive**, organized by model or BIOS platform, with official firmware sources and related version information.

> [!WARNING]
> **Flashing BIOS / EC firmware carries a risk of making the device unbootable.**
>
> Confirm the model, firmware version, and target platform before updating, and keep the device on stable AC power throughout the process.

## BIOS update precautions

The following precautions and update steps are based on instructions provided by MECHREVO customer support.

1. A BIOS update may trigger BitLocker recovery-key verification. Before updating, make sure you know the Microsoft account used to sign in to Windows. You may also disable Device Encryption beforehand. In Windows 11, go to **Start → Settings → Privacy & security → Device encryption**, or search for “Device encryption” from Windows Search.
2. Before running the BIOS updater, exit third-party PC management, security, or protection software to avoid conflicts or blocking.

## BIOS update steps

1. After downloading the BIOS firmware package, right-click it and choose **Extract All**.
2. Make sure the AC adapter is connected, then right-click the BIOS update application and choose **Run as administrator**.
3. Wait for the progress in the updater window to complete, then enter **Y** when prompted to confirm the restart.
4. The computer will restart automatically and complete the BIOS update. Do not use the keyboard or mouse, and do not disconnect power during the update. Wait until the process finishes and Windows starts again automatically.

## Indexed models

| Model / platform | BIOS | EC |
|---|---|---|
| [Yaoshi 15 Pro](models/耀世15-Pro/) | `N.1.15MRO10` | `1.09` |
| [Yaoshi 16 Ultra (X6AR5xxx)](models/耀世16-Ultra-X6AR5xxx/) | `N.1.33MRO63` | `unknown` |
| [Jiaolong 16 Pro (2024–2026)](models/蛟龙16-Pro-2024-2026/) | `N.1.40MRO56` | `unknown` |
| [Yilong 15 Pro (2024) / Jiaolong 16S (GMxHGxx)](models/GMxHGxx/) | `N.1.10MRO28` | `unknown` |
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

Official BIOS / EC firmware files are stored under each entry's `firmware/` directory. Original vendor filenames and official source URLs are preserved. If the vendor site blocks automated downloads, the original file must be added manually.

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
