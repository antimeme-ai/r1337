# Analog/control acquisition record

Acquired 2026-10-15 for reference study only. Original archive/PDF bytes remain
intact in ignored directories. No reference source was executed or adopted.

## PSLab firmware

- Source: `https://github.com/fossasia/pslab-firmware`
- Revision: `33b0b136b826fe30f59b177bb6f6ddf105cbcce4`
- Archive URL: `https://codeload.github.com/fossasia/pslab-firmware/tar.gz/33b0b136b826fe30f59b177bb6f6ddf105cbcce4`
- Archive: `quarantine/weird-devices/analog-control/pslab-firmware-33b0b136b826fe30f59b177bb6f6ddf105cbcce4.tar.gz`
- Size: 1,738,775 bytes.
- SHA-256: `82c63fad6a8156b37fd6bdbffb06693a1e1c5ae102694d3c5d62b66e3c32a5ca`
- Extracted directory: archive name without `.tar.gz`.
- License: root `LICENSE`, Apache-2.0.
- Unpopulated submodule: `external/cmake-microchip`; this is not a recursive,
  buildable checkout. Its `.gitmodules` declaration was read.
- Studied: README, command dispatch, oscilloscope modes/status, buffer API,
  UART defaults and local timing/counter paths. No exhaustive firmware review.

Restoration from repository root:

```sh
mkdir -p quarantine/weird-devices/analog-control
curl -fL https://codeload.github.com/fossasia/pslab-firmware/tar.gz/33b0b136b826fe30f59b177bb6f6ddf105cbcce4 -o quarantine/weird-devices/analog-control/pslab-firmware-33b0b136b826fe30f59b177bb6f6ddf105cbcce4.tar.gz
tar -xzf quarantine/weird-devices/analog-control/pslab-firmware-33b0b136b826fe30f59b177bb6f6ddf105cbcce4.tar.gz -C quarantine/weird-devices/analog-control
```

The acquisition host's Python lacks `tarfile.extractall(filter=...)`; extraction
was retried after checking every member for absolute/parent traversal paths and
requiring regular files/directories. Check extracted references for `.git`,
`.DS_Store`, `__MACOSX` and AppleDouble `._*`; remove any such detritus without
modifying the original archive. None was retained in this extracted snapshot.

## Sensirion design guide

- Title: Design Guide for Humidity and Temperature Sensors.
- Served document: Version 2, March 2024, 21 pages; the URL's filename says V1.
- Source: `https://sensirion.com/media/documents/FC5BED84/662A065D/Sensirion_Temperature_Sensors_Design_Guide_V1.pdf`
- Local: `papers/field-sensing/sensirion-design-guide-2024.pdf`
- SHA-256: `b7db78c1e8a80000411c258b9a86b2c588fbf6ee5b315cc05c728f3ab2a20662`
- Read: system versus sensor accuracy, representative placement, heat coupling,
  enclosure and response-time guidance. PDF text read via web tool; no figures
  were used as measurement evidence.

```sh
mkdir -p papers/field-sensing
curl -fL https://sensirion.com/media/documents/FC5BED84/662A065D/Sensirion_Temperature_Sensors_Design_Guide_V1.pdf -o papers/field-sensing/sensirion-design-guide-2024.pdf
```

Linked HydraBus/HydraLINCAN primary documentation was read without a local
archive. No inaccessible literature item arose in this lane.
