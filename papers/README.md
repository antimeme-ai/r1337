# Research index

The first parallel frumentarii pass combined source study and literature with
an independently collected device inventory. Read the
[reconnaissance synthesis](../docs/RECONNAISSANCE.md) for consequences and next
experiments, and [device inventory](../docs/DEVICE.md) for direct observations.

## Reports and acquisitions

| Lane | Research report | Acquisition/restoration record |
| --- | --- | --- |
| Hardware/manuals/CPU2 | [Hardware findings](2026-10-15-hardware-frumentarii.md) | [Three PDFs and download gaps](2026-10-15-hardware-acquisitions.md) |
| Firmware source | [Startup, memory, storage, CLI/RPC and ownership](2026-10-15-firmware-frumentarii.md) | [Four source snapshots](2026-10-15-firmware-acquisitions.md) |
| Recovery and tooling | [Recovery mechanisms, host effects and independent references](2026-10-15-recovery-frumentarii.md) | [Four source snapshots](2026-10-15-recovery-acquisitions.md) |

The source snapshots retain exact upstream revisions, original archives,
checksums, restoration commands, and license locations. Acquired code was not
executed and no dependency was adopted. Reports distinguish material actually
read from sources merely located. Original PDFs are ignored in
`papers/hardware/`; extracted source and archives are ignored in `quarantine/`.

## Portable instrument discussion

The operator is gathering more equipment and directed that understanding and
possibility discussion precede further experiments or implementation. Read the
[growing inventory](../docs/HARDWARE_INVENTORY.md) and
[possibility map](../docs/POSSIBILITIES.md).

| Research input | Scope | Acquisitions |
| --- | --- | --- |
| [ESP32 SDR reconnaissance](2026-10-15-esp32-sdr-reconnaissance.md) | Native I/Q, exact chip differences, capture/export limits, external-radio and transmit distinctions | [Three source snapshots and one measurement PDF](2026-10-15-esp32-sdr-acquisitions.md) |
| [Radio module possibilities](2026-10-15-radio-module-possibilities.md) | Exact CC1312R1, classic WROVER and conditional Wi-Fi Module V1 roles | Manufacturer sources linked; no new local corpus |
| [Portable system possibilities](2026-10-15-portable-system-possibilities.md) | Use-driven physical forms, host roles, timing, power, and useful CAD studies | TI LaunchPad hardware PDF and restoration recorded in report |
| [Bus Pirate 5 possibilities](2026-10-15-bus-pirate5-possibilities.md) | Buffered interfaces, target power, capture topology, automation and screen roles | Primary docs linked; exact unit revision/firmware unverified |
| [Network and USB possibilities](2026-10-15-network-usb-instrument-possibilities.md) | Pineapple Mark VII, MK7AC, Bash Bunny and candidate O.MG Plug roles | Primary manufacturer docs linked; no device activation |
| [MR6150 and power possibilities](2026-10-15-mr6150-power-possibilities.md) | Backhaul, actual model limits and battery-label energy arithmetic | Two original NETGEAR PDFs with hashes/restoration in report |
| [MR6150 internals](2026-10-15-mr6150-internals.md) | Exact-model facts, shared-family FCC photographs, RF/power/antenna blocks and software-access gaps | Eight PDF downloads with sources/hashes/restoration; technical sheet overlaps the earlier batch |
| [Wi-Fi 7 SDR reconnaissance](2026-10-15-wifi7-sdr-reconnaissance.md) | Actual W1700K/MT7996 raw-I/Q implementation, firmware, export and measurement limits | [One pinned source snapshot](2026-10-15-wifi7-sdr-acquisitions.md) |

These reports describe candidate uses and source-supported capabilities. They
do not establish results on the operator's boards or select an architecture.
No device operations or source execution accompanied this discussion pass.

## Weird device and sensing research

The operator added camera/basic sensing as tertiary goals and requested a
parallel exploration of Flipper One and unusual device projects. Old iPhones
are also available. Read the [synthesis](2026-10-15-weird-devices-synthesis.md)
for the implications of these references and the current priority order.

| Lane | Report | Acquisitions |
| --- | --- | --- |
| Flipper One portal, source and physical integration | [Flipper One](2026-10-15-flipper-one-frumentarii.md) | [Pinned archives and publication limits](2026-10-15-flipper-one-acquisitions.md) |
| RF/EM and adaptable debug instruments | [Weird instruments](2026-10-15-weird-instruments-frumentarii.md) | [Glasgow source and LibreVNA manual](2026-10-15-weird-instruments-acquisitions.md) |
| Field sensing, camera/thermal and coherent UI | [Field sensing](2026-10-15-field-sensing-frumentarii.md) | [Tricorder/Arducorder source](2026-10-15-field-sensing-acquisitions.md) |
| Analog instruments, control interfaces and sensor packaging | [Analog/control](2026-10-15-analog-control-frumentarii.md) | [PSLab source and Sensirion guide](2026-10-15-analog-control-acquisitions.md) |
| Existing iPhones as components | [iPhone integration](2026-10-15-iphone-integration.md) | Primary Apple/Tailscale documentation linked; no local archive |
| Closed-case sensing: thermal, acoustic, ultrasonic and RF | [Enclosure sensing](2026-10-15-enclosure-sensing.md) | Two original ultrasound/structural-testing PDFs; hashes/restoration and selected read scope in report |

No acquired implementation was executed or adopted; no hardware was selected
or operated. Revision and development status qualify every reference.

The later R8000-like form-factor discussion acquired an original General
Dynamics brochure. Its source, checksum, restoration and read scope are in the
[research journal](../journal/2026-10-15-weird-device-frumentarii.md#r8000-like-service-monitor-form).

## System design and adversarial review

The [first architecture](../docs/ARCHITECTURE.md) and
[capability matrix](../docs/CAPABILITIES.md) synthesize the discussion into a
proposal. Three independent reviews challenged the actual boundaries:

- [Software/action boundaries](2026-10-15-architecture-software-review.md)
- [Measurement, electrical paths and throughput](2026-10-15-architecture-measurement-review.md)
- [Physical integration, power and human use](2026-10-15-architecture-physical-review.md)

Initial findings and revision dispositions are retained in the reports.
No new acquisition, device operation, implementation or dependency accompanied
this design pass. Detailed performance requirements, electrical block design,
power/return domains and motion/volume studies remain ahead of a prototype plan.

## Aftermarket and unusual interaction research

Read the [synthesis](2026-10-15-aftermarket-and-interface-synthesis.md) for
capability gaps, stash overlap and consequences for detailed design.

| Lane | Report | Acquisition/restoration |
| --- | --- | --- |
| Flipper accessories and credential/radio/industrial/sensing additions | [Survey](2026-10-15-flipper-aftermarket-frumentarii.md) | [Four source archives and two PDFs](2026-10-15-flipper-aftermarket-acquisitions.md) |
| BP accessories and adjacent interface/industrial/optical tools | [Survey](2026-10-15-interface-aftermarket-frumentarii.md) | [Three archives, native schematic and datasheet](2026-10-15-interface-aftermarket-acquisitions.md) |
| Overlooked physical/temporal/analog/HMI interaction avenues | [Research](2026-10-15-unusual-interface-avenues.md) | [Six primary PDFs](2026-10-15-unusual-interface-acquisitions.md) |
| Supplied Gemini claims and protocol software | [Claim/tool check](2026-10-15-interface-tool-claims.md) | [URH/Netzob source snapshots](2026-10-15-interface-methods-acquisitions.md) |
| Electrical signatures, UHF reader physics and reflectometry | [Measurement methods](2026-10-15-interface-measurement-methods.md) | [GS1/Huntron PDFs and Keysight HTML](2026-10-15-interface-methods-acquisitions.md) |

Coverage is categorical/representative. Reports separate inspected source,
maker descriptions, provisional integrations and proposed experiments. No
device operation, purchase, dependency, installation or loadout was selected.
Current-module manuals/schematics and unavailable full measurement references
are tracked in [SHOPPING_LIST.md](../SHOPPING_LIST.md).

## Two source baselines

- [Modern official firmware reference](https://github.com/flipperdevices/flipperzero-firmware/tree/3fb1d51727733d2007abc5ec636a89328857803e),
  retained from bootstrap for comparison.
- [Historical official reference matching the reported device hash](https://github.com/flipperdevices/flipperzero-firmware/tree/1af022116e3d6b262289c5668a90f0fa353592c2),
  used to inspect the observed 0.81.1 command and storage behavior.

A matching self-reported identity is not binary authentication. Modern source
must not stand in for the installed-reference behavior. The reports record
source-path links for concrete findings and identify which baseline they use.

## Open literature work

[SHOPPING_LIST.md](../SHOPPING_LIST.md) records original ST PDFs and fresh
schematic links still needed. Several ST documents were readable through web
access while local transfers failed; RM0434 and revision-matched schematics
remain important unread gaps. The CPU2 research paper was acquired and read;
its conclusions were not reproduced on this device.

Next research should reconcile actual chip/protection/layout information with
the historical firmware and published manuals, then support the recovery design
and first owned CPU1 milestone. No project language/runtime or firmware
replacement boundary has been selected.

## Acquisition and timing-engine design

The [engine design](../docs/ACQUISITION.md) compares complete MCU/PIO, iCE40
and larger growth paths, with explicit sample-rate/buffer/transport assumptions.

- [Primary source study and source-file restoration](2026-10-15-timing-engine-study.md)
- [Hardware feasibility, backpressure and timebase review](2026-10-15-acquisition-hardware-review.md)
- [State, output ownership and record-retention review](2026-10-15-acquisition-state-review.md)

These are design inputs, not benchmark results, selected hardware or a prototype
implementation plan. Original-manual download gaps remain separately tracked.
