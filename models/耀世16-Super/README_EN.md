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
| `N.1.11MRO10` | [`GMxIX9xN111MRO10_CAP.exe`](firmware/GMxIX9xN111MRO10_CAP.exe) | [MECHREVO](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2026/BIOS/GMxIX9xN111MRO10_CAP.EXE) | Archived. `$FID` matches this model's ROM ID family; microcode unknown. |

On 2026-11-26 a firmware lead was received for the Yaoshi 16 Super Destroyer variant (i9-14900HX + RTX 4080). The user reported that an update supplied by customer support resolved blue-screen restarts while playing Phantom Blade in performance mode. The original post lists `N.1.10MRO10`. The archived BIOS image contains the version string `N.1.11MRO10` and the `$FID` project identifier `GMxIX9xN1`.

**On the `GMxIX9x` prefix:** `GM6IX8B` is the DMI motherboard name, while AFU `/S` prints `System ROM ID` as `GMxIX9xN`. `GMxIX9xN110MRO09_CAP.EXE` was flashed successfully on the same GM6IX8B unit on 2026-08-04 (FFS pass, RomLayout pass, Secure Flash verified), so `GMxIX9x` is this model's ROM family and the prefix difference is not evidence of incompatibility.

**No plaintext version data in the package:** a full-file ASCII and UTF-16LE scan of the archived CAP.EXE finds no `N.1.11MRO10`, `GMxIX9xN1` or `MRO10`; the single `$FID` hit sits in `.rdata` and belongs to AFU itself. The version values therefore come from the unpacked image. The package is AMI AFU 5.15.03 (PE32+ x64) with an `@UAF` archive starting at overlay `0x110000`, unsigned.

**Downloaded file:** `sha256 eeccef4a80cf47784d443f34fe80def73b7e950173e074d4d434eaf0cabb4edb`, 10,936,672 B, vendor `Last-Modified` 2026-11-06.

**Still not an approved upgrade:** microcode changes are unknown, and the previous `N.1.10MRO09` build left the CPU microcode revision at `0x120`. Confirm applicability with MECHREVO customer support before flashing.

## Known information

- Thanks to @Icather for providing model, motherboard, and BIOS version information in [Issue #3](https://github.com/YYplus/Mechrevo-BIOS/issues/3). The reported installed BIOS is `N.1.10MRO09`; whether it is the final version remains unknown.
- [Official MECHREVO driver downloads](https://www.mechrevo.com/cn/products/yao-shi-16-super/downloads/): the contributor reports that no BIOS / EC download is listed. Contact MECHREVO customer support to request the appropriate firmware.
- **Overseas reference model:** XMG NEO 16 (E24 / `XNE16E24`), service-manual motherboard family `GM6IXxB`; known RTX 4080 / 4090 firmware branch version `N1.10A13` / EC `1.15.00`: [official XMG driver downloads](https://download.schenker-tech.de/package/xmg-neo-16-17-e24-xne16e24-xne17e24/). This is a platform and driver reference, not evidence of cross-flash compatibility.
