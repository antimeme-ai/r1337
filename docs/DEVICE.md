# Device baseline: 2026-10-15

## Directly observed

The connected Mac's I/O Registry enumerated an active USB device with vendor
`Flipper Devices Inc.` and a Flipper product name. macOS exposed matching
`cu.usbmodemflip_*` and `tty.usbmodemflip_*` serial device nodes.

USB identifiers were vendor `0x0483` and product `0x5740`. The registry reported
a 12,000,000 bit/s USB link. These identify the observed USB interface; they do
not establish the board revision or installed firmware version.

The commands used were:

```sh
ioreg -p IOUSB -l -w 0
ls /dev/cu.* /dev/tty.*
system_profiler SPUSBDataType
```

`system_profiler SPUSBDataType` returned no text in this session. I/O Registry
and serial device enumeration supplied the positive observations. Raw captures
and unit-specific names belong in ignored `context/`.

## Still unknown

- Board revision, installed firmware family/version, and bootloader version.
- Current device health, battery state, microSD presence, and available storage.
- CLI/RPC capabilities and whether another application holds the serial port.
- Available debug probe, physical SWD access, and observed recovery behavior.
- Peripheral behavior and which capabilities matter most to our experiments.

No serial session was opened, no device files were read, and no reset, update,
flash write, or radio operation was performed during bootstrap.

## Recovery research

The vendor documents recovery through qFlipper and USB DFU. Developer
documentation distinguishes firmware-bootloader DFU from MCU ROM bootloader DFU
and describes failure conditions involving debug state and option bytes.
These are documented paths, not recovery tests performed on this unit.
Consult the [vendor recovery guide](https://docs.flipper.net/zero/basics/firmware-update/firmware-recovery)
and [developer key-combination reference](https://developer.flipper.net/flipperzero/doxygen/key_combos.html)
before designing the device-specific recovery experiment.
