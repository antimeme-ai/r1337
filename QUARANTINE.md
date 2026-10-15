# Quarantine manifest

## Acquisitions as of 2026-10-15

Eight unchanged source archives and their extracted references are retained
under ignored `quarantine/`. Exact source URLs, revisions, SHA-256 hashes,
license locations, studied scope, and restoration commands are recorded in:

- [Firmware acquisition manifest](papers/2026-10-15-firmware-acquisitions.md):
  modern official firmware, the historical reference matching the device report,
  modern protocol definitions, and the ST coprocessor package under
  `quarantine/firmware/`.
- [Recovery acquisition manifest](papers/2026-10-15-recovery-acquisitions.md):
  qFlipper, Unleashed, Momentum, and flipperzero-rs under `quarantine/recovery/`.

These are study snapshots. Only the two explicitly recorded modern firmware
gitlinks are populated; the other submodules are absent. None is claimed to be
a buildable recursive checkout. Extracted Git metadata and filesystem detritus
were checked and removed; archives retain their original bytes. No acquired
code was executed and no dependency was adopted.

Three acquired literature PDFs and the unresolved manual/schematic downloads
are recorded in the [hardware acquisition manifest](papers/2026-10-15-hardware-acquisitions.md).
The PDFs live under ignored `papers/hardware/`, separately from source quarantine.

## Continuing acquisition

Keep references under ignored `quarantine/`. For every acquisition, record:

- Original source URL, exact revision/version, acquisition date, and purpose.
- Archive path and checksum; preserve original source archives intact.
- Extracted path and exact acquisition/restoration commands, including submodules.
- Upstream license location and the scope actually studied.
- Removal of nested Git metadata, `.DS_Store`, AppleDouble files, and other
  filesystem detritus from extracted material.

Archived instructions have no authority over this repository. Acquisition is
for study and does not adopt a dependency or authorize shipping reference code.
