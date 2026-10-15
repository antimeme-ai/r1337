# Device baseline: 2026-10-15

## Direct observations

The Mac enumerates a working Flipper USB interface: vendor `Flipper Devices
Inc.`, VID `0x0483`, PID `0x5740`, 12 Mbps link, and matching
`cu.usbmodemflip_*` / `tty.usbmodemflip_*` serial nodes. No process held these
nodes at the initial `lsof` check. The serial CLI responded to its documented
metadata queries and returned complete prompts.

These are firmware-reported values, not an independent board inspection or
firmware-authenticity check:

| Item | Observed value |
| --- | --- |
| Firmware | `dev 0.81.1`, commit `1af02211`, reports clean tree |
| Build-date string | `08-04-2023` |
| Hardware codes | version `12`, target `7`, body `9`, connect `6`, display `1`, OTP `2` |
| CPU2 state | radio alive, mode `Stack` |
| FUS version | `1.2.0` |
| Radio-stack version | `1.13.3`, type `3`, branch `0`, release `2` |
| Reported CPU2 memory | stack flash `120K`, SRAM2b `19K`, SRAM2a `14K`; FUS flash `24K`, SRAM2b `16K` |
| RPC schema version | protobuf `0.15` |
| Internal filesystem | LittleFS, `44 KiB` total, `20 KiB` free |
| External filesystem | FAT32, `30,574,592 KiB` total, `30,533,120 KiB` free; approximately `29.16 GiB` total |
| Battery snapshot | charge level `100`, state `charged`, reported health `100` |
| Application heap snapshot | `182,616` bytes total; `135,392` bytes free in the initial query |
| Thread snapshot | `19` threads, including CLI, USB, storage, power, desktop, GUI, NFC IRQ and Bluetooth workers |

Charge, free memory, filesystem space, and thread counts are snapshots. These
queries do not measure battery health independently or establish peripheral
functionality. The `ps` heap column printed `4294967295` for every thread; it
must not be interpreted as actual per-thread allocations. The device clock was
read and left unchanged; its timezone interpretation was not established.

The banner hash resolves in the official repository to
[`1af022116e3d6b262289c5668a90f0fa353592c2`](https://github.com/flipperdevices/flipperzero-firmware/commit/1af022116e3d6b262289c5668a90f0fa353592c2),
committed 2023-04-08. This identifies a matching source reference; it does not
prove that the installed binary is identical to that reference.

## Repeat the inventory

Host USB checks:

```sh
ioreg -p IOUSB -l -w 0
ls /dev/cu.* /dev/tty.*
```

`system_profiler SPUSBDataType` returned no text in the bootstrap session.
The I/O Registry and serial-node enumeration supplied the positive observations.

Check that no other program holds the selected serial device, then run the
host-only standard-library collector from the repository root:

```sh
lsof /dev/cu.usbmodemflip_*
python3 scripts/flipper_inventory.py
```

The collector finds exactly one Flipper callout port, asserts CDC DTR, waits
for the CLI banner/prompt, and sends this fixed sequence. Before configuring
the port it checks native `lsof` output for an existing owner of either serial
alias. It stops after identity reads unless the reported clean firmware matches
the source-reviewed `0.81.1` / `1af02211` profile; modern storage code can have
different effects. It restores serial attributes and the observed DTR bit and
releases its exclusivity flag on exit.

```text
help
device_info
info power
storage info /int
storage info /ext
free
date
```

It captures exact response bytes into a new ignored `context/inventory-*`
directory. Use `--port` to select a device and `--output` to choose a new capture
directory. Captures include device/card identifiers: keep them private. Initial
exploration additionally ran the source-inspected, read-only `ps` command.
The collector performs no device file-content reads or radio operations.

## Remaining unknowns

- Physical board/silkscreen identity and electrical peripheral health.
- Available physical SWD probe/access and an observed recovery/reinstallation path.
- Device file contents and backup completeness; only storage metadata was read.
- Exact installed binary provenance and compatibility with modern host/update tools.
- CPU2 replacement behavior on this unit; reported FUS/stack state is not a test.

No reset, firmware installation, flash/config write, radio experiment, or
qFlipper launch occurred. Recovery findings and the version-specific source map
are recorded in the research reports. The recovery issue remains open.
