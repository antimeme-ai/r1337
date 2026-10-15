# Architecture review: physical integration, power and human use

Reviewed 2026-10-15: [ARCHITECTURE.md](../docs/ARCHITECTURE.md) and [CAPABILITIES.md](../docs/CAPABILITIES.md), with current instructions, project brief, inventory, operator decisions in the journal, and the power, analog/control, BP5, iPhone, enclosure-sensing and instrument-reference reports. This is one adversarial review of the proposed architecture. No equipment operation, implementation, CAD or procurement occurred.

The proposal respects the chosen service-monitor form, articulated display, stash-first evaluation, one core/at most one companion, local narration and bench-only AD3. The stable base with fixed test leads is a sensible hypothesis to mock up. The findings below concern system boundaries that can invalidate a physically neat assembly; none requires finished CAD or selecting a new part now.

Severity: **P1** needs resolution before approving a powered prototype plan because its failure can change the connected equipment or defeat the instrument's electrical boundary. **P2** should enter the next architecture revision and its prototype questions. These are design omissions, not claims that an existing build has failed.

## P1 — System ground and source domains are delegated to frontends but not composed

**Sections:** Architecture *Functional boundaries*, *Physical architecture*, *Power, noise and operating modes*; capability rows for scope, waveform stimulus, power/EM behavior and industrial control.

The frontend boundary names grounding/isolation, and the diagram correctly disclaims a shared ground. However, the integration proposal does not require a system view showing which grounds and power sources become joined through internal USB, connector shields, mounting hardware, charging, target power and the companion dock. Correct individual frontend descriptions are insufficient once those assemblies share a host and enclosure.

**Practical failure:** in a plausible configuration, a grounded target, USB instrument and externally powered/charging host acquire a return path through instrument grounds. A frontend intended to float or isolate can then be bypassed by another connection. Alternatively, a powered target or self-powered internal board can energize an otherwise disabled rail through a signal/power path. These are conditional circuit consequences, not observations on the stash. BP5's documented VOUT/VREF behavior and USB power path make this a concrete integration question, particularly alongside analog/industrial interfaces. [BP5 source report](2026-10-15-bus-pirate5-possibilities.md), [analog-interface report](2026-10-15-analog-control-frumentarii.md).

**Proposed resolution:** add an explicit system constraint: every target-facing interface belongs to a documented electrical/power domain, with intended returns and source/sink paths understood across battery operation, external power/charging, docked devices and supported combinations of connected targets. Unknown domains remain design gaps. A first block diagram can use candidate domains and unresolved crossings; it need not select an isolator, charger or connector. Subsequent electrical work should demonstrate that chosen isolation/protection is not bypassed by host, shield or chassis connections and that disabled branches are not powered unintentionally.

## P1 — Power/control ownership has no defined target-facing state during failures and transitions

**Sections:** Architecture *Functional boundaries*, *Power, noise and operating modes*, *Heterogeneous control systems*; capability rows for electrical stimulus, BP5 and control interfaces.

The supervisor owns buttons, power sequencing and host shutdown, while independent engines execute waveforms and target transactions. The design says which block configures an operation but not which block owns the physical output state if the host stalls, the control link disappears, standby is requested, or power falls below the usable operating range. The remote-operation “outcome unknown” rule addresses reconnection semantics; it does not define what a still-powered generator or target supply is doing electrically.

**Practical failure:** the UI/host goes away while a local engine continues its last waveform, target power or driven bus state. Conversely, a supervisor removes a branch during a firmware operation that needs continuity, or a reboot restores an old output setting before the operator sees the current state. “Retain useful state” in standby cannot decide among those behaviors. No such behavior is asserted about actual BP5 or another owned device; the proposed integrated system has not assigned it.

**Proposed resolution:** require each output-capable engine to declare its behavior for start, normal stop, operator abort, lost host/control link, standby, low energy and power restoration. Some operations may deliberately continue independently; others need a bounded stop or an explicit hold/disconnect state. Do not assume that unpowered means electrically disconnected or that clearing software state removes a driven output. Give the supervisor/engine boundary the minimum control and status necessary to enforce the chosen policy, with visible output/target-power status when those can outlive the host UI. Keep routine narration/capture controls distinct from target abort. Specific watchdogs, switches and shutdown hardware remain later design choices.

## P2 — Quiet observation is not yet reconciled with cooling and host independence

**Sections:** Architecture *Power, noise and operating modes* and *Physical architecture*; capability rows for raw RF, power/EM behavior, environmental readings and narration.

The mode table appropriately names fans, radios, converters and display activity as possible interferers, but cooling has no explicit operating contract. Compute/power/communications are proposed together; intact backhaul and a possible embedded phone add independent loads. The architecture needs to say what remains usable when an acceptable observation state requires changing those loads, and what happens when the thermal condition no longer permits that state.

**Practical failure:** a short noise check passes with fans/radios quiet, but a longer local capture/storage session heats the assembly and forces a fan, throttling or a mode change. A changing interferer can spoil comparisons or the display can continue to imply the earlier quiet configuration. A fan/exhaust location can also undermine ambient sensing or PTT audio. The reference corpus already contains an integrated cyberdeck whose sensor breadth exceeded its cooling/runtime provision. [Reference synthesis](2026-10-15-weird-devices-synthesis.md), [sensor-packaging discussion](2026-10-15-analog-control-frumentarii.md).

**Proposed resolution:** make an operating mode a qualified combination of acquisition, host load, backhaul/display state and required cooling, with an explicit indication when it changes. Quiet operation may mean reduced compute, deferred upload, a bounded capture interval or another measured arrangement; it must preserve necessary thermal control. Add sustained acquisition-plus-storage, charging-plus-operation, and sensitive-observation thermal/noise behavior to the forthcoming architecture/prototype questions. Reserve deliberate heat/exhaust paths and sensor/microphone locations in volume studies. No temperature, runtime or fan specification is required in this first revision.

## P2 — Serviceable packaging needs an explicit measurement reference plane

**Sections:** Architecture *Capability coverage*, *Physical architecture*, *Timing, storage and remote support*; capability rows for scope/AWG and VNA/SNA.

Short connector paths, removable carriers and calibration context are named, but the architecture does not state where the integrated analog/RF instrument's measurement boundary lies. A bare instrument board's original connector, a front-panel bulkhead, a moving connector assembly and the far end of a target lead are different candidate planes.

**Practical failure:** a source/receiver is characterized on the bench, then an internal pigtail, relay, adapter or front-panel extension changes the path. A saved calibration can still be selected even though servicing a carrier or rearranging a harness changed that path. Screen articulation is especially worth keeping separate from sensitive signal paths; moving only the screen is already a useful preference. The RF report explicitly identifies fixture/cable reference planes as part of the instrument. [RF/instrument report](2026-10-15-weird-instruments-frumentarii.md).

**Proposed resolution:** adopt the constraint that integrated measurement/stimulus paths have a named reference plane, with internal routing treated as part of that path. Define what servicing, replacement or reconfiguration requires recharacterization or a different calibration record. The exact plane and method remain open until frontends/ranges are chosen. Use early connector/harness studies to preserve strain relief, repeatable mating and access to required calibration fixtures; no final connector panel or numerical accuracy target is demanded now.

## Human-use and form observations that do not merit additional findings

The draft already requests plug/backshell clearance, lead bends, screen cables, tip-over checks, handle clearance and service access. Those cover the correct first motion/volume studies; the absence of a selected linkage or dimensioned mechanism is appropriate. Compare the proposed lift/tilt with the simpler hinge using the same populated working configuration, including a connected stiff lead and a supported base, rather than judging empty-shell motion alone.

The PTT provision already includes occupied-hand reach, fan/handling noise and an indicator tied to actual recording. Retain those requirements. A useful mockup should include the display at its working angle, grip/support and a real probe posture; assess whether narration can be started/stopped without losing the measurement position. This is a direct ergonomic question, not a request for another carried controller. Likewise, phone photography and a Flipper pocket role must compete within the existing core/one-companion rule; the architecture already states that correctly.

AD3 remains bench equipment. The unresolved portable scope/generator and VNA functions are honest capability gaps deserving frontend, power and mechanical study; their absence is not repaired by putting AD3 into the box. The expected SLogic outline and unknown parts can retain allowances until identified. The review does not require eliminating breadth, finishing CAD, selecting every capability's hardware or reopening the operator's chosen form.

## Disposition

Resolve the two P1 boundaries in the architecture, then carry the thermal/mode and reference-plane constraints into block schematics and motion/volume studies. The overall local-host/local-engine/remote-support split remains viable as a proposal. No additional research duplication, purchase, device experiment or implementation is necessary to make these architectural responsibilities explicit.

## Revision disposition — 2026-10-15

Re-read the revised architecture and capability matrix against these four findings. **All four are resolved at first-architecture maturity.** The original findings above remain the review record.

- **Ground/source domains — resolved:** *Power, noise and operating modes* now requires the composed battery/charger/USB/instrument/target/dock/chassis return-path map, assigns electrical/power domains and names isolation, common-mode and backfeed decisions. The actual map and electrical qualification remain subsequent design work.
- **Output states — resolved:** the same section now requires operation-specific loss, cancellation, shutdown, low-energy and restart behavior, identifies independent enforcement/status needs, and distinguishes operator stop from power-off. It explicitly avoids implying that the supervisor can stop an engine without a control path. Concrete engines must later implement and demonstrate those policies.
- **Cooling/noise modes — resolved:** sensitive observation must preserve required cooling, report actual state/mode changes, account for settling and qualify sustained recording and charging workloads. Heat/exhaust, microphone and ambient-sensor placement are explicit integration inputs.
- **Measurement reference plane — resolved:** *Physical architecture* now includes internal pigtails/switches/protection/panel connectors in the measurement path and requires calibration invalidation or recharacterization when servicing changes it.

The capability matrix explicitly carries these cross-cutting contracts across its rows. No outstanding finding from this physical review blocks proceeding to the next design studies. This disposition approves the architectural responsibilities at the stated maturity; it does not establish electrical isolation, thermal performance, calibration quality or working failure behavior on hardware.
