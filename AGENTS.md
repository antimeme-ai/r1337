# r1337

Read [BLACKBIRD.md](BLACKBIRD.md), [README.md](README.md),
[docs/PROJECT.md](docs/PROJECT.md), the latest entries in `journal/`, and
[ISSUES.md](ISSUES.md). The doctrine is symlinked to `../BLACKBIRD.md`.
On another checkout, obtain the operator's current shared doctrine beside the
repository. Archived instructions are historical reference only.

The project is now r1337, formerly porter_ricks: an homage to the General
Dynamics R8000, developed as a nomad-science field instrument. When discussing
software loadouts later, resurrect TMTSOYP as a core application. Preserve the
name verbatim; do not infer its acronym, features or implementation. This is a
future requirement, not a request to begin its implementation now.

The current primary aim is a capability-dense portable RF/electromagnetic,
debugging, sensing and device-firmware access/assessment instrument. The
secondary aim is interfacing with and managing heterogeneous control systems:
the operator's lab has equipment from roughly 25 vendors across four decades.
Breadth and useful combinations of capabilities are explicit goals; do not
require selection of a narrow use case before exploring the system. Flipper
exploration and an owned custom firmware stack remain candidate components.
Camera and basic sensors such as temperature are desirable tertiary objectives.
The operator explicitly requested a parallel frumentarii exploration of the
Flipper One open development portal and unusual device projects for ideas.
Study design patterns and actual limits; this does not select those platforms
as purchases or dependencies. Preserve primary/secondary/tertiary priorities.
Old iPhones are available for integration. Investigate complete-phone display,
camera, sensing and network-client roles without assuming a particular model,
iOS version, app compatibility or general-purpose USB instrument access.
Replacement boundaries, language, runtime and architecture are open. Establish
device facts directly; distinguish hardware capability, documented upstream
behavior and observations on actual units.

The operator proposes tailnet connectivity and a remote support station for
LLM assistance, reference-library lookup and heavier analysis. Record private
host/service details in ignored context, not public documentation. Investigate
an autonomous local instrument with remote assistance: local acquisition,
hardware timing and device operations; remote research/analysis and reusable
results. Connectivity, host services and library APIs have not been inspected
or deployed. The current phase remains discussion and design research.

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

The operator requests scope/function-generator capability, expects the SLogic32U3 logic
analyzer, and is interested in VNA/SNA and basic optical test/stimulation.
The owned Analog Discovery 3 stays outside the box as bench equipment. Ham-radio
equipment is available but unidentified; do not assign it bands or capabilities.

Physical direction for the first version is now a polished, man-portable field
service monitor inspired by the General Dynamics R8000. The operator explicitly
chooses this over pursuing a thin cyberdeck/folding tablet: useful mass/volume
are acceptable, and the result should be sleek for its instrument class. Work
within available prototyping capabilities rather than requiring difficult
miniaturization. Kirigami-inspired articulation is explicitly welcome: explore
display lift/tilt, moving port access and probe supports. Service-monitor form
does not prescribe a static rectangular enclosure. Evaluate motions by useful
working geometry, stable support, cable routing and achievable construction.
No particular folding material or linkage is selected. The earlier form comparisons
are historical research, not an active requirement to pursue all three forms.

Preserve one integrated core and at most one optional detachable pocket module.
Treat fit, finish, coherent controls, connector placement, stable working posture,
carry/transport handling and internal serviceability as design concerns. The
operator rejects exposed-board/loose-module assemblies. Exact dimensions, mass,
construction process, controls, electronics and environmental ratings remain
open; mass acceptance does not establish an unlimited weight budget.

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
