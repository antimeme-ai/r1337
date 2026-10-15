# Aftermarket coverage and unusual interfaces: synthesis for r1337

Research date: 2026-10-15. The operator requested parallel work on Flipper/Bus
Pirate aftermarket coverage and overlooked avenues for interfacing with strange
technologies. Three frumentarii surveyed Flipper accessories, adjacent wired/
industrial tools, and unusual interaction mechanisms. Root checked the supplied
Gemini hardware/software leads and studied electrical signatures/reflectometry.
This is research to refine the first architecture, not a BOM or implementation.

## Read the underlying work

| Report | Scope |
| --- | --- |
| [Flipper aftermarket](2026-10-15-flipper-aftermarket-frumentarii.md) | Credential/SAM/UHF, packet radios, industrial interfaces, optical/analog probing, sensors/camera, carriers and package economics |
| [Bus Pirate and adjacent tools](2026-10-15-interface-aftermarket-frumentarii.md) | Official accessory categories, hidden BP capabilities, programmable engines, legacy debug and industrial/optical frontends |
| [Unusual interaction avenues](2026-10-15-unusual-interface-avenues.md) | Optical/supply/temporal channels, transducers/media, multi-physics, coherent excitation, physical HMI and event sidebands |
| [Supplied claims and protocol tools](2026-10-15-interface-tool-claims.md) | Correct hardware attribution; URH/Netzob source patterns and Wireshark/Scapy roles |
| [Electrical signatures and reflectometry](2026-10-15-interface-measurement-methods.md) | UHF reader physics, bounded V/I characterization and VNA time-domain possibilities |

Each lane preserves primary sources, implemented versus advertised behavior,
actual read scope and acquisition limits. The survey is comprehensive by
capability category and representative design, not a claim to enumerate every
shop/clone or prove which techniques most people overlook. No actual stash
integration, new hardware performance or market-wide price ranking is established.

## What an accessory can really add

Judge each addition along separate dimensions:

1. **Physical coupling:** frequency band, antenna/coil, optical detector, contact
   head, socket or probe geometry.
2. **Electrical behavior:** voltage/current ranges, line signaling, target power,
   isolation, termination and actual loading.
3. **Local timing and observation:** acquisition/trigger/buffering, full analog
   samples versus thresholds/bits/packets, supported controller/target/sniffer role.
4. **Protocol/device semantics:** framing, inventory/transactions, programming
   algorithm, units/state and recovery.
5. **Provisioned capabilities:** keys or permitted secure-element operations;
   generic silicon is not a substitute for an appropriately configured element.
6. **Practical integration:** durable contacts, cables, UI, enclosure, software
   support, availability and serviceability.

A passive carrier can be valuable if it makes a real job repeatable. A cheap bare
module is not a complete comparison with a finished reader/secure-element kit.
The pass does not conclude that named sellers are overpriced. Compare complete
capability and integration cost before making a component recommendation.

## The actual gaps and overlaps

| Capability | New information from the survey | Relationship to stash / design judgment |
| --- | --- | --- |
| UHF RFID reader | YRM/UCM601/ThingMagic-class paths do radio/protocol work and expose host commands. Reader, emulator and sniffer roles differ. | Genuine missing reader function. Existing CC1101/CC1312 tuning does not supply passive-tag powering/backscatter reception. A core host may control a module directly. |
| SAM and contact cards | Original NARD/FlipperMeister use SEC1210 contact-card machinery; SAMadams includes a reader-configured HID SAM. SAM processing and UHF radio are independent. | Distinct credential-processing/contact interface. Useful if relevant subjects exist; no universal decryption, key source or protected-credential encoding is inferred. |
| External CC1101 / stronger IR | Antenna, PA/filter/driver, optics and physical placement can improve use of an existing function. | Significant overlap with Flipper. Earn space through measured coupling/reach or a useful independent counterpart. |
| New packet-radio families | nRF24 and SX1262/LoRa add specific modulation/protocol paths; C5/RTL8720 boards change Wi-Fi capabilities. | Some real additions, substantial overlap with ESP/Pineapple/MK7AC. None closes generic I/Q, calibrated spectrum or VNA coverage. |
| Industrial electrical access | RS-232/422/485, CAN/LIN and current-loop/contact frontends contain real circuitry beyond GPIO. HART adds an AC modem path to loop observation. | Strong gap for the 25-vendor lab. Choose actual interfaces and roles; controller firmware and protocol names do not supply field signaling or command semantics. |
| Programmable/legacy timing | Glasgow applets, USBDM and target-debug probes address different interfaces. FTDI MPSSE/MCU engines/FPGA paths have different roles and limits. | Add a new engine when actual target/timing requirements warrant it. Common SPI/UART alone overlaps BP5. |
| Optical amplitude and probing | Gladiolus preserves sampled optical behavior; DigiLab separates conditioned ADC and comparator paths; demodulated IR receivers discard other information. | Real frontend/ergonomic ideas. Flipper IR and phone images do not establish these measurements. |
| Scope/generator, calibrated RF | BP firmware has a limited 500 kS/s scope mode; DigiLab offers low-cost probing and frequency indication. | Hidden stash capabilities worth verifying, while the general portable scope/AWG and RF measurement design remains open. AD3 stays bench-only. |
| Fixtures and package access | Socket planks, optical shrouds, magnetic-head guides, pogo contacts and observation headers make reliable contact/coupling possible. | High practical value; integrate retained probes/leads and serviceable frontends, avoiding a carried tower of boards. |
| Protocol analysis software | URH/Netzob contain useful analysis patterns; Wireshark/Scapy serve interpretation and packet handling. | Reference study only. Original URH is archived; no library or loadout selected. Preserve original data beneath candidate decoders. |

USB deserves an additional explicit boundary. [Cynthion's maker](https://greatscottgadgets.com/luna/)
documents FPGA-based Low/Full/High-Speed USB 2.0 analysis with Packetry, alongside
separate LUNA/Facedancer roles. [The capture tutorial](https://cynthion.readthedocs.io/en/latest/tutorials/usb_analysis.html)
shows actual host/device analysis, not arbitrary USB3/USB-C/PD capability.
Bash Bunny/O.MG device roles and a BP low-speed-keyboard plank do not establish
that analyzer function. This was a primary-documentation supplement, not an
acquisition, implementation audit or selected Cynthion purchase.

## What the long think changes

The strongest opportunities extend the meaning of an interface. These are
established niche techniques plus our proposed combinations, not a claim to have
invented them:

- **An optical window or status lamp:** raw photodetector timing, documented
  maintenance communication, or bounded optical stimulus. The TI single-LED
  emitter/detector reference is a specific implementation, not evidence every
  LED accepts commands.
- **A supply wire or process loop:** DC operating context plus a small AC overlay.
  HART and PGA300 supply-pin communication are different specific examples.
  Unexpected ripple alone is not proof of communication.
- **A time/state boundary:** startup, reset or documented maintenance entry can
  determine when a pad has meaning. An idle pin can be silent despite a real
  interface. Entry/observation and target-changing actions remain distinct.
- **A transducer:** bridges, RTDs, thermocouples, quadrature, resolver/LVDT and
  encoded media need excitation, conditioning, timing and a physical reference.
  Reading a voltage is not yet reporting pressure, angle or temperature.
- **A repeatable physical signature:** current, near-field EM, contact vibration
  and optical state can jointly reveal an operating transition. Confounders,
  repositioning and independent readback decide whether the conclusion survives.
- **A controlled response:** measured excitation/reference/response can expose
  weak optical/electrical/acoustic behavior. Lock-in or sweep methods have
  bandwidth, stationarity, coupling and interpretation limits.
- **The human panel:** a fitted optical reader or bounded actuator can bridge
  old equipment without replacing firmware. Actuator motion is not equipment
  completion; physical readback and device-specific state still matter.
- **A sideband event:** ready/busy, SRQ, index, trigger, relay and emission timing
  can locate a workflow stall even before the payload is fully understood.

The attractive shared core is a family of protected frontends, bounded stimulus,
local reference/trigger paths and repeatable fixtures around retained records.
RF network measurement, lower-frequency impedance and fast-edge reflectometry
can complement this family but need their own ranges and reference planes.
A single universal input or switch matrix has not been established.

## A useful discovery workflow

Our synthesis for later software/experiment design:

1. Identify equipment, connector/material geometry and documented operating state.
2. Establish energy, electrical domain, loading and intended observation/stimulus
   role before connecting an unknown interface.
3. Retain a useful observation layer and its settings/completeness; record
   decoded candidates separately.
4. Form competing explanations, including instrument noise, coupling artifacts
   and an absent/disabled channel.
5. Choose a bounded experiment that separates those explanations. Keep actual
   stimulus and an appropriate independent response/readback where possible.
6. Promote a repeatable, understood result into a model-specific profile. A
   remote LLM can help find sources or propose a next experiment; a plausible
   guess does not become an executable device command.

This workflow can be followed by an operator before any automation. It does not
select a general inference framework, classifier or new application feature.
TMTSOYP remains reserved for the later core-app discussion without inferred scope.

## Consequences for the next design work

Keep the service-monitor base, screen articulation, local host/engine split and
one optional companion. Add the newly exposed capability classes to requirements
discussion without attempting to enclose every researched board.

Highest-leverage studies, in root's judgment:

1. **Representative lab interfaces and protected analog frontends.** Determine
   actual RS232/485/CAN/loop/transducer needs alongside scope/generator operating
   points. Include source/sink, grounding, common-mode and fault behavior.
2. **A retained optical head and fixture system.** Separate image capture,
   demodulated IR, sampled amplitude and controlled emitters. Compare optical
   alignment/ambient-light limits and routes into planned analog timing.
3. **Independent observation and recorded stimulus.** Specify actual target-side
   logic access, buffer loss reporting, reference/trigger paths and local engines.
   This reuses BP5/future SLogic and informs whether FPGA work is justified.
4. **Selective new radio/credential paths.** UHF is a clear missing reader
   function; LoRa/SAM/other packet paths should follow identified subjects.
   Retain calibrated RF and raw-I/Q requirements as separate unresolved work.
5. **Physical access that earns its storage.** Probe guides, sockets, hooks,
   optical shrouds and serviceable adapters can unlock the stash. Persistent
   lab-side fixtures remain infrastructure rather than extra carried modules.

Review/readback of research: root read all lane reports and acquisition records,
spot-checked central primary claims, inspected URH/Netzob paths and the retained
GS1/Huntron material. A separate interface researcher checked root's hardware/
measurement claims and found no material correction needed. This is documentary
evidence; operating ranges, performance and compatibility still require actual
selected-device work under a later reviewed plan.
