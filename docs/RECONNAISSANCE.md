# First reconnaissance — 2026-10-15

The device is accessible through its serial CLI. It reports development firmware
0.81.1 from a source commit dated April 2023, hardware code 12, FUS 1.2.0, radio
stack 1.13.3, 44 KiB of internal LittleFS, and a mounted approximately 29.16 GiB
FAT32 microSD filesystem. The [device inventory](DEVICE.md) distinguishes
firmware self-reports from measurements and records what remains unknown.

Three parallel frumentarii lanes acquired and studied sources while the host
lane performed metadata queries. Their reports are first-class research inputs:

- [Hardware, memory boundaries, manuals, and CPU2 research](../papers/2026-10-15-hardware-frumentarii.md)
- [Firmware startup, services, storage, CLI/RPC, and source-version comparison](../papers/2026-10-15-firmware-frumentarii.md)
- [Recovery, host-tool effects, debugging, and existing custom-firmware boundaries](../papers/2026-10-15-recovery-frumentarii.md)

## Findings that change the plan

**The installed source matters.** The banner hash corresponds to official commit
`1af022116e3d6b262289c5668a90f0fa353592c2`; this correspondence does not authenticate
the running binary. Modern command names, application APIs, and storage behavior
have changed. The historical `/int` is flash-backed LittleFS; modern source
aliases it to `/ext/.int`, with directory creation possible during path handling.
Our collector checks the historical identity before issuing the reviewed storage
queries. [Source comparison](../papers/2026-10-15-firmware-frumentarii.md).

**The application image owns the flash-base vectors.** The installed reference
links at `0x08000000`. Its firmware-assisted DFU code jumps into ST system ROM;
a separate preserved Flipper bootloader partition cannot be assumed. A custom
image needs an independently established ROM/SWD return path. Available flash
also depends on CPU2 protection and the installed filesystem; physical capacity
is not an available application budget.
[Boot and memory study](../papers/2026-10-15-firmware-frumentarii.md).

**Full CPU1 ownership is a substantial concrete option.** Startup, exceptions,
clocking, scheduler/event loop, allocator, drivers, USB protocol, storage, UI and
applications are all candidate owned components. The main unresolved contract
is what CPU2 continues to do and how CPU1 coordinates shared memory, clocks,
flash and key services with it. That boundary affects even ostensibly local
driver or storage choices. No language, runtime, or library has been selected.
[Source map](../papers/2026-10-15-firmware-frumentarii.md).

**CPU2 ownership remains open research.** ST's supported FUS route accepts
ST-signed/encrypted radio images. Cougnard's published research and ST's CPU
isolation advisory qualify any claim that this makes CPU2 execution impossible.
The reported FUS 1.2.0 makes the research relevant to investigate; it does not
establish that any method works on this unit. Execution control also does not
supply an owned radio implementation, stable boot path, or recovery procedure.
[Primary literature and limits](../papers/2026-10-15-hardware-frumentarii.md).

**Existing custom firmware mostly retains the underlying stack.** The studied
Unleashed and Momentum snapshots retain Furi/FreeRTOS and STM32WB coprocessor
support. The Rust reference provides applications using firmware APIs. These
teach useful interface and compatibility lessons; none demonstrates the whole
owned replacement we are considering.
[Reference comparison](../papers/2026-10-15-recovery-frumentarii.md).

**Host and recovery tools have effects beyond their names.** The studied
qFlipper discovery path sets the clock, its bare CLI initiates update/repair,
and its user backup covers `/int`, not SD or complete flash. Full repair can
alter radio, firmware, option bytes and assets. `fbt debug` can flash before
attaching. None of these tools was launched against the unit.
[Tooling study](../papers/2026-10-15-recovery-frumentarii.md).

## Next conceptual units

1. Fill the [schematic/manual gaps](../SHOPPING_LIST.md), reconcile the installed
   flash/SRAM/security boundaries, and identify available physical debug access.
2. Design scoped preservation and recovery experiments: distinguish internal
   files, SD contents, application image, option bytes, and provisioned CPU2 state.
   Entry/exit to ROM DFU and restoration of an image are distinct claims.
3. Compare a small owned CPU1 milestone with CPU2 retained or omitted, including
   RAM-loaded and bounded-flash execution options. State its memory footprint,
   observable behavior, persistent effects, and return-to-known-image procedure.
4. Keep deeper CPU2/radio ownership as its own research unit; do not make the
   first useful CPU1 milestone depend on resolving undocumented radio machinery
   unless that capability becomes an explicit operator priority.

These are research consequences and proposed experiments, not a reviewed product
design or implementation plan. This pass made no flash/config writes, firmware
updates, resets, debugger attachment, device file-content reads, or radio tests.
