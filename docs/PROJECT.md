# Project brief

## Intent

The operator initiated `porter_ricks` on 2026-10-15 with two aims:

1. Explore the connected Flipper Zero deeply enough to understand and experiment
   with it as an embedded system.
2. Most probably build a full custom firmware stack.

The device is both our research subject and the eventual deployment target.
An owned stack is the likely destination. Its scope must be made concrete through
hardware and source study rather than inferred from the phrase "full custom."

## Exploration sequence

| Stage | Work | Useful result |
| --- | --- | --- |
| Establish the device baseline | Identify hardware and installed firmware; inspect documented USB/CLI/RPC interfaces; determine storage and backup options | A repeatable device inventory with knowns and unknowns |
| Understand recovery | Study reset, firmware bootloader, ROM DFU, flash layout, update flow, and available debug hardware | A device-specific recovery procedure with its observed limits |
| Map the stack | Study schematics, MCU documentation, upstream startup, drivers, scheduling, services, applications, and host tooling | A source-grounded component map and replacement options |
| Define the first custom system | Decide ownership boundaries, host/device interfaces, language, runtime, and the smallest useful hardware milestone | Reviewed design and implementation plan |
| Implement and explore | Build in conceptual units, test against explicit behavior, review, and iterate | Working owned firmware with reproducible builds and measured behavior |

These are research stages, not a selected implementation architecture. Device
exploration can continue while independent source questions are being resolved.

## Questions that determine the design

- Which layers does "full custom" replace: application firmware, OS primitives,
  board support, bootloader, update mechanism, host tooling, and radio support?
- What runs on each MCU core, which components can we own, and which vendor
  components or hardware protections constrain the boundary?
- What is the actual flash/RAM allocation, including reserved areas, shared
  memory, retained state, and recovery-related configuration?
- Which experiments benefit most from the display, buttons, storage, USB,
  GPIO, infrared, NFC, LF RFID, Sub-GHz, and Bluetooth interfaces?
- Which first milestone demonstrates useful custom execution and a repeatable
  return to a known working system?

The [research index](../papers/README.md) supplies starting sources. The
[issue index](../ISSUES.md) tracks the immediate work. No dependency or reference
implementation has been adopted, and no firmware changes occurred at bootstrap.
