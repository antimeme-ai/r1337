# Portable instruments: first possibilities

This is a discussion map for the operator's growing parts inventory. It does
not select a device, firmware stack, enclosure, protocol, or implementation
sequence. The [hardware inventory](HARDWARE_INVENTORY.md) distinguishes parts
found by the operator from hardware actually inspected by this project.

## Capabilities emerging from the inventory

| Candidate resource | What it contributes to investigate | Important distinction |
| --- | --- | --- |
| Flipper Zero | Battery, physical controls, display, storage, IR/NFC/LF RFID/Sub-GHz and exposed interfaces | Existing physical interfaces and an owned full firmware stack are separate scope choices |
| Freenove classic ESP32-WROVER | A programmable wireless/peripheral companion; newly exposed raw-radio capture is worth studying | Classic ESP32 support does not confer S3/S31 streaming features; fitted board peripherals remain unknown |
| Flipper Wi-Fi module v1 | A candidate ESP32-S2 platform and especially useful debugging instrument | Identify the physical module and installed image; an SDR role and a debugger role need explicit firmware choices |
| CC1312R1 LaunchPad | An independent programmable sub-GHz endpoint with its own application processor | Raw packets, demodulated timings and RSSI differ from raw I/Q; fitted RF network matters |
| Raspberry Pis | Possible local host, analysis, storage and richer display | Model determines connectivity, size, load, cooling and usable interfaces |
| Bus Pirate 5, working identification | Wired protocol control, buffered IO, voltage/current context and target-power functions | Revision/firmware affect output ratings, capture topology and automation interfaces |
| Nighthawk M6 MR6150 | Candidate independent cellular backhaul, with Wi-Fi/Ethernet/tethering roles | Regional SKU, actual power behavior and available management interfaces remain unverified |
| Pineapple Mark VII and MK7AC | An independent network computer and dual-band USB packet interface | USB host/device roles, channel allocation, driver compatibility and capture loss matter |
| Bash Bunny and candidate O.MG Plug | Programmable USB test counterparts for identified laboratory hosts | Exact generation/tier and present configuration remain unknown; these are active devices |
| Nighthawk pack and FPV batteries | Candidate energy stores for different mechanical arrangements | Pack voltage/energy labels do not establish regulated rails, charging or connector requirements |
| Industrial/network units and cable collection | Subjects to study, known test counterparts, and possible adapters/infrastructure | Identify each model, electrical interface and pinout before assigning a role |
| Xilo controller and other modules | Further compute, sensing or interface options | Wait for actual identification before assigning capabilities |

The [module research](../papers/2026-10-15-radio-module-possibilities.md)
grounds the identified platforms in manufacturer documentation. These are
candidate roles. No board must be included merely because it is available.

The later inventory supports a broader combination of physical-interface,
network, radio and USB instruments. Useful common machinery might record which
subject, interface, instrument configuration, trigger and observation produced
each result. That is a candidate ownership boundary worth comparing with
replacing individual device firmware.

New primary-source reports cover [Bus Pirate 5](../papers/2026-10-15-bus-pirate5-possibilities.md),
[network/USB platforms](../papers/2026-10-15-network-usb-instrument-possibilities.md),
and [MR6150/power](../papers/2026-10-15-mr6150-power-possibilities.md).
The BP5 already has its own color electrical-status display, so Flipper need
not automatically own every user interaction. The Nighthawk can be useful as
an intact network appliance independently of any battery-reuse proposal.

## The ESP32 SDR opening

The current ESP-SDR work exposes raw complex receiver samples from an
undocumented internal radio path. Original ESP32 support makes the classic
WROVER a plausible research target. A raw-radio receiver opens spectrum,
waveform and software-demodulation experiments beyond normal packet APIs.

For a portable design, distinguish five independent properties: tuning range,
analog bandwidth, internal capture rate, sustained output rate, and capture duty
cycle. Shared firmware or several similar boards does not establish coherent
multi-antenna reception. Wi-Fi uplink concurrent with raw-radio capture also
needs actual support; the same on-chip receiver cannot be treated as an
independent networking instrument by assumption.

The original ESP32 path is presently a short-snapshot candidate. The much faster
S3/S31 examples use different silicon, transports and sometimes substantial
external hardware. The [SDR report](../papers/2026-10-15-esp32-sdr-reconnaissance.md)
records precise source baselines, sample/export constraints and what has not
been reproduced. No ESP board was flashed or tested in this discussion pass.

## Router internals and a wider SDR possibility

The later router investigation is recorded in
[MR6150 internals](../papers/2026-10-15-mr6150-internals.md) and
[Wi-Fi 7 SDR reconnaissance](../papers/2026-10-15-wifi7-sdr-reconnaissance.md).
The Nighthawk's documented X62/Wi-Fi 6 platform and the Gemtek/MediaTek Wi-Fi 7
SDR project are distinct hardware/access paths. No raw-I/Q capability has been
established on the operator's MR6150.

The W1700K SDR author reports replacement MT7996 firmware, raw complex sampling
at up to 320 MS/s, and sustained export over 10 GbE. That suggests a materially
different instrument option from the short snapshots of classic ESP32: a wide
instantaneous RF view in the supported bands. It also changes the processing,
memory, storage and transport budget. The author has not established calibrated
dBm levels or completed all long-run work; a 14-bit sample representation alone
does not specify effective resolution or instrument accuracy.

This is a capability lead, not a proposed purchase or a claim of compatibility
with arbitrary Wi-Fi 7 routers. Identify the networking stash before considering
a new receiver. Any future radio subsystem still needs to fit the integrated
core/one-companion form and the actual observation being sought.

## Experiences worth comparing

| Possible instrument | Example experience | What would make it useful |
| --- | --- | --- |
| Signal notebook | Examine activity, save selected observations, attach notes, and revisit the same place or object | Clear scope of observation, honest capture gaps, useful local display and storage |
| Controlled experiment station | Send a known IR/radio stimulus and observe a target's wired or sensor response | Independent stimulus/observation paths and a defined trigger/time relationship |
| Core with one pocket companion | Leave the companion beside a subject or carry it separately and inspect results on the core | A defined companion role, local autonomy, link behavior and a finished dock |
| Integrated interface instrument | Select the appropriate built-in interface for the job and attach its target lead | Consolidated ports, useful labeling, stored leads and reusable procedures |
| Equipment identification workbench | Build a documented understanding of a controller's connectors, signaling and observable behavior | Model/pinout identification, suitable interface electronics, probes and reproducible notes |
| Controlled network/USB laboratory | Compare an owned host or network device's response to known supported endpoints | Deliberate device roles, known configurations and independent observations |

These are use proposals, not claims that the current boards already perform
the complete experience. A Bus Pirate might improve the wired observation
part; a Pi might improve analysis and storage; a CC1312R node might move an
observation away from the user's hands. The desired experience should decide
whether each addition earns its power, space and integration cost.

The industrial-control and networking bins could make these experiences
concrete. Cable variety is valuable once each cable's purpose is known;
connector shape alone does not establish RS-232, RS-485, CAN, logic-level serial,
USB data roles or power. Appropriate interface electronics remain a separate
design question. No current target's protocol or voltage has been inferred.

## Physical forms and what CAD can contribute

The operator has narrowed the earlier options: a finished folding tablet or
polished cyberdeck, with one integrated portable core and at most one detachable
pocket module. Visual/mechanical integration is part of the product brief.
Historical research comparing many probes, packs and nodes remains useful
reference; it does not define the desired external form.

| Candidate | Character to investigate | Open decisions |
| --- | --- | --- |
| Folding tablet | A compact closed object that opens into a larger working interface | Display arrangement, input method, hinge and supported working positions |
| Refined clamshell cyberdeck | A deliberate portable instrument with protected controls and well-organized ports | Keyboard versus other controls, thickness, display, grip and working posture |
| One docked pocket companion | A single useful instrument that separates from the core and has a finished home when carried | Whether Flipper or another design fills this role, retention, power/data and standalone behavior |

CAD could resolve the hinge, docking bay, structural carriers, service panels,
connector access and deliberate antenna placement as one assembly. Internal
modularity can support repair while the outside reads as a finished product.
Target leads still need storage and strain relief designed into the experience.
Shielded regions and RF
windows need an electrical purpose and later measurements. Geometry cannot
establish RF quality, thermal performance, or battery endurance by itself.

Exact board outlines, connector protrusions, antenna regions and module
identities are still needed before dimensions are meaningful. The
[physical/system research](../papers/2026-10-15-portable-system-possibilities.md)
compares the transport, power, timing and mechanical consequences.

## Questions to keep open as more parts arrive

- What does the user want to observe, understand or control while carrying it?
- Which results need a screen immediately, and which can be examined later?
- Which events need continuous capture, and which tolerate short snapshots?
- Which operations need local hardware timing, and which can use host messages?
- What should the core do, and what single standalone role earns the pocket companion?
- Does a folding tablet or a clamshell arrangement better support the intended work?
- Which desired behavior calls for custom firmware, and how much of the stack
  would owning it help us change?

The current task remains understanding and discussion. The growing inventory
can reshape every candidate above.

## Use the stash first

The operator is open to key acquisitions and wants existing equipment put to
work. Compare candidates against what is already available before extending
the inventory. For a proposed addition, name the missing capability or
integration problem, identify existing parts it would enable, and explain why
another available part is unsuitable. Interface electronics, connectors,
mechanical parts or power components may unlock more of the stash than another
general computing board; the actual need remains to be established.

The final portable assembly, detachable instruments, development fixtures and
subjects under study can all use existing equipment. A coherent instrument
does not need every useful part inside one enclosure. No hardware shopping
list or purchase is selected. `SHOPPING_LIST.md` currently tracks inaccessible
literature, separately from any future component proposal.
