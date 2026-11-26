# MECHREVO Yaoshi 16 Super

[简体中文](README.md) | [English](README_EN.md)

## Model information

| Item | Value |
|---|---|
| Model | Yaoshi 16 Super (2024) |
| Known configuration | Intel Core i9-14900HX + GeForce RTX 4080 Laptop GPU (12 GB) |
| Motherboard model | `GM6IX8B` |
| BIOS platform / firmware prefix | `unknown` |
| Known BIOS version | `N.1.10MRO09` (user report) |
| BIOS date | 2025-01-07 (user report) |
| EC | `unknown` |

## BIOS

| Version | File | Official source |
|---|---|---|
| `N.1.10MRO09` | Not yet obtained | `unknown` |

## Archived firmware linked in the Destroyer report

| BIOS version in the image | Firmware file | Official source | Status |
|---|---|---|---|
| `N.1.11MRO10` | [`GMxIX9xN111MRO10_CAP.exe`](firmware/GMxIX9xN111MRO10_CAP.exe) | [MECHREVO](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2026/BIOS/GMxIX9xN111MRO10_CAP.EXE) | Archived. Target motherboard unconfirmed. |

On 2026-11-26 a firmware lead was received for the Yaoshi 16 Super Destroyer variant (i9-14900HX + RTX 4080). The user reported that an update supplied by customer support resolved blue-screen restarts while playing Phantom Blade in performance mode. The original post lists `N.1.10MRO10`. The archived BIOS image contains the version string `N.1.11MRO10` and the `$FID` project identifier `GMxIX9xN1`. The reporting device’s motherboard identifier remains unconfirmed. **Compatibility with `GM6IX8B` is not established; confirm with MECHREVO customer support before flashing.** Microcode changes are unknown.

## Known information

- Thanks to @Icather for providing model, motherboard, and BIOS version information in [Issue #3](https://github.com/YYplus/Mechrevo-BIOS/issues/3). The reported installed BIOS is `N.1.10MRO09`; whether it is the final version remains unknown.
- [Official MECHREVO driver downloads](https://www.mechrevo.com/cn/products/yao-shi-16-super/downloads/): the contributor reports that no BIOS / EC download is listed. Contact MECHREVO customer support to request the appropriate firmware.
- **Overseas reference model:** XMG NEO 16 (E24 / `XNE16E24`), service-manual motherboard family `GM6IXxB`; known RTX 4080 / 4090 firmware branch version `N1.10A13` / EC `1.15.00`: [official XMG driver downloads](https://download.schenker-tech.de/package/xmg-neo-16-17-e24-xne16e24-xne17e24/). This is a platform and driver reference, not evidence of cross-flash compatibility.
