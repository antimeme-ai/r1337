# Flipper aftermarket acquisitions — 2026-10-15

Corpus for [the aftermarket survey](2026-10-15-flipper-aftermarket-frumentarii.md): **four original pinned source/hardware archives and two original PDFs**. Archives remain unchanged in ignored `quarantine/aftermarket-flipper/archives/`; extracted study copies are in `quarantine/aftermarket-flipper/extracted/`. PDFs remain unchanged under ignored `papers/aftermarket-flipper/`. No reference code, generator, test, installer, build or firmware was executed. No dependencies were recursively fetched or adopted. Source media and nested manufacturer documents remain within their original archives, not republished separately.

## Original archives

### killergeek/nard

- Revision: [`64c63042eeb1a115a46c5cb9e4e8a52923bb3845`](https://github.com/killergeek/nard/tree/64c63042eeb1a115a46c5cb9e4e8a52923bb3845); upstream committer timestamp `2024-11-25T22:07:02Z`.
- Exact source: [nard archive](https://codeload.github.com/killergeek/nard/tar.gz/64c63042eeb1a115a46c5cb9e4e8a52923bb3845).
- Original file: `quarantine/aftermarket-flipper/archives/nard-64c63042eeb1a115a46c5cb9e4e8a52923bb3845.tar.gz` (5,638,259 bytes).
- SHA-256: `020b1b07dc65c4aa8fc872ddb6f5938a4d8801055651faa1b916bf0364b0e031`.
- Study tree: `quarantine/aftermarket-flipper/extracted/nard/`.

### bettse/seader

- Revision: [`abc2a54c9d0c22c57b56c6a06459658fc1d7dd4a`](https://github.com/bettse/seader/tree/abc2a54c9d0c22c57b56c6a06459658fc1d7dd4a); upstream committer timestamp `2026-08-26T01:55:51Z`.
- Exact source: [seader archive](https://codeload.github.com/bettse/seader/tar.gz/abc2a54c9d0c22c57b56c6a06459658fc1d7dd4a).
- Original file: `quarantine/aftermarket-flipper/archives/seader-abc2a54c9d0c22c57b56c6a06459658fc1d7dd4a.tar.gz` (36,141,468 bytes).
- SHA-256: `08b5639c2e7b3120714cb6f85b0e8befa4b23645ebc8739c57e4329789f61776`.
- Study tree: `quarantine/aftermarket-flipper/extracted/seader/`.

### mtoolstec/fz-uhf-expansion

- Revision: [`8280ee566c4fcb44ddc2d3b0428c584e8a619b71`](https://github.com/mtoolstec/fz-uhf-expansion/tree/8280ee566c4fcb44ddc2d3b0428c584e8a619b71); upstream committer timestamp `2026-10-13T15:18:16Z`.
- Exact source: [fz-uhf-expansion archive](https://codeload.github.com/mtoolstec/fz-uhf-expansion/tar.gz/8280ee566c4fcb44ddc2d3b0428c584e8a619b71).
- Original file: `quarantine/aftermarket-flipper/archives/fz-uhf-expansion-8280ee566c4fcb44ddc2d3b0428c584e8a619b71.tar.gz` (201,423 bytes).
- SHA-256: `9b5466fef8bf88702c58763a02b0865a303ad739c9ab5c55c54dac7365d9e38f`.
- Study tree: `quarantine/aftermarket-flipper/extracted/fz-uhf-expansion/`.

### Didgitalpunk/UHF-RFID_SAM-interface_Board

- Revision: [`a9db9edc497dc1768d0f6be6ef2bac62b11ccd42`](https://github.com/Didgitalpunk/UHF-RFID_SAM-interface_Board/tree/a9db9edc497dc1768d0f6be6ef2bac62b11ccd42); upstream committer timestamp `2026-01-28T16:22:49Z`.
- Exact source: [UHF-RFID_SAM-interface_Board archive](https://codeload.github.com/Didgitalpunk/UHF-RFID_SAM-interface_Board/tar.gz/a9db9edc497dc1768d0f6be6ef2bac62b11ccd42).
- Original file: `quarantine/aftermarket-flipper/archives/UHF-RFID_SAM-interface_Board-a9db9edc497dc1768d0f6be6ef2bac62b11ccd42.tar.gz` (33,264,044 bytes).
- SHA-256: `659aea4531ad5b39ae61d0333287d71d0d26c4235e73fe8f16b8d38425bfc00b`.
- Study tree: `quarantine/aftermarket-flipper/extracted/UHF-RFID_SAM-interface_Board/`.

### Read scope and upstream terms

- **NARD:** read `README.md`, root `LICENSE`, the KiCad hardware-file inventory and relevant SEC1210/connector portions of `Hardware/nard_sam.kicad_sch`. The project publishes original board CAD, BOM-related component references and Gerbers; it is a contact-card carrier, not an RF reader. Root `LICENSE` declares MIT. No PCB manufacturing or complete netlist verification occurred.
- **Seader:** read `readme.md`, `board_identity.{c,h}`, UART initialization/defaults, portions of `hf_interface_fal/hf.c`, CCID/SAM interface paths, UHF capability probing and USB-reader implementation/README. These establish separate HF, SAM and UHF-carrier responsibilities, not complete correctness or tag coverage. Root `LICENSE` contains GPLv3. `.gitmodules` remains as source documentation; submodules were not populated. Media assets are preserved in the original archive, not relied upon as our own test results.
- **MTools UHF Expansion:** read `README.md`, `CHANGELOG.md`, `application.fam`, protocol interface/implementation, serial/reset initialization and documented tag-memory/saved-record limits. Snapshot manifest says 1.6 while the online catalog showed 1.5; the store still describes an older, narrower Flipper role. Root `LICENSE` declares MIT. Reader-module firmware/hardware was not acquired or audited. No memory operation was performed.
- **FlipperMeister carrier:** read `README.md`, `UHF RFID board BOM V2.6.csv`, relevant SEC1210/SAM/header/reader portions of `UHF RFID board.kicad_sch`, the YRM1001 schematic inventory, case-file inventory, and the included Microchip SEC1210 datasheet feature overview. The archive includes additional component documents, CAD and photographs not exhaustively read. README permits personal/free distribution with attribution but requires agreement for commercial board sales; no blanket open-hardware commercial license was found. Embedded manufacturer documents keep their own terms. Published CAD/BOM filenames and repository pin do not establish the revision a seller currently ships.

Archived instructions are historical reference, not workspace instructions. These are study references, not product source or selected dependencies.

## Original PDFs

- [microchip-sec1110-sec1210-ds00001561e.pdf](https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/00001561E.pdf) → `papers/aftermarket-flipper/microchip-sec1110-sec1210-ds00001561e.pdf`; 2,284,287 bytes; SHA-256 `3d50372dd19b6208d8d431769a8729142330ea279461e991e527404416a252dc`.
- [lab401-digilab-schematic-3e1e27054cdc0de4a3a8e2e2480060d2ff2afd55.pdf](https://raw.githubusercontent.com/lab-401/fzDigiLab/3e1e27054cdc0de4a3a8e2e2480060d2ff2afd55/hw/DIGILAB_SCHEMATICS.pdf) → `papers/aftermarket-flipper/lab401-digilab-schematic-3e1e27054cdc0de4a3a8e2e2480060d2ff2afd55.pdf`; 128,295 bytes; SHA-256 `792c67a8bb8a08cdcbe8de445012f4a5b96126a5aadeae6d3158bfd3d3a86873`.

The **Microchip PDF** is *SEC1110/SEC1210 — Smart Card Bridge to USB and UART Interfaces*, DS00001561E, ©2013–2022, 220 PDF pages. Read the feature/interface overview on printed pages 1–2, including ISO7816, T=0/T=1, card voltages, UART/USB variants and supply limits. No claim of a full 220-page controller/firmware audit is made. The exact manufacturer URL was obtained from Microchip's [SEC1210 product page](https://www.microchip.com/en-us/product/sec1210). Manufacturer copyright/terms apply.

The **DigiLab PDF** is the original two-page drawing `hw/DIGILAB_SCHEMATICS.pdf` from lab-401/fzDigiLab revision `3e1e27054cdc0de4a3a8e2e2480060d2ff2afd55` (committer timestamp 2025-10-20T07:15:39Z). Drawing title DIGILAB, Rev 1.3.2, dated 2025-09-24; both sheets were rendered and visually read. Sheet 1 connects the conditioned ADC/comparator paths to Flipper and exposes memory/bus headers; sheet 2 contains the divider, TLV9061 buffer/RC path and TLV3501 comparator. This supports topology interpretation, not a verified bandwidth/accuracy claim. The repository's app license is GPLv3; a separate explicit hardware/drawing license was not established in this pass despite the README's open-hardware description. The source app README and `401DigiLabApp/scenes/scope/401DigiLab_scope.c` were read online at this revision, without downloading a full app archive.

Rendered DigiLab study images are ignored derivatives under `quarantine/aftermarket-flipper/derived/`. Restore them, if useful, with the final `pdftoppm` command below; they are not additional original acquisitions.

## Restoration

Run from the project root, with fresh extraction directories. Downloads are pinned where possible and checks use retained original bytes. The commands never execute upstream code.

```sh
mkdir -p quarantine/aftermarket-flipper/archives
mkdir -p quarantine/aftermarket-flipper/extracted
mkdir -p papers/aftermarket-flipper
curl --fail --location --output 'quarantine/aftermarket-flipper/archives/nard-64c63042eeb1a115a46c5cb9e4e8a52923bb3845.tar.gz' 'https://codeload.github.com/killergeek/nard/tar.gz/64c63042eeb1a115a46c5cb9e4e8a52923bb3845'
curl --fail --location --output 'quarantine/aftermarket-flipper/archives/seader-abc2a54c9d0c22c57b56c6a06459658fc1d7dd4a.tar.gz' 'https://codeload.github.com/bettse/seader/tar.gz/abc2a54c9d0c22c57b56c6a06459658fc1d7dd4a'
curl --fail --location --output 'quarantine/aftermarket-flipper/archives/fz-uhf-expansion-8280ee566c4fcb44ddc2d3b0428c584e8a619b71.tar.gz' 'https://codeload.github.com/mtoolstec/fz-uhf-expansion/tar.gz/8280ee566c4fcb44ddc2d3b0428c584e8a619b71'
curl --fail --location --output 'quarantine/aftermarket-flipper/archives/UHF-RFID_SAM-interface_Board-a9db9edc497dc1768d0f6be6ef2bac62b11ccd42.tar.gz' 'https://codeload.github.com/Didgitalpunk/UHF-RFID_SAM-interface_Board/tar.gz/a9db9edc497dc1768d0f6be6ef2bac62b11ccd42'
curl --fail --location --output 'papers/aftermarket-flipper/microchip-sec1110-sec1210-ds00001561e.pdf' 'https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/00001561E.pdf'
curl --fail --location --output 'papers/aftermarket-flipper/lab401-digilab-schematic-3e1e27054cdc0de4a3a8e2e2480060d2ff2afd55.pdf' 'https://raw.githubusercontent.com/lab-401/fzDigiLab/3e1e27054cdc0de4a3a8e2e2480060d2ff2afd55/hw/DIGILAB_SCHEMATICS.pdf'

shasum -a 256 -c <<'SHA256'
020b1b07dc65c4aa8fc872ddb6f5938a4d8801055651faa1b916bf0364b0e031  quarantine/aftermarket-flipper/archives/nard-64c63042eeb1a115a46c5cb9e4e8a52923bb3845.tar.gz
08b5639c2e7b3120714cb6f85b0e8befa4b23645ebc8739c57e4329789f61776  quarantine/aftermarket-flipper/archives/seader-abc2a54c9d0c22c57b56c6a06459658fc1d7dd4a.tar.gz
9b5466fef8bf88702c58763a02b0865a303ad739c9ab5c55c54dac7365d9e38f  quarantine/aftermarket-flipper/archives/fz-uhf-expansion-8280ee566c4fcb44ddc2d3b0428c584e8a619b71.tar.gz
659aea4531ad5b39ae61d0333287d71d0d26c4235e73fe8f16b8d38425bfc00b  quarantine/aftermarket-flipper/archives/UHF-RFID_SAM-interface_Board-a9db9edc497dc1768d0f6be6ef2bac62b11ccd42.tar.gz
3d50372dd19b6208d8d431769a8729142330ea279461e991e527404416a252dc  papers/aftermarket-flipper/microchip-sec1110-sec1210-ds00001561e.pdf
792c67a8bb8a08cdcbe8de445012f4a5b96126a5aadeae6d3158bfd3d3a86873  papers/aftermarket-flipper/lab401-digilab-schematic-3e1e27054cdc0de4a3a8e2e2480060d2ff2afd55.pdf
SHA256

mkdir 'quarantine/aftermarket-flipper/extracted/nard'
tar -xzf 'quarantine/aftermarket-flipper/archives/nard-64c63042eeb1a115a46c5cb9e4e8a52923bb3845.tar.gz' --strip-components=1 -C 'quarantine/aftermarket-flipper/extracted/nard'
mkdir 'quarantine/aftermarket-flipper/extracted/seader'
tar -xzf 'quarantine/aftermarket-flipper/archives/seader-abc2a54c9d0c22c57b56c6a06459658fc1d7dd4a.tar.gz' --strip-components=1 -C 'quarantine/aftermarket-flipper/extracted/seader'
mkdir 'quarantine/aftermarket-flipper/extracted/fz-uhf-expansion'
tar -xzf 'quarantine/aftermarket-flipper/archives/fz-uhf-expansion-8280ee566c4fcb44ddc2d3b0428c584e8a619b71.tar.gz' --strip-components=1 -C 'quarantine/aftermarket-flipper/extracted/fz-uhf-expansion'
mkdir 'quarantine/aftermarket-flipper/extracted/UHF-RFID_SAM-interface_Board'
tar -xzf 'quarantine/aftermarket-flipper/archives/UHF-RFID_SAM-interface_Board-a9db9edc497dc1768d0f6be6ef2bac62b11ccd42.tar.gz' --strip-components=1 -C 'quarantine/aftermarket-flipper/extracted/UHF-RFID_SAM-interface_Board'

find quarantine/aftermarket-flipper/extracted -name .git -prune -exec rm -rf {} +
find quarantine/aftermarket-flipper/extracted -type d -name __MACOSX -prune -exec rm -rf {} +
find quarantine/aftermarket-flipper/extracted -type f \( -name .DS_Store -o -name '._*' -o -name '*.kicad_prl' -o -name fp-info-cache \) -delete
mkdir -p quarantine/aftermarket-flipper/derived
pdftoppm -scale-to 2000 -png papers/aftermarket-flipper/lab401-digilab-schematic-3e1e27054cdc0de4a3a8e2e2480060d2ff2afd55.pdf quarantine/aftermarket-flipper/derived/digilab
```

Extraction cleanup removed nested Git metadata, Apple filesystem detritus and local KiCad user/cache files. Original archives were not modified. A final scan found none of those paths remaining in the extracted copies, and all six original-file SHA-256 values were checked again. Documentation/link checks apply; no source/device tests were run.

Other maker/app/component sources are linked directly from the survey and were read online, without additional acquisitions. GS1's current Gen2 standard is owned by root's complementary lane, so this lane did not download a duplicate. Unavailable original FlipperMeister listing/current kit details, UCM601NC hardware documentation and current CAN Commander board/firmware evidence are recorded as unresolved in the survey for shared acquisition tracking.
