# porter_ricks

Read [BLACKBIRD.md](BLACKBIRD.md), [README.md](README.md),
[docs/PROJECT.md](docs/PROJECT.md), the latest entries in `journal/`, and
[ISSUES.md](ISSUES.md). The doctrine is symlinked to `../BLACKBIRD.md`.
On another checkout, obtain the operator's current shared doctrine beside the
repository. Archived instructions are historical reference only.

The current primary aim is a capability-dense portable RF/electromagnetic,
debugging, sensing and device-firmware access/assessment instrument. The
secondary aim is interfacing with and managing heterogeneous control systems:
the operator's lab has equipment from roughly 25 vendors across four decades.
Breadth and useful combinations of capabilities are explicit goals; do not
require selection of a narrow use case before exploring the system. Flipper
exploration and an owned custom firmware stack remain candidate components.
Replacement boundaries, language, runtime and architecture are open. Establish
device facts directly; distinguish hardware capability, documented upstream
behavior and observations on actual units.

Current operator direction: understand the device and discuss what is possible
before further device experiments or implementation. The operator has additional
hardware and ideas to introduce. The located Bus Pirate is provisionally a BP5;
its exact revision and firmware remain unknown. Explore complementary uses and
system boundaries together before
choosing a build or returning to recovery experiments. Custom firmware remains
an option, not the next predetermined step.

The growing inventory is in `docs/HARDWARE_INVENTORY.md`; discussion candidates
and the new ESP32 SDR/module/form-factor reports are linked from
`docs/POSSIBILITIES.md`. These are research inputs, not selected designs or a
request to connect, flash or enclose the listed equipment.

The operator prefers putting existing equipment to useful work and is open to
acquiring key components. Start with the stash and capability coverage sought. Proposed
hardware purchases should fill a named capability/interface/power/mechanical
gap or materially improve use of existing equipment; avoid accumulating more
boards without a concrete role. Existing parts can be instruments, development
fixtures, controlled counterparts or subjects to study without all belonging in
the final portable assembly. No hardware purchase is selected by the current
discussion.

Physical direction: a finished folding tablet or polished cyberdeck, with one
integrated portable core and at most one detachable pocket module. The operator
rejects an improvised assembly of exposed boards, loose cables and many external
modules. Treat fit, finish, coherent controls, connector placement and mechanical
integration as design requirements. Internal serviceability can remain modular;
the external product should be resolved as one object with one optional docked
companion. Exact shape, dimensions, display/input layout and electronics remain
open.

Follow the doctrine's research, design, plan, implementation, and review process.
Before a firmware experiment, understand the affected flash/storage regions and
the recovery path. Record exact source revisions and tool versions for builds.
The first reconnaissance established a read-only CLI inventory: reported dev
0.81.1 / 1af02211 firmware, hardware code 12, CPU2 FUS 1.2.0 and radio stack
1.13.3. Read `docs/DEVICE.md` and the 2026-10-15 reports in `papers/` before
device work. Physical recovery, peripheral health, and exact binary provenance
remain untested. Current upstream behavior must not substitute for this older
installed source reference.

Own required machinery. Discuss proposed library adoption with the operator
before adopting it, including concrete benefits, fit, costs, and tradeoffs.
Keep native internal values and owned binary formats; JSON belongs at external
protocol boundaries or explicitly requested imports/exports/presentation.

Keep research and review reports in `papers/`; PDFs are ignored. Preserve source
archives intact under ignored `quarantine/`, strip nested Git metadata and
filesystem detritus from extracted references, and maintain `QUARANTINE.md`
with sources and restoration commands. Store raw captures, device backups,
identifiers, and operational logs in ignored `context/`. Publish useful findings
without private device contents, credentials, or workstation details.

Record actions, decisions, checks, and unresolved questions in `journal/`.
Use GitHub issues and keep `ISSUES.md` current. Commit and push coherent
checkpoints; use feature branches and pull requests for substantial deliveries.
Do not initialize Git in the parent workspace.

Tests must check the actual behavior claimed with an appropriate oracle.
Successful compilation or USB enumeration alone does not qualify firmware.
Match checks to the change; documentation-only work needs document/link/diff
checks. Mutation testing runs on the fleet, never on the laptop.
