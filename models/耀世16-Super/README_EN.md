# MECHREVO Yaoshi 16 Super

[简体中文](README.md) | [English](README_EN.md)

## Model information

| Item | Value |
|---|---|
| Model | Yaoshi 16 Super (2024) |
| Known configuration | Intel Core i9-14900HX + GeForce RTX 4080 Laptop GPU (12 GB) |
| Motherboard model | `GM6IX8B` |
| BIOS platform / firmware prefix | `GMxIX9x` (reported System ROM ID: `GMxIX9xN`) |
| Known BIOS version | `N.1.10MRO09` (user report) |
| BIOS date | 2025-01-07 (user report) |
| EC | `unknown` |

## BIOS

| Version | File | Official source |
|---|---|---|
| `N.1.10MRO09` | `GMxIX9xN110MRO09_CAP.EXE` (reported successful flash; not archived) | `unknown` |

## Archived firmware linked in the Destroyer report

| BIOS version from filename | Firmware file | Official source | Status |
|---|---|---|---|
| `N.1.11MRO10` | [`GMxIX9xN111MRO10_CAP.exe`](firmware/GMxIX9xN111MRO10_CAP.exe) | [MECHREVO](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2026/BIOS/GMxIX9xN111MRO10_CAP.EXE) | Archived; reported ROM family matches, newer version not flash-tested. |

On 2026-11-26 a firmware lead was received for the Yaoshi 16 Super Destroyer variant (i9-14900HX + RTX 4080). The user reported that an update supplied by customer support resolved blue-screen restarts while playing Phantom Blade in performance mode. The original post lists `N.1.10MRO10`. The archived version `N.1.11MRO10` is recorded from the official filename, which differs from the original report's `N.1.10MRO10`. No reproducible extracted-image result confirming the internal version or `$FID` is available here. Actual flashing of this newer version on `GM6IX8B` remains unconfirmed. Microcode changes are unknown.

## Additional user test data (2026-11-26)

Thanks to @Icather for the [follow-up in Issue #3](https://github.com/YYplus/Mechrevo-BIOS/issues/3#issuecomment-7189742406):

- DMI System Model is `yaoshi16 Super Series GM6IX8B`, while AFU `/S` reports System ROM ID `GMxIX9xN`. These are different identifiers; differing prefixes alone do not establish incompatibility.
- On 2026-08-04 the contributor successfully flashed `GMxIX9xN110MRO09_CAP.EXE`, reporting successful FFS, RomLayout and Secure Flash checks. The newer filename belongs to the same ROM family, but the contributor has not reported flashing the newer package.
- The browser-downloaded newer official EXE reportedly measures 10,936,672 bytes, matching the archived file size (full content not independently compared). The reported HTTP Last-Modified value is 2026-11-06 10:00:41 GMT; this is not necessarily the BIOS date or release date.
- The contributor reports an AFU overlay using `@UAFP` and no internal version or ROM ID in the plaintext scan. Searching the wrapper is not a substitute for inspecting the extracted image; do not run a flash updater just to inspect a version.
- Windows reported microcode `0x120` after the older version was flashed. The newer microcode remains unknown.

**The ROM family match is supported by user test data, not a successful flash of the newer version. Confirm the exact hardware and firmware applicability before updating.**

## Known information

- Thanks to @Icather for providing model, motherboard, and BIOS version information in [Issue #3](https://github.com/YYplus/Mechrevo-BIOS/issues/3). The reported installed BIOS is `N.1.10MRO09`; whether it is the final version remains unknown.
- [Official MECHREVO driver downloads](https://www.mechrevo.com/cn/products/yao-shi-16-super/downloads/): the contributor reports that no BIOS / EC download is listed. Contact MECHREVO customer support to request the appropriate firmware.
- **Overseas reference model:** XMG NEO 16 (E24 / `XNE16E24`), service-manual motherboard family `GM6IXxB`; known RTX 4080 / 4090 firmware branch version `N1.10A13` / EC `1.15.00`: [official XMG driver downloads](https://download.schenker-tech.de/package/xmg-neo-16-17-e24-xne16e24-xne17e24/). This is a platform and driver reference, not evidence of cross-flash compatibility.
