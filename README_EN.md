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

Models are organized into six product series. Select a model to open its directory for firmware versions, download links, and related information.

### 01 · Wujie Series

[Wujie 14XA / Wujie 14X (AMD 8845HS variant)](models/无界14XA-8845HS/)

---

### 02 · Yaoshi Series

[Yaoshi 15 Pro](models/耀世15-Pro/), [Yaoshi 16 Pro](models/耀世16-Pro/), [Yaoshi 16 Super](models/耀世16-Super/), [Yaoshi 16 Ultra](models/耀世16-Ultra-X6AR5xxx/)

---

### 03 · Jiaolong Series

[Jiaolong 5](models/蛟龙5/), [Jiaolong 16K](models/蛟龙16K/), [Jiaolong 16 Pro](models/蛟龙16-Pro/), [Jiaolong 16S](models/GMxHGxx/)

---

### 04 · Yilong Series

[Yilong 15 Pro (2024)](models/GMxHGxx/)

---

### 05 · Kuangshi Series

[Kuangshi 16 Pro](models/旷世16-Pro/), [Kuangshi X](models/耀世16-Ultra-X6AR5xxx/)

---

### 06 · Jiguang Series

[Jiguang X Pro](models/XxRPxxxx/)

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

You are welcome to share firmware leads in [Discussions](https://github.com/YYplus/Mechrevo-BIOS/discussions). **All we need is the MECHREVO model name and either a BIOS / EC firmware download link or the firmware file itself.** Other details are optional.

## Disclaimer

This is an independent community project and is not affiliated with MECHREVO or its related companies, and it does not represent official MECHREVO technical support.

Flashing BIOS / EC firmware is a high-risk operation. Before using firmware from this repository, verify the model, hardware variant, platform, and firmware version, and retain important data and the BitLocker recovery key. Users assume the risks associated with flashing, upgrading, or downgrading firmware.

See [DISCLAIMER.md](DISCLAIMER.md) for the full disclaimer.

## License

Repository-authored code and documentation are licensed under the MIT License. MECHREVO BIOS/EC firmware, flashing utilities, trademarks, and other vendor materials remain subject to the rights of their respective owners.
