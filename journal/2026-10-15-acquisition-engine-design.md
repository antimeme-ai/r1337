# Acquisition and interface engine design

The operator directed us to proceed after the iCE40 discussion. Continued the
authorized system-design phase: compare complete local timing/acquisition paths
before choosing silicon or preparing implementation. Asked an optional model
question about available Pis and representative lab equipment; no answer was
assumed. The breadth and selected service-monitor form remain unchanged.

## Source study and design

Read primary RP2040 chip/datasheet material, the complete pinned official PIO
logic-analyzer example, iCE40 UltraPlus resources, current iCEBreaker/Olimex maker
pages and selected existing Glasgow source. Saved the single unchanged source
file in ignored quarantine with URL/pin/hash/rights/read scope/restoration in
[papers](../papers/2026-10-15-timing-engine-study.md). Direct RP2040 original PDF
downloads returned 403 and attempted Lattice datasheets returned 404; recorded
limits and acquisition gaps without claiming full originals. No SDK/source was
built/run or installed. The old iCEBreaker hardware documentation is not evidence
that its optional FTDI FIFO wiring applies to the current V1.1b.

Wrote [ACQUISITION.md](../docs/ACQUISITION.md): existing supported firmware first,
MCU/peripheral/PIO versus iCE40 complete paths, and explicit workloads covering
bounded interface work through higher-rate digital/analog/IQ pressure cases.
Those are chosen comparison assumptions, not operator specifications or measured
performance. Payload arithmetic separates conversion/frontend, buffering and
transport. Existing BP5 is not spare MCU hardware; expected SLogic is not an
assumed reprogrammable engine. No new board or toolchain was selected.

## Adversarial reviews and integration

Reused two explicitly requested frumentarii for independent conceptual reviews:
[hardware/timebase](../papers/2026-10-15-acquisition-hardware-review.md) and
[state/output/retention](../papers/2026-10-15-acquisition-state-review.md).
Accepted all five findings and revised the contract:

- Capture phases have explicit output permissions; continuing output/transaction
  ownership is separate from capture completion and memory reservation.
- Drain blocks/status bind to operation and reset/configuration generation;
  completed data needs host-retention acknowledgment or explicit discard before
  destructive reuse. Unexpected reset reports loss/unknown availability.
- Applied configuration is separate from frontend/clock/pipeline readiness,
  with explicit validity boundaries or a recorded intended transition.
- Backpressure distinguishes uncontrolled observation, permitted protocol waits
  and timed-stimulus underrun. Correct stored counts cannot fabricate a uniform
  time axis; unknown gaps remain unknown.
- Timebase source/schedule and nominal versus measured accuracy are explicit;
  local FIFO service interruption matters alongside average throughput.

Both reviewers completed bounded rechecks and closed all five findings at this
design maturity, retaining original findings and dispositions in their reports. This refines a design contract; no general
scheduler, data format, schematic or implementation was introduced.

## Delivery and limits

Linked design, source study and reviews from the architecture, capability matrix,
README and research index. Updated the quarantine/source-gap records and #7
tracking; carry the reviewed result into the existing research PR. Current next
inputs remain actual host/interfaces and scope/generator/RF operating points,
followed by real pin, memory, bridge, frontend, power and volume budgets. No
device operation, flash, purchase, dependency adoption, remote deployment or
implementation plan occurred. Validation is direct arithmetic, local document
links/anchors, ignored-source boundary and complete staged diff whitespace;
code/device tests are inapplicable to this documentation change.

Validation passed: 239 local Markdown links, 13 anchors, workload arithmetic,
source digest/ignored boundary and doctrine symlink. Updated GitHub #7 and
rewrote PR #5 around the combined final delivery. All acquisition changes are
design/research documents; full staged diff whitespace is checked before commit.
