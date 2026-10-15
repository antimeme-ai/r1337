# Research index

Research begins with primary sources and direct device observations. This is an
initial reading map, not a completed hardware or firmware architecture study.
Keep research and independent review reports here. Acquired PDFs are ignored.

## Primary sources checked on 2026-10-15

| Source | Starting use | Status |
| --- | --- | --- |
| [Official firmware](https://github.com/flipperdevices/flipperzero-firmware) | Understand source layout and supported build/debug entry points | README reviewed; implementation study pending |
| [Pinned firmware revision](https://github.com/flipperdevices/flipperzero-firmware/tree/3fb1d51727733d2007abc5ec636a89328857803e) | Reproducible starting point for source study | `dev` resolved to this commit; no local source acquired or build run |
| [Official hardware documentation](https://docs.flipper.net/zero/development/hardware) | Locate schematics and board documentation | Entry point located; board-specific study pending |
| [Flipper Build Tool](https://developer.flipper.net/flipperzero/doxygen/fbt.html) | Understand upstream build, flash, and debug machinery | Located for follow-up |
| [Firmware recovery](https://docs.flipper.net/zero/basics/firmware-update/firmware-recovery) | Understand qFlipper and USB DFU recovery | Guide reviewed; no device recovery trial |
| [Developer key combinations](https://developer.flipper.net/flipperzero/doxygen/key_combos.html) | Distinguish reset, firmware DFU, and ROM DFU | Reviewed; hardware behavior untested here |
| [ST STM32WB55RG documentation](https://www.st.com/en/microcontrollers-microprocessors/stm32wb55rg.html) | Locate MCU datasheet and reference manuals; study core and memory boundaries | Product overview reviewed; detailed manuals pending |

The upstream firmware README describes C with some C++ and assembly, and a build
system covering build, USB flashing, and in-circuit debugging. Its source layout
separates applications, core primitives, libraries, targets, and supporting
tools. That gives us an initial map to investigate, not a selected architecture
or dependency. [Source](https://github.com/flipperdevices/flipperzero-firmware).

ST describes separate Cortex-M4 and Cortex-M0+ cores, interprocessor
communication, shared-resource coordination, and protected memory regions.
Our design question is how those boundaries affect an owned firmware stack;
this overview does not establish which radio firmware we can replace or the
configuration of our particular unit. [Source](https://www.st.com/en/microcontrollers-microprocessors/stm32wb55rg.html).

## Next reading and acquisition

1. Acquire pinned firmware source and its required reference submodules into
   quarantine, preserving archives and recording restoration commands.
2. Acquire the relevant schematics, MCU datasheet, reference manual, bootloader
   application notes, and dual-core/radio firmware documentation.
3. Trace reset through startup and application launch, then trace a small
   peripheral operation and USB command end to end.
4. Write a component map with exact source locations, observed behavior,
   unresolved constraints, and candidate experiments.

Record inaccessible sources in `SHOPPING_LIST.md` when one is actually needed.
No project library, firmware fork, or vendor SDK has been adopted.
