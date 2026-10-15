# Recovery, host tooling, and ecosystem reconnaissance — 2026-10-15

The useful boundary is already clear: application firmware, Flipper startup/update machinery, ST ROM recovery, and Core2/FUS are separate components. Replacing the first does not require replacing the others. A full update or repair can change several of them, so it is an unsuitable inventory operation.

This is a bounded source reconnaissance, not a tested recovery procedure. This lane performed no device access, resets, firmware writes, debugger attachment, software installation, or execution of acquired code. Source archives and exact restoration commands are in [the acquisition record](2026-10-15-recovery-acquisitions.md).

## Evidence boundary and version mismatch

The inventory lane reports that this unit identifies its firmware as **dev 0.81.1**, short revision **1af02211**, with the firmware's date field **08-04-2023**. This report does not reinterpret that date string or treat self-reported firmware identity as a verified flash image. Recovery behavior, option-byte values, debugger availability, FUS state, and backup completeness remain unobserved.

The qFlipper tree read here is `1d26683ff5b751f219a4e40443b7c8355eb39469`; current upstream firmware documents were read from the separately acquired `3fb1d51727733d2007abc5ec636a89328857803e` tree. These describe newer machinery than the unit's 2023 firmware. Match its historical source before selecting RPC messages, update packages, app API versions, or debugger symbols. Current source support for legacy protocols does not prove end-to-end compatibility with this unit.

## Recovery mechanisms and concrete failure conditions

The official [key combinations guide](https://developer.flipper.net/flipperzero/doxygen/key_combos.html) documents the following distinctions. None was exercised here.

| Mechanism | Component involved | Documented limit |
| --- | --- | --- |
| LEFT + BACK held for a few seconds | Board gate asserts MCU reset | Debug circuitry can hold the reset line and defeat this reset |
| BACK held for 30 seconds with USB and external supply disconnected | Charger switches SYS power | Connected USB or external 5 V prevents this power-reset path |
| LEFT held at startup | Flipper bootloader requests DFU | Needs a present, functioning Flipper bootloader |
| OK held at startup | MCU loads ST's internal bootloader | Depends on option bytes retaining the intended boot-pin behavior |
| SWD programmer fallback | External debug interface | Needs suitable probe, electrical connection, and accessible MCU debug configuration; not established on this unit |

Firmware DFU's blue LED/screen indication is absent from documented hardware DFU. A dark display by itself therefore cannot diagnose failure. The [user recovery guide](https://docs.flipper.net/zero/basics/firmware-update/firmware-recovery) supplies qFlipper repair steps, while the developer key guide explains the deeper distinctions and exceptions. Do not conflate an app crash, a broken Flipper bootloader, damaged boot configuration, and an electrically unresponsive board.

For a later device-specific recovery trial, record the starting USB identity, exact entry sequence, resulting USB identity, entry/exit behavior, and normal-boot return. Merely seeing DFU would test entry, not prove that a known image can be restored and booted. No such trial is part of today's read-only pass.

## qFlipper is a recovery reference, with observable side effects

[Source tree](https://github.com/flipperdevices/qFlipper/tree/1d26683ff5b751f219a4e40443b7c8355eb39469).

1. **A bare qFlipper CLI invocation runs an update/repair action.** The [CLI documentation](https://github.com/flipperdevices/qFlipper/blob/1d26683ff5b751f219a4e40443b7c8355eb39469/cli/README.md) and [CLI dispatcher](https://github.com/flipperdevices/qFlipper/blob/1d26683ff5b751f219a4e40443b7c8355eb39469/cli/cli.cpp) establish this. It is not an enumeration command. Explicit help/version options are separate; the binary was not run here.
2. **Ordinary device discovery writes the clock.** [VCPDeviceInfoHelper](https://github.com/flipperdevices/qFlipper/blob/1d26683ff5b751f219a4e40443b7c8355eb39469/backend/flipperzero/helper/deviceinfohelper.cpp) starts RPC, fetches protocol/device/storage data, reads the clock, then calls `syncTime()`. That method calls `setDateTime(currentDateTime())` unconditionally. Opening the ordinary GUI to inspect the unit would not preserve a strictly read-only baseline.
3. **User backup is `/int`, not the whole device.** [UserBackupOperation](https://github.com/flipperdevices/qFlipper/blob/1d26683ff5b751f219a4e40443b7c8355eb39469/backend/flipperzero/utility/userbackupoperation.cpp) walks `/int` and reads files into a host archive. It does not image SD media, boot code, option bytes, protected Core2 contents, or the complete MCU flash. A later useful backup plan needs separate scopes and an explicit restore oracle.
4. **Full repair changes multiple components.** [FullRepairOperation](https://github.com/flipperdevices/qFlipper/blob/1d26683ff5b751f219a4e40443b7c8355eb39469/backend/flipperzero/toplevel/fullrepairoperation.cpp) fetches files, sets recovery boot mode, installs radio firmware, installs main firmware, corrects option bytes, handles assets, provisions region data, and restarts. It explicitly continues to main-firmware installation after a radio-download error. A successful later stage alone would not establish radio health.
5. **A DFU file install and a `.tgz` bundle take different paths.** [FlipperZero::installFirmware](https://github.com/flipperdevices/qFlipper/blob/1d26683ff5b751f219a4e40443b7c8355eb39469/backend/flipperzero/flipperzero.cpp) selects FullUpdateOperation for `.tgz`, otherwise FirmwareInstallOperation. The latter backs up/restores internal storage when normal firmware is available; starting in recovery skips that backup. The bundle path uploads to `/ext/update` and needs a usable SD card.
6. **FUS replacement is materially different from radio-stack replacement.** The CLI advertises distinct `core2radio` and `core2fus` commands and explicitly warns that `core2fus` invalidates the secure enclave. This is a warning in vendor source, not a behavior tested here. Do not put FUS replacement into an initial custom-M4 experiment.

The repository's normal Qt/libusb/protobuf stack is a reference to study; it has not been selected as our host dependency.

## Update packaging, option bytes, and Core2

The [OTA description](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/documentation/OTA.md) describes an SD-staged package, `/int` backup, a RAM-resident updater, optional radio replacement via proprietary FUS on Core2, option-byte checks/corrections, DFU integrity checking and programming, followed by restoration/resources. This is a host/main-firmware/updater/Core2 protocol spanning restarts, not a single flash-file copy. The RAM updater does not imply ownership of hardware-protected Core2 memory.

The manifest uses Flipper's text key-value format. Its target, loader, checksums, optional radio, resources, and option-byte masks determine operations. A minimal firmware package and a full package have different contents; inspect the generated manifest and actual payload before deciding the affected regions. Source documentation lists explicit failure stages for target/package mismatch, missing or corrupt payloads, FUS transitions, option-byte checks, flash programming/verification, and SD backup/restore. Retry support is not atomic rollback.

[Recovery::setBootMode](https://github.com/flipperdevices/qFlipper/blob/1d26683ff5b751f219a4e40443b7c8355eb39469/backend/flipperzero/recovery.cpp) writes `nBOOT0` and `nSWBOOT0`. Its radio download computes a staging address from actual `SFSA`, page size, and file size when no address is supplied. Thus remembered radio addresses or copied boot-bit settings are insufficient for this unit. The upstream [option-byte reference file](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/scripts/ob.data) is desired configuration for that source revision, not a dump of this unit.

A custom design needs explicit ownership of M4 flash, internal filesystem, reset vectors, shared/retained RAM, update staging, and all boot-related configuration it will touch. The hardware/manual lane owns detailed STM32WB protection and memory analysis; no claim here establishes that arbitrary replacement Core2 firmware is accepted or that a mass erase is recoverable without loss.

## SWD/debug paths and host interfaces

The official [developer-board guide](https://developer.flipper.net/flipperzero/doxygen/dev_board_debugging_guide.html) identifies header pin 10 as SWCLK and pin 12 as SWDIO. A probe also needs its proper electrical reference/ground and any required reset wiring; those two signal numbers alone are not a wiring plan. Direct USB-C connection to Flipper is a USB CDC/DFU transport, not evidence that an SWD probe is present.

[FBT documentation](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/documentation/fbt.md) lists the Wi-Fi Developer Board with stock Black Magic firmware, ST-Link-compatible probes, and J-Link integration. The [dedicated ST-Link V3 board](https://docs.flipper.net/zero/development/hardware/devboard-stlinkv3) adds SWD and a USB-UART connection to Flipper pins 13/14. These are supported routes to evaluate after checking what hardware is available; no purchase or tooling adoption was selected.

The Wi-Fi Developer Board supports Black Magic over Wi-Fi/USB and DAPLink over USB; its [mode documentation](https://developer.flipper.net/flipperzero/doxygen/dev_board_debug_modes.html) notes missing RTOS-thread support in Black Magic mode. Probe capabilities and firmware revisions matter. Starting an SWD debug session can halt execution; `fbt debug` additionally builds and flashes before attaching. A debugger is an experiment affecting execution, even if no flash command is intended. The target's Debug setting controls the normal firmware's SWD pin configuration; its actual state has not been read here.

Host surfaces worth tracing next:

| Surface | Source-grounded purpose | Limit for this pass |
| --- | --- | --- |
| USB CDC text CLI | Existing firmware's command dispatcher; `fbt cli` launches a serial terminal | Use only source-reviewed read commands supported by the observed historical revision |
| USB RPC | qFlipper sends `start_rpc_session`, then protobuf requests | Protocol version is negotiated; normal qFlipper discovery also sets the clock |
| Storage helper | `scripts/storage.py` includes list/read/receive and write/delete/format operations | Read the selected path first; do not run a general script as a harmless probe |
| DFU/DfuSe | qFlipper's `dfu/` library parses/programs address-bearing DFU images | Recovery transport does not by itself prove image scope or restorability |
| SWD + GDB | Memory/register inspection and code debugging through a separate probe | No probe or attachment tested; halting/flash side effects require an explicit experiment |

See pinned [serial CLI](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/scripts/serial_cli.py), [storage helper](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/scripts/storage.py), and [RPC handshake](https://github.com/flipperdevices/qFlipper/blob/1d26683ff5b751f219a4e40443b7c8355eb39469/backend/flipperzero/rpc/startrpcoperation.cpp). No helper was executed in this lane.

## Independent references: what they actually replace

All three are acquired as top-level source snapshots with licenses, commit IDs, and checksums in the acquisition record. No code, library, package, or firmware was adopted.

| Reference | Actual boundary observed in source | What it teaches us |
| --- | --- | --- |
| [Unleashed, d416e74](https://github.com/DarkFlippers/unleashed-firmware/tree/d416e74edc338849b9c817228f44280b72cf936b) | Modified upstream M4 firmware/applications; `targets/f7/target.json` links Furi, FreeRTOS, STM32WB support and existing drivers; `.gitmodules` retains the STM32WB copro repository | Changes and compatibility choices within the upstream stack; not a from-scratch scheduler/driver/Core2 replacement |
| [Momentum, d3f89df](https://github.com/Next-Flip/Momentum-Firmware/tree/d3f89dfe2ef6b01839201598e9be1590cba80322) | Modified upstream M4 system/UI/applications; same Furi/FreeRTOS/STM32WB linkage and copro reference | Broader interface/storage customization within the established architecture; not evidence of a fully owned replacement substrate |
| [flipperzero-rs, 0a6779a](https://github.com/flipperzero-rs/flipperzero-rs/tree/0a6779a49c9fca392794bf9723a7b7c10ae150e5) | Rust application/FAP bindings against existing firmware API; `crates/alloc/src/lib.rs` delegates allocation to firmware `aligned_malloc`/`aligned_free`; runtime accepts FAP entry arguments | A language/toolchain boundary experiment, not a full firmware stack. `no_std` does not mean independent of Furi or hardware initialization |

The two firmware forks' `furi/furi.c` includes FreeRTOS, corroborating the build declarations. The Rust project's current README advertises SDK 87.1 and a much newer firmware baseline than this unit. Do not assume its latest examples load on 0.81.1. No end-to-end independent bare-metal Flipper firmware was established in this bounded search; absence from these results is not proof that none exists.

## Next experiment proposal and open inputs

The next action within the current read-only scope is **historically matched source tracing**, paired with the inventory lane's conservative CLI reads. Resolve full commit `1af02211…`, inspect that tree's CLI dispatcher and storage metadata operations, then record only board/firmware/protocol/radio versions and storage capacity/status exposed by those reviewed read paths. Keep raw identity and operational responses in ignored context. If a command is absent or its implementation mutates state, record that limitation rather than probing it speculatively.

After that, design separate experiments for scoped backup/restore, recovery entry/exit, and an owned M4 milestone. Each needs a concrete oracle: archived bytes and intended restore contents for backup, USB transitions plus return to normal boot for entry/exit, and bounded target outputs plus successful restoration for custom execution. Recovery entry/exit alone will still leave actual reflash recovery unproved.

Needed inputs, rather than unavailable literature: which external SWD probe/devboard is physically available; whether historical firmware's Debug setting exposes SWD; actual option-byte/protection state if and when a debug/DFU inspection is planned; and operator intent for preserving SD/internal contents. No indispensable recovery/tooling source was inaccessible after following the correct official URLs, so this lane adds no operator document-acquisition item to SHOPPING_LIST. Broken guessed documentation URLs were superseded by the working links above.
