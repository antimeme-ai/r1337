# Weird device projects: lessons for porter_ricks

Research date: 2026-10-15. Three parallel frumentarii studied Flipper One,
RF/EM/debug instruments, and sensing/physical integration. Root studied compact
analog instruments, control interfaces, sensor packaging and old-iPhone
integration, then read the lane reports and spot-checked primary sources.
Camera/basic sensing are tertiary goals; the primary RF/EM/debug/firmware and
secondary heterogeneous-control-system goals remain intact.

## The most useful references

| Reference | Concrete lesson | Relationship to this project |
| --- | --- | --- |
| Flipper One | Low-power control processor plus Linux; explicit interprocessor channels, power states and mechanical module integration | Study how a complete instrument remains operable and serviceable; published plans, source and tests have different maturity |
| Jansen's Arducorder and 2026 tricorder cyberdeck | Broad environmental/optical/magnetic sensing in a common physical and UI design | Closest new form/capability reference; current acquisition rate, cooling and runtime limits qualify impressive sensor specifications |
| Glasgow | Local programmable interface timing with host-side interpretation | Relevant to obsolete/custom interfaces in a four-decade lab; exact hardware revision/app support matters |
| LibreVNA and tinySA | Complex network measurements and swept RF power are separate observation classes | Characterize antennas/filters/cables and emissions; neither duplicates raw-I/Q capture |
| ChipWhisperer-Husky | Local triggers and clock relationships for power/EM traces | Inspect a device's physical behavior against events; acquisition frontend and time alignment are the capability |
| PSLab and HydraBus | Analog conditioning/stimulus plus explicit protocol/electrical boundaries | Investigate analog gaps and control-interface adapters before adding another generic bus board |
| tCam and OpenMV/OpenFlexure | Preserve temperature-bearing data; optics, lighting and mechanical support determine inspection usefulness | A visible image, thermal image, ambient reading and contact measurement serve distinct purposes |
| Mayhem, Sensor Watch and Beepy | Consistent local controls, observation states and power behavior | Learn how many functions can remain legible as one instrument |

Primary source links and qualifications are in the [Flipper One report](2026-10-15-flipper-one-frumentarii.md),
[instrument report](2026-10-15-weird-instruments-frumentarii.md),
[field-sensing report](2026-10-15-field-sensing-frumentarii.md) and
[analog/control report](2026-10-15-analog-control-frumentarii.md).
These are references to learn from; none is selected as a purchase or software
dependency. The unidentified stash may contain additional capabilities.

## Source reading changes the apparent capabilities

Jansen's [2026 cyberdeck](https://github.com/tricorderproject/cyberdeck)
combines visible/thermal cameras, magnetic imaging, spectroscopy and
environmental sensing in a uConsole-based prototype. Its README reports an
approximately one-frame/second integrated magnetic view despite the tile's much
faster potential. The pinned firmware contains focus modes, qualifying the
README's claim that such a mode is absent, but retains a one-second loop delay.
This is a useful example of why source and complete data paths matter. It also
documents cooling, runtime, antenna placement and connector mistakes honestly.

Flipper One has implemented MCU code and useful mechanical interfaces, but
the portal's vision pages do not by themselves establish a complete shipping
platform. In particular, internal M.2 module compatibility requires actual key,
lane, power, driver and mechanical support. The lane report records current
source/documentation drift rather than treating the portal as a frozen spec.

PSLab's inspected firmware distinguishes 10-bit multi-channel capture from
other ADC modes and handles acquisition separately from retrieval. Glasgow's
current documentation distinguishes production revC from pre-launch revD and
qualifies its analyzer support. These boundaries are more useful to our design
than combining maximum figures from several product descriptions.

## Old iPhones change the parts comparison

The operator offers old iPhones for integration. A complete phone is a candidate
camera/display/input/network client and could avoid separately integrating some
of that machinery. The operator subsequently identified an 11 Pro Max on
17.4.1 and a 14 Pro Max on 26.6, both Lightning models; battery condition and
actual app/interface behavior remain unknown.
This is not evidence for arbitrary USB instrument access or ambient/thermal
sensing. The [iPhone note](2026-10-15-iphone-integration.md) records Apple
accessory boundaries and the current Tailscale App Store requirement of iOS
16.6, which is newer than the older installation guide's requirement.

Compare an integrated phone/dock with dedicated display/camera parts and with a
phone occupying the sole removable-companion role. Neither arrangement is
selected. The instrument's acquisition controller can remain locally usable
while a phone or another display presents results and accesses remote support.

## Design hypotheses worth evaluating

1. **Separate local acquisition from presentation and remote assistance.**
   Hardware clocks, triggers, buffering and device transactions stay close to
   interfaces. A local host handles storage and the coherent UI; the remote
   support station extends reference lookup and heavier analysis. A phone is
   one possible presentation/camera component, not automatically the USB host.
2. **Design sensing geometry with the enclosure.** Camera working distance,
   illumination, probe access, antenna regions, sensor exposure, heat paths and
   connector strain relief compete for real space. A small sensor footprint
   does not imply a small complete integration cost.
3. **Compare complete operating modes.** Simultaneous radio, compute, charging,
   display and sensor operation creates different power/thermal/EM conditions
   from a quiet observation mode. Record operating state with measurements;
   measure actual self-interference before claiming field sensitivity.
4. **Store observations with their meaning.** Original samples/images, units,
   settings, sensor/probe location, time relationships and calibration context
   should survive local display and remote analysis. A common screen does not
   establish synchronized capture or equal measurement quality.
5. **Let additions fill named gaps.** Candidate gaps in currently identified
   equipment include analog acquisition/stimulus, appropriate industrial line
   interfaces, complex RF-network measurement and synchronous power/EM capture.
   First compare the unclassified modules and lab gear; a reference project
   does not automatically become a shopping item.

The next useful synthesis is a capability matrix across actual ranges,
time/data paths, probes/adapters, existing parts, integration cost and remaining
unknowns. It can explore breadth without assigning every available board to the
enclosure or narrowing the instrument to a single use case. No architecture,
firmware implementation, experiment or procurement was selected in this pass.

## Discussion after the pass

The operator finds the portable-science references appealing and is interested
in making a VNA PCB. They also accept an R8000-inspired field service-monitor
form alongside the tablet/cyberdeck. These expand the design discussion without
selecting a board, enclosure or implementation sequence.

Root's current view: the central value is complementary observations and
repeatable interaction with unfamiliar equipment. Our software could connect
images, RF/electrical traces, interface settings, manual references and reusable
device profiles. Local measurement/control, local presentation/storage and
remote support form a useful candidate separation. Exact processors remain
open. Electrical frontends, probes, calibration and physical integration appear
more discriminating than adding another generic compute board.

A VNA is particularly interesting because it could add a distinct measurement
class and help characterize the antennas, filters, cables and matching networks
used by the broader instrument. The reference design separates RF stimulus,
reference/test receive paths, local digital processing and host analysis;
calibration remains part of the measurement. Making a board could mean
fabricating a reference for study or designing owned hardware; the operator has
not selected between those. Choose intended range/quality, manufacturing and
calibration/verification approach before treating a successful PCB assembly as
an instrument milestone. This paragraph is an engineering judgment based on
the acquired corpus, not a new measured result or a selected build plan.
