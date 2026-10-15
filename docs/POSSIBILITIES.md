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
| Bus Pirate | Potential wired protocol/measurement partner | Generation and actual capture/electrical features remain unknown |
| Xilo controller and other modules | Further compute, sensing or interface options | Wait for actual identification before assigning capabilities |

The [module research](../papers/2026-10-15-radio-module-possibilities.md)
grounds the identified platforms in manufacturer documentation. These are
candidate roles. No board must be included merely because it is available.

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

## Experiences worth comparing

| Possible instrument | Example experience | What would make it useful |
| --- | --- | --- |
| Signal notebook | Examine activity, save selected observations, attach notes, and revisit the same place or object | Clear scope of observation, honest capture gaps, useful local display and storage |
| Controlled experiment station | Send a known IR/radio stimulus and observe a target's wired or sensor response | Independent stimulus/observation paths and a defined trigger/time relationship |
| Portable controller with remote nodes | Leave a sensor or radio node with the subject and inspect results from the handheld | Local autonomy, clear link-loss behavior, and deliberate placement |
| Reconfigurable interface instrument | Exchange a wired probe or radio module as the job changes | Stable module interfaces, identification, connectors and reusable procedures |

These are use proposals, not claims that the current boards already perform
the complete experience. A Bus Pirate might improve the wired observation
part; a Pi might improve analysis and storage; a CC1312R node might move an
observation away from the user's hands. The desired experience should decide
whether each addition earns its power, space and integration cost.

## Physical forms and what CAD can contribute

| Form | Useful when | Cost to investigate |
| --- | --- | --- |
| One compact handheld | Immediate access and one-handed local interaction dominate | Crowded antennas/connectors, enclosure volume, power and service access |
| Handheld core with removable probes | Different jobs need different front ends | Connector durability, module power/data contracts, cable strain and inventory |
| Small folding bench | Several leads, target power and a larger view are central | More carrying volume and a setup step, with more working space available |
| Handheld plus distributed nodes | Observations belong at several physical locations | Multiple clocks, power sources, links and cases |

CAD could let us change module carriers and connector panels while preserving
the hand interface, route probes without loading board headers, place antennas
deliberately, and retain access for repair/debugging. Shielded regions and RF
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
- Does the job favor one object, replaceable probes, or several independent nodes?
- Which desired behavior calls for custom firmware, and how much of the stack
  would owning it help us change?

The current task remains understanding and discussion. The growing inventory
can reshape every candidate above.
