# Weird-device frumentarii — 2026-10-15

The operator added camera and basic sensors such as temperature as tertiary
objectives and explicitly requested frumentarii through the Flipper One open
development portal and unusual device projects. During the pass they offered
old iPhones for integration. Recorded both inputs without assuming models,
software versions, temperature/thermal sensing or general USB instrument access.
The primary RF/EM/debug/firmware, secondary heterogeneous lab-control, finished
core/one-companion and stash-first requirements remain in force.

Reused three parallel research agents for Flipper One, RF/EM/debug instruments
and sensing/physical/UI references. Root studied PSLab/HydraBus, sensor packaging
and Apple/Tailscale primary documentation, then read all reports and
spot-checked sources. Saved each lane's report/acquisition manifest, an iPhone
note and a cross-lane synthesis. Updated the research/quarantine indices and
current project guidance; publish the checkpoint on the existing research PR
and refresh issue #3's expanded research scope and local index.

Concrete findings: Flipper One's implemented independent MCU/control and
mechanical integration are useful patterns, while module compatibility and
portal/current-UI source drift need qualifications. Jansen's 2026 tricorder
cyberdeck is an unusually close reference and documents acquisition, cooling,
runtime and connector compromises. Source focus modes qualify its older README
but still retain a one-second sensor loop delay. Glasgow, LibreVNA, tinySA and
Husky identify distinct digital-timing, complex-network, swept-power and
event-aligned power/EM measurement classes. PSLab source shows separate capture
modes and deferred retrieval. Sensor placement, optics/lighting and calibration
context are integration inputs rather than cosmetic details.

For iPhones, current Tailscale App Store metadata requires iOS 16.6; its older
installation guide still says 15. Apple distinguishes class/accessory-specific
USB support from iPadOS DriverKit; a connector alone does not establish a generic
instrument host. Asked optionally for phone models/OS while continuing research.
No model-dependent capability was assigned without that information.

Preserved eight additional original source archives plus a pinned LibreVNA
manual and Sensirion design guide. Manifests record exact sources, hashes,
restoration, licensing locations and scope read. Root checked document links,
diff whitespace, source-byte digests, ignored corpus boundaries and extracted
detritus. Documentation-only changes need no source/device test run.

No acquired code was executed, built or installed. No device was connected,
opened, interrogated or flashed, and no remote station, tailnet route, software
dependency, hardware purchase or final architecture was selected or deployed.

## Identified iPhones

The operator identified an 11 Pro Max on 17.4.1 and a 14 Pro Max on 26.6, and
may have one or two others. They will look for an older jailbreak candidate.
Updated inventory/current discussion and the iPhone note. Read Apple exact-model
specifications and current official Dopamine/palera1n sources. Both phones use
Lightning; 14 Pro Max adds documented macro photography and LiDAR. The reported
OS versions pass the current Tailscale minimum-version threshold, without
establishing installed app/network operation.

A material current finding is that Dopamine's official site and 3.0.11 README
advertise A12/A13 support for 15.0–18.7.1, including the reported 11 Pro Max
configuration. The reported A16/26.6 configuration is outside that documented
range. Neither phone is in palera1n's A8–A11 chip range. Kept advertised support
separate from results on owned hardware and from generic USB/baseband access.
No phone operation, app install, jailbreak, exploit or downgrade was performed.
Checked document diff/whitespace; this is a documentation-only clarification.

## R8000-like service-monitor form

The operator also finds a field-optimized General Dynamics R8000 form attractive.
Added this as a third physical family alongside folding tablet and polished
cyberdeck, preserving one integrated core, at most one pocket companion and high
production values. No dimensions, weight or environmental rating is selected.
Compared front-panel controls, working posture with probes attached, carry/
transport protection and lead storage as design inputs. Hardware performance
and available interior partitioning remain separate questions.

Read the original General Dynamics R8000A brochure hosted by a distributor;
retained the unchanged PDF at `papers/form-factors/gd-r8000a-brochure.pdf`.
Source/restoration from repository root:

```sh
mkdir -p papers/form-factors
curl -fsSL https://testequipment.center/Product_Documents/General-Dynamics-R8000A-Specifications-02B81.pdf -o papers/form-factors/gd-r8000a-brochure.pdf
```

SHA-256: `5fd0a52ac83de227a1132f1bf28e51f2a90b0f35138de4845513df00823ad3ef`.
Web PDF screenshots failed with cache misses; used the installed `pdftoppm`
to view brochure front/panel pages, with working images in ignored context.
This is an interaction/form reference, not R8000 acquisition or a claim that our
instrument matches its measurements. Checked diff whitespace; no device or
implementation work.

## Synthesis and VNA-board interest

The operator likes the portable-science direction and expressed interest in
making a VNA PCB, then requested root's synthesis of the research/discussion.
Recorded that interest without deciding whether it means fabricating a reference
or designing owned hardware. Updated the cross-lane synthesis with the known
iPhones, service-monitor option and current engineering judgments. Re-read the
current LibreVNA architecture description; a web manual fetch failed, while the
previously acquired original and lane analysis remain available. No new corpus
acquisition was needed. The main synthesis concerns complementary measurement
classes, local timing versus remote analysis, interface/calibration/mechanical
work and reusable device knowledge. Checked diff whitespace; no code/device
work, dependency, purchase or build plan was introduced.
