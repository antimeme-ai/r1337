# Flipper One acquisitions — 2026-10-15

This lane acquired four original GitHub-generated source archives for the [Flipper One report](2026-10-15-flipper-one-frumentarii.md). Original compressed bytes remain unchanged under ignored `quarantine/weird-devices/flipper-one/archives/`; extracted study copies are under `quarantine/weird-devices/flipper-one/extracted/<repository>/`. No acquired program, generator, installer or build was executed. No submodules, firmware images or complete dependency trees were acquired. Archived instructions are historical reference only.

## Exact sources

All repositories belong to the official [flipperdevices organization](https://github.com/flipperdevices). These independent commit pins identify what was acquired; they are not a mutually validated release set. The documentation repository generates the portal from its `public-release` branch, so a pinned source snapshot and a live portal page can differ.

### flipperone-docs

- Revision: [`c82f09d6248e243fd4b214b5746ed1740e1bcd12`](https://github.com/flipperdevices/flipperone-docs/tree/c82f09d6248e243fd4b214b5746ed1740e1bcd12).
- Original archive: [flipperone-docs-c82f09d6248e243fd4b214b5746ed1740e1bcd12.tar.gz](https://codeload.github.com/flipperdevices/flipperone-docs/tar.gz/c82f09d6248e243fd4b214b5746ed1740e1bcd12), 71,439,004 bytes.
- Local archive: `quarantine/weird-devices/flipper-one/archives/flipperone-docs-c82f09d6248e243fd4b214b5746ed1740e1bcd12.tar.gz`.
- SHA-256: `3f0a8f40e9b8bf3f8ab413eafcae0ef37cfc57bc18e90baf8b153d503450ac73`.
- Extracted study root: `quarantine/weird-devices/flipper-one/extracted/flipperone-docs/`.

### flipperone-hardware

- Revision: [`f6f21591643226aa86727a9a637e618b10faf158`](https://github.com/flipperdevices/flipperone-hardware/tree/f6f21591643226aa86727a9a637e618b10faf158).
- Original archive: [flipperone-hardware-f6f21591643226aa86727a9a637e618b10faf158.tar.gz](https://codeload.github.com/flipperdevices/flipperone-hardware/tar.gz/f6f21591643226aa86727a9a637e618b10faf158), 836,306 bytes.
- Local archive: `quarantine/weird-devices/flipper-one/archives/flipperone-hardware-f6f21591643226aa86727a9a637e618b10faf158.tar.gz`.
- SHA-256: `6ba3766caafadd4447b0cbafa492c167c753c39997bc175fd5bf7b4d9fd1640c`.
- Extracted study root: `quarantine/weird-devices/flipper-one/extracted/flipperone-hardware/`.

### flipperone-mcu-firmware

- Revision: [`93d73772144451b582d0ebbd5af61db41e40145e`](https://github.com/flipperdevices/flipperone-mcu-firmware/tree/93d73772144451b582d0ebbd5af61db41e40145e).
- Original archive: [flipperone-mcu-firmware-93d73772144451b582d0ebbd5af61db41e40145e.tar.gz](https://codeload.github.com/flipperdevices/flipperone-mcu-firmware/tar.gz/93d73772144451b582d0ebbd5af61db41e40145e), 440,970 bytes.
- Local archive: `quarantine/weird-devices/flipper-one/archives/flipperone-mcu-firmware-93d73772144451b582d0ebbd5af61db41e40145e.tar.gz`.
- SHA-256: `89dbf0f02b086173f80a2374fe86f68927239c7222184c1bfe5d2abad4ad1754`.
- Extracted study root: `quarantine/weird-devices/flipper-one/extracted/flipperone-mcu-firmware/`.

### flipperone-mechanics

- Revision: [`8d90ad86b3ed2e83e5cf20c538233c9a09dadb8f`](https://github.com/flipperdevices/flipperone-mechanics/tree/8d90ad86b3ed2e83e5cf20c538233c9a09dadb8f).
- Original archive: [flipperone-mechanics-8d90ad86b3ed2e83e5cf20c538233c9a09dadb8f.tar.gz](https://codeload.github.com/flipperdevices/flipperone-mechanics/tar.gz/8d90ad86b3ed2e83e5cf20c538233c9a09dadb8f), 11,849,937 bytes.
- Local archive: `quarantine/weird-devices/flipper-one/archives/flipperone-mechanics-8d90ad86b3ed2e83e5cf20c538233c9a09dadb8f.tar.gz`.
- SHA-256: `d8daf13c7e90c4ebbee2c41ddeb5349bd2aad4cc196bd280c3178bb2573c412b`.
- Extracted study root: `quarantine/weird-devices/flipper-one/extracted/flipperone-mechanics/`.

## What these snapshots contain

`flipperone-docs` preserves the architecture, interfaces, software plans, mechanical explanations and developer/test logs, together with their original referenced image assets. Particularly relevant paths are `docs/general/Tech-Specs.md`, `docs/mcu-firmware/Architecture.md`, `docs/mcu-firmware/MCU-CPU-interconnect.md`, `docs/hardware/`, `docs/mechanics/`, `docs/cpu-software/`, `docs/testing/WiFi-Monitor.md` and `docs/dev-log/9.md`. A repository-wide license file was not found in this snapshot; public availability should not be read as a blanket reuse license.

`flipperone-hardware` contains its README and three images. It points to the [public Altium viewer](https://flipper.365.altium.com/designs/folder-A78C8D02-EA07-49E1-AC7A-E84FAA2AF410); it does not itself contain the mainboard CAD, schematic or BOM. No Altium source project or derived PDF was downloaded in this pass. A repository-wide license file was not found in this snapshot.

`flipperone-mcu-firmware` contains actual RP2350 board/service/interprocessor implementation, including source paths linked in the report. Its `LICENSE.md` and `REUSE.toml` describe most first-party code as MIT, a small Flipper Zero-derived subset as GPL-3.0-or-later, and graphical assets/documentation as CC-BY-SA-4.0, with per-file SPDX headers taking precedence. Third-party components retain their own terms. Git submodule declarations remain present as source records; their dependency code was not recursively downloaded. No build or generated output was produced.

`flipperone-mechanics` includes `CURRENT/B.1/Flipper One (B.1).stp`, artwork and selected third-party accessory geometry. Its root `LICENSE` is CERN Open Hardware Licence Version 2 — Permissive. The README intentionally limits the main-body STEP to external shape; the back plate and antenna rail expose their internal geometry. It is not a complete internal product reconstruction.

Licensing descriptions identify upstream declarations for study; they do not adopt any material as a project dependency or authorize copying it into the product.

## Restore the study corpus

Run from the project root. The following commands download exact pinned archives, check their original bytes, extract fresh study copies and remove nested Git metadata and filesystem detritus. They never invoke upstream code. Existing extracted study copies are expected to be absent; use a fresh destination if preserving another local study.

```sh
mkdir -p quarantine/weird-devices/flipper-one/archives
mkdir -p quarantine/weird-devices/flipper-one/extracted
curl --fail --location --output 'quarantine/weird-devices/flipper-one/archives/flipperone-docs-c82f09d6248e243fd4b214b5746ed1740e1bcd12.tar.gz' 'https://codeload.github.com/flipperdevices/flipperone-docs/tar.gz/c82f09d6248e243fd4b214b5746ed1740e1bcd12'
curl --fail --location --output 'quarantine/weird-devices/flipper-one/archives/flipperone-hardware-f6f21591643226aa86727a9a637e618b10faf158.tar.gz' 'https://codeload.github.com/flipperdevices/flipperone-hardware/tar.gz/f6f21591643226aa86727a9a637e618b10faf158'
curl --fail --location --output 'quarantine/weird-devices/flipper-one/archives/flipperone-mcu-firmware-93d73772144451b582d0ebbd5af61db41e40145e.tar.gz' 'https://codeload.github.com/flipperdevices/flipperone-mcu-firmware/tar.gz/93d73772144451b582d0ebbd5af61db41e40145e'
curl --fail --location --output 'quarantine/weird-devices/flipper-one/archives/flipperone-mechanics-8d90ad86b3ed2e83e5cf20c538233c9a09dadb8f.tar.gz' 'https://codeload.github.com/flipperdevices/flipperone-mechanics/tar.gz/8d90ad86b3ed2e83e5cf20c538233c9a09dadb8f'

shasum -a 256 -c <<'SHA256'
3f0a8f40e9b8bf3f8ab413eafcae0ef37cfc57bc18e90baf8b153d503450ac73  quarantine/weird-devices/flipper-one/archives/flipperone-docs-c82f09d6248e243fd4b214b5746ed1740e1bcd12.tar.gz
6ba3766caafadd4447b0cbafa492c167c753c39997bc175fd5bf7b4d9fd1640c  quarantine/weird-devices/flipper-one/archives/flipperone-hardware-f6f21591643226aa86727a9a637e618b10faf158.tar.gz
89dbf0f02b086173f80a2374fe86f68927239c7222184c1bfe5d2abad4ad1754  quarantine/weird-devices/flipper-one/archives/flipperone-mcu-firmware-93d73772144451b582d0ebbd5af61db41e40145e.tar.gz
d8daf13c7e90c4ebbee2c41ddeb5349bd2aad4cc196bd280c3178bb2573c412b  quarantine/weird-devices/flipper-one/archives/flipperone-mechanics-8d90ad86b3ed2e83e5cf20c538233c9a09dadb8f.tar.gz
SHA256

mkdir 'quarantine/weird-devices/flipper-one/extracted/flipperone-docs'
tar -xzf 'quarantine/weird-devices/flipper-one/archives/flipperone-docs-c82f09d6248e243fd4b214b5746ed1740e1bcd12.tar.gz' --strip-components=1 -C 'quarantine/weird-devices/flipper-one/extracted/flipperone-docs'
mkdir 'quarantine/weird-devices/flipper-one/extracted/flipperone-hardware'
tar -xzf 'quarantine/weird-devices/flipper-one/archives/flipperone-hardware-f6f21591643226aa86727a9a637e618b10faf158.tar.gz' --strip-components=1 -C 'quarantine/weird-devices/flipper-one/extracted/flipperone-hardware'
mkdir 'quarantine/weird-devices/flipper-one/extracted/flipperone-mcu-firmware'
tar -xzf 'quarantine/weird-devices/flipper-one/archives/flipperone-mcu-firmware-93d73772144451b582d0ebbd5af61db41e40145e.tar.gz' --strip-components=1 -C 'quarantine/weird-devices/flipper-one/extracted/flipperone-mcu-firmware'
mkdir 'quarantine/weird-devices/flipper-one/extracted/flipperone-mechanics'
tar -xzf 'quarantine/weird-devices/flipper-one/archives/flipperone-mechanics-8d90ad86b3ed2e83e5cf20c538233c9a09dadb8f.tar.gz' --strip-components=1 -C 'quarantine/weird-devices/flipper-one/extracted/flipperone-mechanics'

find quarantine/weird-devices/flipper-one/extracted -name .git -prune -exec rm -rf {} +
find quarantine/weird-devices/flipper-one/extracted -type d -name __MACOSX -prune -exec rm -rf {} +
find quarantine/weird-devices/flipper-one/extracted -type f \( -name .DS_Store -o -name '._*' \) -delete
```

The original archives were retained unchanged. The extracted trees were scanned after cleanup; no `.git`, `.DS_Store`, `__MACOSX` or AppleDouble `._*` paths remained. SHA-256 values above were read back from the retained archives.

## Located without acquisition

The report links exact inspected repository revisions for image build scripts (`9606c32f91a7798a97e88ea87acffff5b4c80892`), kernel (`d66a9f4f3efa5f14df5db733ef77f8abe68c371a`), U-Boot (`9337c09e4c9ba5b1641a003abd157a6b3e8caf8d`), board tests (`2298fb5b3548dde68cce536e15ecfe1d163c4bd7`), UI/design overview (`d9029a19ef82cb15a9624ec01ec69e5780740483`) and current Slint-based UI (`88cb743d78b6cf3de846a1729e7735293b6d1238`). Their overview/README pages were read online; no corresponding source archives were added. The older FlipCTL vision repository (`3285ba6caf53d41b46f8494c6b7c54422d510449`) still describes WebKit, so the report explicitly flags that drift from the current image builder and UI implementation. No repository list is treated as a tested complete system build.
