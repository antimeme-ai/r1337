# First system architecture and adversarial review

The operator directed that we proceed while they locate the thermal dongle.
Interpreted this within the current discussion/design phase: turn the accumulated
research into a first architecture and capability matrix, before powered
experiments or implementation. Read the current shared doctrine, agent guidance,
brief, inventory, possibility map, synthesis, recent journals and issue/PR state.
No additional clarification was needed to do that work.

## Proposal

Added docs/ARCHITECTURE.md and docs/CAPABILITIES.md. Proposed local acquisition
engines/frontends, a local UI/session/storage host, a minimal instrument supervisor
and remote research/analysis. Defined equipment sessions without conflating
host timestamps, native sample clocks, calibration or derived interpretations.
Candidate stash roles remain conditional: evaluate an available Pi as host, BP5
for wired control, expected SLogic for independent observation, Flipper for the
sole optional pocket role, CC1312 boards as a controlled development pair and
intact Nighthawk as backhaul. Portable scope/generator and RF network paths
remain real design gaps; AD3 stays on the bench.

Preferred a stable base with fixed test connections and an articulated display
for mockup comparison against a simple hinge. Included connector backshells,
lead force/bend space, probe posture, serviceability, thermal/sensor placement
and one-core/one-companion limits. No board, linkage, dimension, power pack,
performance target, software loadout, dependency or purchase was selected.
TMTSOYP remains a future core-app requirement for its later discussion.

## Parallel review and disposition

Reused the three frumentarii for independent reviews of software/action
boundaries, measurement feasibility and physical/power/human integration.
Each wrote a papers/ report; root read all findings and revised the design.
All initial findings are accepted at the architecture level:

- Give each local operation ownership of its affected configuration/actions;
  bind it to actual applied settings and equipment context, invalidating stale
  prepared work on reset, disconnect or unaccounted change.
- Require per-engine output behavior and an actual enforcing/status path through
  host/link loss, standby, shutdown, low energy and restart. A supervisor cannot
  implicitly control an engine with no corresponding physical path.
- Distinguish complete, incomplete/gapped and unknown captures. Retain available
  sequence/clock/context, report overflow/storage failures and acknowledge actual
  recording state rather than merely requested recording.
- Preserve unknown action outcomes without silent repeat or dependent assumptions;
  permit documented diagnostic/stop/recovery actions valid under that uncertainty.
- Compose charger, battery, USB/hub, target, dock and chassis power/return domains.
  Preserve required cooling during qualified observation modes and expose mode
  changes. Carry measurement reference planes and servicing/calibration effects
  into physical design.
- Separate raw I/Q access from spectrum-measurement requirements.

Each reviewer re-read the revised sections and appended a disposition closing
its findings at first-architecture maturity. This reviews a proposal, not actual
hardware or finished specifications. Detailed measurement requirements, block
schematics and populated motion/volume studies precede a reviewed prototype plan.
No additional implementation plan or code was produced in this phase.

## Tracking and related clarification

Opened issue #7 for detailed service-monitor system design. Updated the local
index, README, project/agent guidance, possibility and research indices. Corrected
issue #3's stale folding-tablet/cyberdeck direction to the selected service monitor.
Updated the existing research PR to describe its final research/design scope.

Recorded the preceding GPR explanation in the enclosure-sensing report, with
USGS, Sensors & Software and FHWA sources read for that answer. Reflection delay
and material properties explain buried-target detection; it does not establish
imaging behind a continuous metal panel. No radar subsystem or new source
archive was selected. Thermal-dongle identification remains open.

## Validation

Documentation-only checks passed for 173 local Markdown links, 11 anchors,
the shared-doctrine symlink and ignored context working files. Diff whitespace
was checked before staging and is checked again on the complete staged change. No
source tests apply; no collector, device, firmware, radio stimulus, remote
service or reference implementation was run. Commit and push a coherent
checkpoint on the existing research branch and retain PR #5 for review.
