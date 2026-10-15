# Project brief

## Intent

The operator initiated `porter_ricks` on 2026-10-15 with two aims:

1. Explore the connected Flipper Zero deeply enough to understand and experiment
   with it as an embedded system.
2. Most probably build a full custom firmware stack.

The operator has since clarified the broader goal: maximize useful capability
across RF, electromagnetic sensing, debugging, sensing and firmware access and
assessment of varied devices in a portable, finished instrument. Capability
breadth is itself a design objective; a narrow application is not a prerequisite
for exploring the design. Flipper remains a research subject and candidate
component; it is no longer assumed to be the sole deployment target. Owned
firmware is a means of enabling the instrument, with its scope still open.

A secondary focus is interfacing with and managing heterogeneous control
systems. The operator's lab contains equipment from approximately 25 vendors
spanning four decades. The system should support investigating unfamiliar
equipment and making understood equipment useful together. Exact models,
interfaces and supported operations have not yet been identified.

A camera and basic sensors, including temperature, are desirable tertiary
objectives. Investigate their use for equipment identification, inspection,
measurement context and field observations. Distinguish ambient temperature,
contact target temperature, thermal imaging and internal device temperature;
these require different sensor paths. Optical focus, lighting, sensor placement
and measurement metadata are integration concerns. No camera, thermal imager or
sensor suite has been selected or assumed present in the stash.

The operator also offers old iPhones for integration. Compare reusing a complete
phone for camera/display/input and network access with dedicated parts, keeping
the finished core/one-companion requirement. Models, OS versions and battery
condition are unknown. No generic USB driver support, thermal camera, ambient
temperature sensor or specific network/app support is inferred.

The operator requested parallel research through the Flipper One open
development portal and other unusual device projects. Study their actual
hardware/software boundaries, physical integration and useful combinations of
capabilities; record published plans and prototype claims separately from
demonstrated or inspected implementations.

Compare capability coverage with the space, power, thermal, RF-interference,
data-path and integration costs. Count usable observations and operations,
including their supported ranges and limits, rather than installed board count.

For control systems, distinguish electrical adaptation, protocol transport,
device command semantics and coordinated operation. A shared connector or bus
does not establish interchangeable behavior. Investigate persistent lab-side
adapters/gateways as an architectural option alongside the portable core;
multiple external modules carried with the instrument remain outside the
physical brief. No gateway, protocol stack or management architecture is
selected.

## Remote support

The operator proposes putting the portable instrument on the tailnet and
providing a remote support station with LLM access, a reference library and
compute/storage that need not be carried. Model identifiers, label/board
images, selected signal captures and device transcripts are candidate inputs;
manual references, analysis, candidate identifications and suggested next
measurements are candidate outputs. The named host/library details are retained
in ignored context. Their interfaces and availability remain uninspected.

Investigate a split in which capture, triggering, local display, buffering and
time-sensitive device operations work locally. Remote assistance extends
research and analysis. Bounded captures and selected windows can use much less
bandwidth than continuous raw streams; actual transfer budgets depend on the
sample representation, channel count, rate and duration. Preserve the original
data and capture metadata so remote interpretation can be checked.

Connection loss should leave local instruments usable, retain pending captures
and allow interrupted transfers to resume. Remote suggestions need their
supporting sources and uncertainty attached. Separate analysis retries from
commands that change device state; reconnecting must not silently repeat a
control or firmware operation. This is design direction, not a selected
transport, job protocol, LLM stack or deployment.

## Current discussion

Following the first reconnaissance, the operator directed that we understand
the device and think through possibilities before further experiments or
implementation. Additional equipment and ideas will shape this discussion;
the operator located a likely Bus Pirate 5, with exact revision and firmware
still to be established.

The operator has since found additional boards and is interested in a new
portable form factor, CAD possibilities, and recent ESP32 SDR work. The
[growing inventory](HARDWARE_INVENTORY.md) and
[possibility map](POSSIBILITIES.md) preserve this expanding scope. The project
may involve several instruments or independently placed nodes; Flipper firmware
ownership remains one possible component of that discussion.

The operator prefers using the existing stash and is open to acquiring key
components. Let known hardware and desired experiences shape the design.
Identify a concrete missing capability or integration need before proposing
another acquisition. A part can earn its role in the portable instrument, on
the development bench, as a test counterpart, or as a subject to understand.
Using the stash does not require enclosing every available board.

Investigate the Flipper as an instrument in a larger set of tools: its own
capabilities and limits, overlap and complementary roles, useful joint
experiments, interfaces between instruments, and what custom firmware would
enable. Evaluate host-coordinated instruments and direct coupling as distinct
system choices. No physical pairing or firmware architecture is selected.

## Physical direction

The operator can see a folding tablet or a cyberdeck with high production
values. The core should be portable, visually coherent and reasonably ordinary
to carry. One detachable pocket module is acceptable; a collection of exposed
modules and improvised external cabling is outside the desired form.

This narrows the earlier physical possibilities to an integrated product with
one optional companion. Internal carriers and serviceable electronics can still
be modular. Hinges, retention, cable routing, ports, antenna placement, controls,
materials and finish must be designed together with the electronic layout.
The exact enclosure, display/keyboard arrangement, size and pocket-module role
are still discussion questions. The broader stash can support development and
test subjects without appearing on the outside of the finished instrument.

## Exploration sequence

| Stage | Work | Useful result |
| --- | --- | --- |
| Establish the device baseline | Identify hardware and installed firmware; inspect documented USB/CLI/RPC interfaces; determine storage and backup options | A repeatable device inventory with knowns and unknowns |
| Understand recovery | Study reset, firmware bootloader, ROM DFU, flash layout, update flow, and available debug hardware | A device-specific recovery procedure with its observed limits |
| Map the stack | Study schematics, MCU documentation, upstream startup, drivers, scheduling, services, applications, and host tooling | A source-grounded component map and replacement options |
| Define the first custom system | Decide ownership boundaries, host/device interfaces, language, runtime, and the smallest useful hardware milestone | Reviewed design and implementation plan |
| Implement and explore | Build in conceptual units, test against explicit behavior, review, and iterate | Working owned firmware with reproducible builds and measured behavior |

These are possible research stages, not the current execution queue or a
selected implementation architecture. The understanding/discussion phase above
currently precedes further device experiments.

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
