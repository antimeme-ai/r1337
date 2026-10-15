# Portable system possibilities — 2026-10-15

The interesting opportunity is a portable instrument with separable controls, acquisition hardware, and bulk storage. The inventory could support several versions of that idea: a compact handheld with interchangeable probes, a handheld controller with a separate compute/storage pack, or a small case that opens into a bench. These are candidate arrangements, not a selected design or a proposal to connect everything at once.

Scope: a bounded physical/system architecture pass using the operator's named equipment and primary documentation. No equipment was connected, inspected, powered, reprogrammed, or modified in this lane. No software was installed or dependency selected. The Flipper remains a useful development target even if the eventual portable instrument uses several independently owned firmware components.

## What the named equipment suggests, and what remains unknown

| Named equipment | Documented capability relevant to this discussion | Identification or measurement still needed |
| --- | --- | --- |
| Flipper Zero | Existing screen/buttons, battery, removable storage, peripheral interfaces; installed firmware exposes USB as a device | How much UI/control work it should own; sustained capture/storage rates; acceptable enclosure access to its native interfaces |
| Flipper Wi-Fi module v1 | Official developer board uses ESP32-S2 and provides SWD debugging through USB or Wi-Fi | Board markings/revision, installed firmware, accessible pins, power wiring, and physical dimensions |
| Freenove ESP32-WROVER board + extension | A separate ESP32 platform; Freenove's FNK0060 reference supports WROVER applications | Exact Freenove product/revision and extension model, PSRAM/flash sizes, camera or other peripherals actually present, USB bridge and pin reservations |
| TI LAUNCHXL-CC1312R1 | Sub-1 GHz MCU LaunchPad with separate XDS110 debugger/USB-UART bridge and selectable power/debug jumpers | Jumper positions, antenna path, board revision, installed firmware, available header access |
| Assorted Raspberry Pis | Some Pi computers can supply USB host, filesystem and display/network services | Exact models: a Pi computer, Zero, Compute Module, and Pico imply very different roles; do not infer Linux, ports, dimensions, current, or cooling from the family name alone |
| Xilo flight controller | Unknown board; no MCU, sensors, USB role, storage, supply range, or debugger capability established | Model/revision and clear component/connector identification before assigning any role |
| Assorted modules; Bus Pirate sought | Possible specialized probes and adapters | The modules and any Bus Pirate generation must first be identified; the latter is not yet confirmed available |

Primary anchors: [Flipper developer board](https://developer.flipper.net/flipperzero/doxygen/dev_board.html), [Freenove's FNK0060 repository](https://github.com/Freenove/Freenove_ESP32_WROVER_Board), and [TI LaunchPad](https://www.ti.com/tool/LAUNCHXL-CC1312R1). These describe product families or named products, not observed state of the operator's individual boards.

## Three use-driven physical arrangements

| Arrangement | Work it favors | Components' possible jobs | Benefits | Costs and unanswered questions |
| --- | --- | --- | --- | --- |
| **Handheld with detachable probe cartridges** | Walk up to equipment, make a short measurement, inspect a result, move on | Flipper supplies controls and local status; one probe at a time performs a defined bus/RF/sensor task; a selected ESP32 or TI board might become one probe | Smaller working set; shorter target wiring; individual modules can be changed or recovered separately | Full development boards may overwhelm a pocket-sized envelope; connector/power design and pin protection still need ownership; existing Flipper firmware does not automatically control these boards |
| **Handheld controller plus compute/storage pack** | Longer logging, several probes, local analysis, session comparison | A confirmed Pi computer hosts USB/storage and heavier processing; Flipper provides portable controls/status; MCU probes capture near the target | UI, recording and acquisition can evolve independently; probe can stay on a target while controls move; compute heat and battery mass need not sit in the hand | More cables or a wireless control link; separate power domains and failure recovery; a phone/laptop may still be needed for initial development or rich presentation |
| **Small fold-out bench** | Repeated embedded work at a table, clipping to boards, experimenting with several instruments | Case retains an optional Pi host and power distribution; removable trays hold Flipper, LaunchPad, ESP32 and probe adapters; lid may hold controls/display or cable storage | Space for target fixture, short organized leads, reset/debug access, ground points and visible power state; existing boards can stay intact | Larger carry volume; hinge/cable routing, ventilation and operating stability matter; less useful while walking or working one-handed |

The sparse handheld—Flipper plus one module, with analysis elsewhere—also remains a candidate. There is no requirement to put every board into a final object; separate boards can serve as experimental endpoints without becoming enclosure residents.

## Connectivity: decide who hosts which link

The [upstream Flipper USB HAL](https://github.com/flipperdevices/flipperzero-firmware/blob/3fb1d51727733d2007abc5ec636a89328857803e/targets/f7/furi_hal/furi_hal_usb.c) initializes a USB device stack. Today's USB-C connection is therefore not a ready-made USB host for the other boards. Its [GPIO documentation](https://docs.flipper.net/zero/gpio-and-modules) describes bridges such as USB-UART and separates supply pins from 3.3 V I/O; power-pin voltage does not establish signal compatibility.

TI's [SWRA588B hardware guide, sections 4.1–4.6](https://www.ti.com/lit/an/swra588a/swra588a.pdf) distinguishes the CC1312R application MCU from XDS110, which supplies programming/debug and USB-UART. P4 disconnects the target/debug sections; P10 selects the target power source. A USB cable reaching this LaunchPad is not evidence that the CC1312 application has native USB or that the bridge transports arbitrary sample rates.

A candidate Pi-host arrangement is a **star**: one explicitly chosen host/hub talks to Flipper's USB interface, the TI bridge, and whichever USB bridges/probes are actually identified. Multiple downstream devices do not become hosts merely because they share a hub. For a Zero-class Pi, [official Zero documentation](https://www.raspberrypi.com/documentation/computers/zero.html) distinguishes the power connector from its OTG data port. Other Pi variants have different port/role arrangements. Confirm the actual model before drawing a wiring diagram.

An MCU-only arrangement could use an owned UART/SPI link, trading the Linux host for firmware/protocol work. Acquisition beside the target can keep sensitive probe wiring short while a different transport carries buffered results.

The ESP32-S2 silicon also supports USB host operation in Espressif's [host documentation](https://docs.espressif.com/projects/esp-idf/en/v5.1.1/esp32s2/api-reference/peripherals/usb_host.html). This is a possible separate research route, not a claim that the stock Flipper Wi-Fi module is wired, powered, or flashed to host the proposed instrument network. VBUS sourcing, role circuitry, device classes and SDK-specific hub support would need study. The classic ESP32-WROVER is not interchangeable with the S2; [Espressif's family comparison](https://docs.espressif.com/projects/esp-techpedia/en/latest/esp-friends/get-started/board-selection.html) lists different peripherals.

If the Bus Pirate turns up, its [official logic-analyzer documentation](https://docs.buspirate.com/docs/logic-analyzer/logicanalyzer/) shows why the exact generation matters: follow-along capture paths differ between hardware versions. It could be a detachable bus instrument, but its buffering, target-voltage handling and host protocol must be checked against the actual board.

## Acquisition, storage, and correlated time

A candidate split is hardware capture and bounded buffering at the probe, then host storage/presentation. Sampling should not depend on UI refresh or transport scheduling. No rate, latency or losslessness is claimed for these boards.

Espressif's [RMT documentation](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/rmt.html) shows a concrete example of hardware recording pulse-duration/level symbols into memory. It also documents finite buffers and chip-dependent DMA support. It suggests a pulse-task pattern, not a general logic-analyzer capability claim.

WROVER PSRAM is useful candidate workspace, but is not all equivalent to internal peripheral memory. Espressif's [external RAM guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/external-ram.html) describes internal-memory requirements for some buffers, shared cache effects, and external-memory unavailability while flash cache is disabled. A capture design therefore needs its own buffer/overflow analysis even when advertised RAM capacity looks ample.

A later design should distinguish **acquisition ticks**, **host arrival time**, and **civil date/time**, retaining the mapping and its uncertainty.

A synchronized date display does not prove cross-probe edge alignment. [ESP-IDF system time](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/system_time.html) explicitly permits wall-clock steps or gradual adjustment. For tight correlation, evaluate a shared trigger/clock and measure skew/drift with one signal seen by both probes. That requirement would affect connector and enclosure layout; clock identity, restart and gap reporting would matter to recorded data.

Burst capture, continuous logging and decoded event logs have different storage needs. Flipper SD, an identified ESP32 storage path or a Pi filesystem are candidates; sustained rates and failure behavior remain unmeasured. A recorder would need explicit overrun/incomplete-capture reporting. No format or transport implementation is selected.

## Power, heat, RF, and enclosure consequences

**Power:** treat each connector as a source/sink decision, not just a place to join matching voltages. Flipper's documented GPIO supply behavior changes when USB is present. LaunchPad power selection depends on its jumpers. Raspberry Pi's [hardware documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html) makes peripheral power limits model-dependent and discusses unwanted upstream back-powering from hubs. A common battery system would need explicit power paths, switching/limits, grounds, charging and shutdown behavior. No battery, runtime, regulator or numerical Pi power budget is assigned.

**Heat:** identify Pi/ESP32 variants and sustained workloads before allocating a sealed compute bay. A removable pack or vented fold-out layout allows more freedom for measured thermal design. Grip surfaces, battery placement and any heat spreader would need thermal/RF consideration.

**RF and EMI:** distinguish an ESP32's own radio scheduling from interference between boards in a box. Espressif's [coexistence guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/coexist.html) describes time-sharing of the ESP32 RF resource; adding cores does not give its Wi-Fi and Bluetooth independent simultaneous radios. Separately, close board placement, supplies, digital cabling and the final case can affect receiving performance. Espressif's [module placement guidance](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32/pcb-layout-design.html) calls for antenna clearance and testing of the assembled product. Its 15 mm clearance recommendation belongs to the illustrated ESP32 module context, not a universal spacing rule for all these boards. A dense universal handheld therefore needs RF comparison against the separate-board baseline, including different module power states.

**Target interfaces:** a detachable probe cartridge could make target voltage, signal direction, ground and protection visible and replaceable. Protection, level shifting and allowable cable length require design for the actual bus. An unidentified flight controller or extension board does not become a generic protected probe simply because it has many connectors.

## What CAD could usefully do now

Early CAD can answer real ergonomic and assembly questions before the electronics are settled:

- Reversible carriers for the intact boards, with accessible boot/reset buttons, jumpers, debug headers and removable media.
- Grip and button reach mockups, screen viewing angle, bench tilt and whether probe leads pull the object over.
- A module rail or removable tray with alignment and strain relief, leaving the electrical connector unspecified until its signals/power requirements are known.
- Cable routing with bend and unplugging space, connector protection, and leads stored without loading GPIO headers.
- Antenna and sensing-face keepout volumes so a later battery, fastener, hub or metal heat spreader cannot silently occupy them.
- A fold-out work surface or target-board fixture that retains clips and separates exposed target wiring from the instrument's power components.

These are candidate mechanical studies, not requested CAD deliverables. Start with measured board/connector envelopes and simple reversible fits. A polished outer shell, permanent stacking arrangement, battery compartment and final connector panel become more useful after deciding whether the primary job is walk-up measurement, prolonged logging, or bench work, and after identifying the Pis and Xilo. CAD can shape that discovery; it need not wait for a finished firmware architecture.

## Source acquisition in this lane

TI SWRA588B, *SimpleLink CC1312R LaunchPad for 868 MHz/915 MHz Bands LAUNCHXL-CC1312R1*, revised December 2018, was downloaded on 2026-10-15 from `https://www.ti.com/lit/an/swra588a/swra588a.pdf`. Despite the URL suffix, the acquired document identifies itself as revision B. It is retained unchanged at ignored `papers/portable-system/ti-swra588.pdf`; SHA-256 `54151b07b17ac7a0d31bdb2a05187e52ca265b2367fcf25b0e768e9a6bc2c1e1`. Sections 4.1–4.6 were read from text extracted with existing `pdftotext` into ignored `context/portable-system/ti-swra588.txt`. No diagram-dependent dimension or wiring claim was inferred. Restore with `mkdir -p papers/portable-system` then `curl -fL https://www.ti.com/lit/an/swra588a/swra588a.pdf -o papers/portable-system/ti-swra588.pdf`, and compare `shasum -a 256 papers/portable-system/ti-swra588.pdf` to the recorded digest. The PDF carries TI copyright and terms; it is literature, not adopted implementation code.

Other citations are live primary vendor pages checked on 2026-10-15; they were read as references, not acquired as executable software. The web tool could not fetch the large TI PDF, but direct download succeeded, so no operator acquisition request follows from that tooling limit.
