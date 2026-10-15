# Firmware frumentarii — 2026-10-15

The application-core stack is tractable to own: the source exposes reset, hardware initialization, scheduling, services, USB, application loading, and peripheral drivers. The radio core is a separate design boundary with vendor firmware, protected memory, interprocessor coordination, and device key storage. A full custom application-core system is a concrete research direction; ownership of the radio core itself is not established.

This pass read acquired official sources without running their code or touching the device. The root exploration lane independently observed the device. Source behavior below means behavior of that revision, not behavior measured on this particular unit. Archive identities, hashes, restoration commands, and license locations are in the [acquisition manifest](2026-10-15-firmware-acquisitions.md).

## Two source baselines

| Baseline | Identity | Role |
| --- | --- | --- |
| Bootstrap reference | `3fb1d51727733d2007abc5ec636a89328857803e` | Modern architecture/source map; retained from bootstrap |
| Reference matching device report | `1af022116e3d6b262289c5668a90f0fa353592c2` | Explain the observed 0.81.1 CLI and storage behavior |

The observed banner reports `dev 0.81.1 (1af02211 built on 08-04-2023)`. The [official commit lookup](https://api.github.com/repos/flipperdevices/flipperzero-firmware/commits/1af02211) resolves the abbreviated hash to the full 2023-04-08 commit above. This is an upstream correspondence for a self-reported identity, not proof that the image is unmodified or authentic. Do not use modern command inventories, storage assumptions, or application ABI expectations against this older image without checking them.

## Reset through services and applications

At the bootstrap revision, [`targets/f7/src/stm32wb55_startup.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/targets/f7/src/stm32wb55_startup.c) owns the vector table and reset handler. Reset sets the stack, resets chip clock state, copies initialized data, zeros BSS and the CPU2 mailbox buffer section, runs libc constructors, and calls `main`.

[`targets/f7/src/main.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/targets/f7/src/main.c) initializes Furi, runs early hardware setup, allocates the initialization thread, and samples boot mode/buttons before scheduling. The normal branch starts that thread; its task initializes the remaining HAL and starts services. Other branches enter DFU, update, or recovery handling. The RAM build takes a separate path that suppresses sleep and skips those boot choices.

[`furi/furi.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/furi/furi.c) starts the FreeRTOS scheduler. [`targets/f7/furi_hal/furi_hal.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/targets/f7/furi_hal/furi_hal.c) separates critical early setup from full peripheral initialization. The latter starts CPU2 glue before USB, Sub-GHz, NFC, and RFID initialization; the RAM build omits that final group. These are useful ownership seams, not isolated components we can delete blindly.

[`furi/flipper.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/furi/flipper.c) starts each `FLIPPER_SERVICES` entry as a service thread. [`scripts/fbt_tools/fbt_apps.py`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/scripts/fbt_tools/fbt_apps.py) generates these registries from application manifests. Desktop and loader are services; startup hooks are a separate generated registry executed by the loader. The kernel configuration enables preemption, static/dynamic allocation, a 1 kHz tick, and tickless idle in [`targets/f7/inc/FreeRTOSConfig.h`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/targets/f7/inc/FreeRTOSConfig.h).

[`applications/services/loader/loader.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/applications/services/loader/loader.c) creates application threads for internal apps. External apps are preloaded, checked for API/target compatibility, mapped to memory, and then given a thread. They depend on exported firmware APIs. An external app experiment explores this environment; replacing the OS and drivers requires a different execution milestone.

## Memory and boot boundaries

| Region in bootstrap linker script | Source meaning | Constraint |
| --- | --- | --- |
| Flash `0x08000000`, length 1024 KiB | Vector table and application image at flash base | Linker span includes the upper flash that CPU2 can reserve; it does not certify writable/free capacity |
| RAM1 `0x20000008`, length `0x2FFF8` | Main data/BSS/heap/stack region | First 8 bytes omitted in the flash layout |
| RAM2A `0x20030000`, 10 KiB | Mapping table and CPU2 mailbox sections, then spare pool | Not all physical SRAM2 is freely owned by M4 |
| RAM2B `0x20038000`, 10 KiB | Secondary pool start | Runtime protection boundaries also matter |

These are linker allocations from [`targets/f7/stm32wb55xx_flash.ld`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/targets/f7/stm32wb55xx_flash.ld), not a measured map of the connected unit. The RAM firmware script places code in RAM1 and uses its full 192 KiB span; that suggests a useful experiment to study, without establishing that its loading/recovery route is ready here.

[`targets/f7/furi_hal/furi_hal_flash.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/targets/f7/furi_hal/furi_hal_flash.c) computes the available upper flash boundary from `FLASH->SFR.SFSA` in 4096-byte pages. Its flash writes use 8-byte units. When CPU2 is alive, flash operations take a CPU2 mutex, use hardware semaphores, notify CPU2 of erase activity, and wait on flash coordination. A custom flash/storage driver must implement the actual coordination contract if CPU2 remains active.

[`targets/f7/furi_hal/furi_hal_memory.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/targets/f7/furi_hal/furi_hal_memory.c) derives additional SRAM2 pools from secure SRAM boundary registers. It includes a radio-stack-version-related boundary workaround. Therefore physical RAM totals and linker lengths alone are insufficient for an owned allocator design.

The matching 2023 source also places the vector/application image at flash base in [`firmware/targets/f7/stm32wb55xx_flash.ld`](https://github.com/flipperdevices/flipperzero-firmware/blob/1af022116e3d6b262289c5668a90f0fa353592c2/firmware/targets/f7/stm32wb55xx_flash.ld). Do not infer a separately preserved Flipper bootloader partition. Both versions' DFU code displays a splash, deinitializes early hardware, remaps system flash, and jumps to the ROM vector: [2023 DFU implementation](https://github.com/flipperdevices/flipperzero-firmware/blob/1af022116e3d6b262289c5668a90f0fa353592c2/firmware/targets/f7/src/dfu.c). Firmware-assisted entry therefore depends on executing functioning firmware first; the independent hardware ROM-entry procedure must be established separately.

## Read-oriented USB inventory commands

The installed-reference [`applications/services/cli/cli_commands.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/1af022116e3d6b262289c5668a90f0fa353592c2/applications/services/cli/cli_commands.c) registers these commands:

| Command | Handler behavior in installed reference |
| --- | --- |
| `help` | Lists registered commands |
| `device_info` / `!` | Device/hardware/firmware/radio properties with underscore-separated keys |
| `info device` | Same property provider, dotted keys |
| `info power` | Battery/power telemetry |
| `date` with no arguments | RTC read; arguments select a write path |
| `ps` | Runtime thread statistics |
| `free` | Heap statistics |

`uptime` and `top` exist in the bootstrap source but are absent from the observed old CLI; root confirmed that difference through `help`. `power info` is not the inventory syntax in either source. The `power` command includes state-changing operations and should not be used to guess a telemetry command.

Installed-reference [`applications/services/storage/storage_cli.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/1af022116e3d6b262289c5668a90f0fa353592c2/applications/services/storage/storage_cli.c) supports `storage info /int`, `storage info /ext`, and `storage stat /int` or `/ext` for capacity/state. `info /ext` emits SD identifying fields including its serial number. Lists and file reads disclose user contents and belong in private captures if needed later. The same storage command namespace also includes writes, deletes, formatting, and extraction; its existence is not blanket authorization to run subcommands.

The installed provider [`firmware/targets/f7/furi_hal/furi_hal_info.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/1af022116e3d6b262289c5668a90f0fa353592c2/firmware/targets/f7/furi_hal/furi_hal_info.c) includes unique identifiers and BLE address. It also checks enclave keys through crypto operations. These commands avoid persistent configuration/file writes in their handlers, but are executable telemetry operations, not passive wire observation. Raw identifiers should remain in ignored `context/`.

The old VCP backend reacts to the host's DTR bit: [`applications/services/cli/cli_vcp.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/1af022116e3d6b262289c5668a90f0fa353592c2/applications/services/cli/cli_vcp.c). In the bootstrap revision, DTR explicitly starts a shell thread and pipes it to CDC interface 0: [modern VCP backend](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/applications/services/cli/cli_vcp.c). The modern registry/pipe/shell implementation should not be projected onto the old source layout.

## Storage changed materially

The old firmware's [`applications/services/storage/storages/storage_int.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/1af022116e3d6b262289c5668a90f0fa353592c2/applications/services/storage/storages/storage_int.c) implements internal LittleFS with flash reads, programming, and erasure. Its allocation derives from free flash after the application and before the CPU2 boundary. A firmware image growing into that region changes the storage problem.

The bootstrap source instead rewrites `/int` paths to `/ext/.int` in [`applications/services/storage/storage_processing.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/applications/services/storage/storage_processing.c), and its CLI labels the internal view `Virtual`. Path processing can create the backing directory when absent. Consequently this modern source cannot certify strict read-only filesystem effects for every path operation, and modern SD/internal-storage behavior cannot describe the 2023 unit. Do not update firmware simply to make research assumptions match.

## RPC is an optional second interface

The bootstrap [`applications/services/rpc/rpc_cli.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/applications/services/rpc/rpc_cli.c) opens a USB-owned RPC session from `start_rpc_session`, locks USB configuration during it, and feeds bytes to the RPC parser. This changes the session from interactive text to binary traffic.

The pinned protocol gitlink is `flipperdevices/flipperzero-protobuf@1c84fa48919cbb71d1cc65236fc0ee36740e24c6`. Its [`flipper.proto`](https://github.com/flipperdevices/flipperzero-protobuf/blob/1c84fa48919cbb71d1cc65236fc0ee36740e24c6/flipper.proto) defines command IDs, status, continuation, and typed message bodies. [`system.proto`](https://github.com/flipperdevices/flipperzero-protobuf/blob/1c84fa48919cbb71d1cc65236fc0ee36740e24c6/system.proto) includes ping, device info, power info, date read, and protocol version, alongside mutating requests. [`storage.proto`](https://github.com/flipperdevices/flipperzero-protobuf/blob/1c84fa48919cbb71d1cc65236fc0ee36740e24c6/storage.proto) separates information, stat, list, and read from write/delete/restore. A backup-create request writes an archive to a supplied device path; it is not a read-only host download. No RPC session was started in this lane. Determine the installed protocol revision before implementing a client.

## CPU2, FUS, and the ownership decision

The bootstrap default is a vendor BLE light binary from CubeWB 1.20.0, selected by [`fbt_options.py`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/fbt_options.py). Its coprocessor gitlink is `flipperdevices/stm32wb_copro@133182d5583e998bb263cd947105be4df9c29cb3`; acquired contents include radio/FUS binaries, host-side WPAN code, and ST release notes. This is not source for a complete replaceable CPU2 firmware image.

The included [`wpan/ble_lld/README.md`](https://github.com/flipperdevices/stm32wb_copro/blob/133182d5583e998bb263cd947105be4df9c29cb3/wpan/ble_lld/README.md) describes application-core code using an IPCC proxy into private radio-core code. In that architecture, application code does not run on the radio core, and radio events incur application-core latency; action packets handle chained operations. This supplies a documented constrained radio-programming alternative. It does not demonstrate arbitrary owned CPU2 code or a replacement for all vendor services.

The bootstrap [`targets/f7/ble_glue/ble_glue.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/targets/f7/ble_glue/ble_glue.c) initializes shared transport, starts CPU2, distinguishes stack/FUS modes, and calls FUS for stack deletion/installation. A second FUS state query in one transition path deliberately restarts the MCU. These calls are not interchangeable with ordinary info reads.

[`targets/f7/furi_hal/furi_hal_crypto.c`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/targets/f7/furi_hal/furi_hal_crypto.c) stores and loads user keys through FUS calls, so the boundary also affects crypto-backed features. The source's [`scripts/flash.py`](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/scripts/flash.py) marks FUS flashing as factory-oriented and warns it erases the crypto enclave. This is a concrete preservation concern, not a reason to avoid application-core ownership.

ST's included [`firmware/Release_Notes.html`](https://github.com/flipperdevices/stm32wb_copro/blob/133182d5583e998bb263cd947105be4df9c29cb3/firmware/Release_Notes.html) explains FUS upgrade variants, anti-rollback sequencing restrictions, and Safeboot recovery after option-byte corruption. Some outcomes erase M4 firmware and the radio stack. The notes point to AN5185 and CubeProgrammer documentation; the independent hardware/recovery lane must reconcile those manuals with device-reported FUS and stack versions before any operation on CPU2/protection state.

## Consequences for design

An owned M4 system can reasonably target startup, exception handling, clocks, scheduling or event loops, allocation, drivers, USB/host protocol, storage, UI, and applications. That is a large meaningful stack even if CPU2 stays vendor-managed. Keeping CPU2 would require owned handling of shared memory, transport, clocks, semaphores, flash arbitration, and any retained key services. Omitting CPU2 radio support from an early milestone is another candidate, but power/clock/reset consequences still need study. Neither is selected here.

A first useful implementation proposal should state its flash/RAM footprint, CPU2 behavior, permitted persistent effects, host-visible success behavior, and return-to-known-image procedure. A RAM-resident or carefully bounded M4 image with a small observable interface is worth comparing after recovery is established. The comparison should precede language/runtime selection and any production dependency proposal.

## Open questions and bounded follow-up

1. Establish the connected unit's exact flash protection and SRAM boundaries without changing option bytes; current telemetry does not supply a complete address map.
2. Reconcile old internal LittleFS placement with actual backup/restore paths before replacing or growing the image.
3. Confirm hardware ROM DFU entry and SWD accessibility independently of the firmware-assisted path.
4. Trace the installed CPU2 transport/version expectations if radio or enclave support belongs in the first custom milestone.
5. Review the M4 ownership alternatives adversarially before drafting the implementation plan. This source pass is research, not that design review.

No build, flash, reset, FUS command, firmware update, dependency adoption, or radio experiment was performed by this lane. Source-path, acquisition hash, and extraction-hygiene checks support this report; source inspection cannot establish hardware recovery behavior.
