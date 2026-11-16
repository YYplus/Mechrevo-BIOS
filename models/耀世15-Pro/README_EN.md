# MECHREVO Yaoshi 15 Pro

[简体中文](README.md) | [English](README_EN.md)

## Model information

Three hardware variants are currently recorded for the Yaoshi 15 Pro:

| Hardware variant | BIOS platform / motherboard | BIOS | EC |
|---|---|---|---|
| 255H | `X6AR45xU` | `N.1.15MRO10` | `1.09` |
| 155H | `XxMT4xxx` | `N.1.07MRO12` | `unknown` |
| i7-14650HX | `GM5IX0A` (motherboard) | `N.1.07MRO15` (tested) | `unknown` |

## BIOS

| Hardware variant | Version | File | Official source |
|---|---|---|---|
| 255H | `N.1.15MRO10` | [`X6AR45xUN115MRO10_CAP.EXE`](firmware/X6AR45xUN115MRO10_CAP.EXE) | [MECHREVO](https://driver.mechrevo.com/d.mechrevo.com/driver/BIOS/Intel_ArrowH45/X6AR45xUN115MRO10_CAP.EXE) |
| 155H | `N.1.07MRO12` | [`XxMT4xxxN107MRO12_CAP.EXE`](firmware/XxMT4xxxN107MRO12_CAP.EXE) | `unknown` |
| i7-14650HX (`GM5IX0A`) | `N.1.07MRO15` | [`GMxIX7xN107MRO15_CAP.EXE`](../耀世16-Pro/firmware/GMxIX7xN107MRO15_CAP.EXE) (shared with Yaoshi 16 Pro) | [MECHREVO](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2026/BIOS/GMxIX7xN107MRO15_CAP.EXE) |

## Known information

- The internal `$FID` for the 255H `N.1.15MRO10` package is `X6AR45xUNd`.
- `N.1.15MRO10` with EC `1.09` has an actual-use record on the 255H variant.
- The 155H variant uses BIOS platform `XxMT4xxx`; the currently archived BIOS is `N.1.07MRO12`.
- **i7-14650HX / `GM5IX0A`:** A user reported successfully updating from BIOS `N.1.07MRO13` using the Yaoshi 16 Pro `GMxIX7xN107MRO15_CAP.EXE` package. The binary is archived once under the [Yaoshi 16 Pro](../耀世16-Pro/) directory.
- **Overseas model sharing the platform family (i7-14650HX / `GM5IX0A`):** XMG FUSION 15 (E24 / `XFU15E24`), motherboard family `GM5IXxA`: [official XMG driver downloads](https://download.schenker-tech.de/package/xmg-fusion-e24-xfu15e24/).
- **Related overseas platform reference (255H / `X6AR45xU`):** XMG FUSION 15 (L25 / `XFU15L25`) uses service-manual platform `X5AR45xS`, not the identical board identifier: [official XMG driver downloads](https://download.schenker-tech.de/package/xmg-fusion-15-l25-xfu15l25/).

## Known issues (255H / `X6AR45xU`)

- **MECHREVO Control Center:** Newer versions of Control Center do not work correctly on this device; the latest known working version is `5.56.60.22`, based on actual use of the 255H variant.
- **Measured Boot / TPM PCR0:** With the current BIOS `N.1.15MRO10` (EC `1.09`), `PCR[0]` reconstructed from the Measured Boot event log still does not match the actual `PCR[0]` read from the TPM. Awaiting a fix from MECHREVO.
