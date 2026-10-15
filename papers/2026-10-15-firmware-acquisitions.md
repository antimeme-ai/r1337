# Firmware reference acquisition manifest — 2026-10-15

Acquired for source reading only. No acquired script, binary, build, or firmware was executed. Archives remain byte-for-byte as downloaded under ignored `quarantine/firmware/archives/`; extracted references are ignored. This is reference acquisition, not dependency selection. No library or SDK has been adopted.

The bootstrap revision remains `3fb1d51727733d2007abc5ec636a89328857803e`. The connected device reports `1af02211`; the [official commit lookup](https://api.github.com/repos/flipperdevices/flipperzero-firmware/commits/1af02211) resolves it to `1af022116e3d6b262289c5668a90f0fa353592c2`, committed 2023-04-08T07:00:52Z. That association does not authenticate the running image. The short-ref archive URL below is intentionally recorded exactly as fetched; the restored short ref must still resolve to that full commit.

Submodule identity comes from the [bootstrap recursive Git tree](https://api.github.com/repos/flipperdevices/flipperzero-firmware/git/trees/3fb1d51727733d2007abc5ec636a89328857803e?recursive=1) and `.gitmodules`. Only protocol definitions and the coprocessor package were acquired; the remaining gitlinks are unpopulated. This is not a buildable recursive checkout.

## Official firmware bootstrap reference

- Source: [flipperdevices/flipperzero-firmware at 3fb1d51727733d2007abc5ec636a89328857803e](https://github.com/flipperdevices/flipperzero-firmware/tree/3fb1d51727733d2007abc5ec636a89328857803e).
- Exact archive URL: `https://codeload.github.com/flipperdevices/flipperzero-firmware/tar.gz/3fb1d51727733d2007abc5ec636a89328857803e`
- Archive: `quarantine/firmware/archives/flipperzero-firmware-3fb1d51727733d2007abc5ec636a89328857803e.tar.gz` (17389854 bytes).
- SHA-256: `7999ce227b46ef38c03e687009218f6680d10f95f57e43e4f9fed4e3561f8be1`
- Extracted destination: `quarantine/firmware/upstream/`.
- License locations within that destination: LICENSE.

```sh
mkdir -p quarantine/firmware/archives quarantine/firmware/upstream
curl -fL 'https://codeload.github.com/flipperdevices/flipperzero-firmware/tar.gz/3fb1d51727733d2007abc5ec636a89328857803e' -o quarantine/firmware/archives/flipperzero-firmware-3fb1d51727733d2007abc5ec636a89328857803e.tar.gz
tar -xzf quarantine/firmware/archives/flipperzero-firmware-3fb1d51727733d2007abc5ec636a89328857803e.tar.gz -C quarantine/firmware/upstream --strip-components=1
```

## Official firmware matching reported hash

- Source: [flipperdevices/flipperzero-firmware at 1af02211](https://github.com/flipperdevices/flipperzero-firmware/tree/1af02211).
- Exact archive URL: `https://codeload.github.com/flipperdevices/flipperzero-firmware/tar.gz/1af02211`
- Archive: `quarantine/firmware/archives/flipperzero-firmware-1af02211.tar.gz` (113122409 bytes).
- SHA-256: `54baf65ce50b29581bf07ab4da55ae4c5aa3b7198293c99096f2dcc31c8c9aa5`
- Extracted destination: `quarantine/firmware/installed-reference/`.
- License locations within that destination: LICENSE.

```sh
mkdir -p quarantine/firmware/archives quarantine/firmware/installed-reference
curl -fL 'https://codeload.github.com/flipperdevices/flipperzero-firmware/tar.gz/1af02211' -o quarantine/firmware/archives/flipperzero-firmware-1af02211.tar.gz
tar -xzf quarantine/firmware/archives/flipperzero-firmware-1af02211.tar.gz -C quarantine/firmware/installed-reference --strip-components=1
```

## Protocol definitions, bootstrap gitlink

- Source: [flipperdevices/flipperzero-protobuf at 1c84fa48919cbb71d1cc65236fc0ee36740e24c6](https://github.com/flipperdevices/flipperzero-protobuf/tree/1c84fa48919cbb71d1cc65236fc0ee36740e24c6).
- Exact archive URL: `https://codeload.github.com/flipperdevices/flipperzero-protobuf/tar.gz/1c84fa48919cbb71d1cc65236fc0ee36740e24c6`
- Archive: `quarantine/firmware/archives/flipperzero-protobuf-1c84fa48919cbb71d1cc65236fc0ee36740e24c6.tar.gz` (6451 bytes).
- SHA-256: `c89c89d5158091e5fdaac497b797354ce5f457ba96cd63862fac27145bb0ebae`
- Extracted destination: `quarantine/firmware/upstream/assets/protobuf/`.
- License locations within that destination: No LICENSE/COPYING file in acquired archive; no reuse selected.

```sh
mkdir -p quarantine/firmware/archives quarantine/firmware/upstream/assets/protobuf
curl -fL 'https://codeload.github.com/flipperdevices/flipperzero-protobuf/tar.gz/1c84fa48919cbb71d1cc65236fc0ee36740e24c6' -o quarantine/firmware/archives/flipperzero-protobuf-1c84fa48919cbb71d1cc65236fc0ee36740e24c6.tar.gz
tar -xzf quarantine/firmware/archives/flipperzero-protobuf-1c84fa48919cbb71d1cc65236fc0ee36740e24c6.tar.gz -C quarantine/firmware/upstream/assets/protobuf --strip-components=1
```

## ST coprocessor package, bootstrap gitlink

- Source: [flipperdevices/stm32wb_copro at 133182d5583e998bb263cd947105be4df9c29cb3](https://github.com/flipperdevices/stm32wb_copro/tree/133182d5583e998bb263cd947105be4df9c29cb3).
- Exact archive URL: `https://codeload.github.com/flipperdevices/stm32wb_copro/tar.gz/133182d5583e998bb263cd947105be4df9c29cb3`
- Archive: `quarantine/firmware/archives/stm32wb_copro-133182d5583e998bb263cd947105be4df9c29cb3.tar.gz` (18632215 bytes).
- SHA-256: `6e6796a380ec2f33bf92a01b824934632a44c286d871ad25434739ae0b3725c6`
- Extracted destination: `quarantine/firmware/upstream/lib/stm32wb_copro/`.
- License locations within that destination: firmware/LICENSE.md and wpan/LICENSE.md (SLA0044 Rev5); component notices also apply.

```sh
mkdir -p quarantine/firmware/archives quarantine/firmware/upstream/lib/stm32wb_copro
curl -fL 'https://codeload.github.com/flipperdevices/stm32wb_copro/tar.gz/133182d5583e998bb263cd947105be4df9c29cb3' -o quarantine/firmware/archives/stm32wb_copro-133182d5583e998bb263cd947105be4df9c29cb3.tar.gz
tar -xzf quarantine/firmware/archives/stm32wb_copro-133182d5583e998bb263cd947105be4df9c29cb3.tar.gz -C quarantine/firmware/upstream/lib/stm32wb_copro --strip-components=1
```

## Restoration order and cleanup

Restore the bootstrap firmware before populating its two submodule directories. Extract into empty destinations to avoid retaining stale files. These are restoration instructions, not instructions to build or execute the reference. GitHub may regenerate archive compression; a changed SHA-256 requires investigation and recording a new acquisition, rather than silently replacing this archive.

After extraction, remove only nested Git metadata and filesystem detritus from the extracted references, never from the preserved archives:

```sh
find quarantine/firmware/upstream quarantine/firmware/installed-reference -name .git -prune -exec rm -rf {} +
find quarantine/firmware/upstream quarantine/firmware/installed-reference -type d -name __MACOSX -prune -exec rm -rf {} +
find quarantine/firmware/upstream quarantine/firmware/installed-reference -type f \( -name .DS_Store -o -name '._*' \) -delete
```

The ingestion scan found no such metadata/detritus in these four extractions. `.gitignore`, `.gitmodules`, `.github`, and reference source documents remain as upstream source; archived agent instructions, if any, are historical reference. No license decision for porter_ricks follows from any upstream license.
