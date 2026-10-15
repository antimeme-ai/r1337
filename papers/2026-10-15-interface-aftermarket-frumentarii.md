# Interface-tool aftermarket and missing electrical capabilities

Research date: 2026-10-15. Scope: Bus Pirate accessories and adjacent programmable
interface, debug, industrial and optical ecosystems. This is a categorical survey
with representative primary designs, not an exhaustive list of store duplicates.
Flipper accessories belong to the parallel lane. No device was operated, source
executed, tool installed, dependency adopted or purchase selected. Exact BP5 board
revision, installed firmware and existing probes remain unknown.

The highest-value additions are **electrical frontends and useful contact
fixtures**: true RS-232/422/485, CAN/LIN, powered current-loop interfaces, proper
contact-card electronics, and analog optical receivers. Another GPIO command
menu adds less unless it supplies a missing timing, target-support or host path.
The existing BP5, future SLogic32U3 and bench AD3 already cover substantial
protocol interaction, independent digital observation and development measurement.
None substitutes for those target-specific frontends.

## 1. Bus Pirate ecosystem: what each accessory actually adds

The current [official accessory index](https://docs.buspirate.com/docs/overview/)
lists the following categories. These pages were read on the research date;
listing, project maturity and stock are separate facts. Existing v3/v4 accessories
must not be assumed to share the v5 connector, pin order, supply path or firmware.

| Accessory category / representative | Actual observation or stimulus | Timing, electrical and firmware boundary | Value for r1337 |
| --- | --- | --- | --- |
| Probe cable, auxiliary cable, KF141 terminals, hooks | Physical access to signals; no new protocol or analog range | Match actual BP main/auxiliary pinout; short returns, contact stability and loading matter. A hook's voltage marking does not raise BP's input limit. | High practical value: retained lead sets and replaceable fixtures can make the existing tool usable inside the service monitor. |
| SOP8 150/208 mil, WSON8 5×6/6×8, DIP8 flash sockets | Reliable contact to supported serial flash parts | Mostly socket/routing hardware; BP runs SPI/flash operations. “Common” flash pinout still needs checking; power/GND switches can reroute socket contacts to IO. | Adds package coverage, not analog isolation, an arbitrary memory programmer or proof that in-circuit access is uncontended. [Sockets](https://docs.buspirate.com/docs/overview/spi-flash-adapters/) |
| IC-card and mini/micro/nano-SIM plank | Contact access to ISO7816-style cards; I2C EEPROM cards, 2-wire cards, half-duplex UART cards use different modes | Sockets expose power, reset, clock, I/O and other contacts; BP supplies timing/power. The board is not evidence of a complete card-protocol stack or a dedicated sequenced card-interface IC. | Contact cards are a distinct gap from Flipper NFC. Useful fixture if the relevant lab devices/cards are identified. [Card adapter](https://docs.buspirate.com/docs/overview/sim-iccard-adapter/) |
| Dual RS-232 plank | Actual bipolar RS-232 translation for TX/RX and RTS/CTS | Two MAX3232-family transceivers; maker offers ADI/Maxim and HGSemi variants, whose identical footprint does not prove identical limits. UART remains local to BP; common signal ground, no isolation established. | Strong candidate missing layer for legacy equipment; DTE/DCE and null-modem wiring still depend on actual equipment. [RS-232](https://docs.buspirate.com/docs/overview/dual-rs232-adapter/) |
| Qwiic / STEMMA / Grove / Gravity / Breakout Garden plank | Routes serial bus, power and optional signals to several connector families | Connector adaptation is not universal level translation or a sensor driver. STEMMA 3-pin is single-signal, not I2C. Each module's rail, pulls, address and signal behavior still apply. | Useful internal sensor harness/reference; existing stash modules may fit before acquiring sensors. [Connector plank](https://docs.buspirate.com/docs/overview/qwiic-stemma-breakout-garden-grove-adapter/) |
| DDR4/DDR5 SPD planks | Access to configuration EEPROM/SPD hub and selected sideband state | Adds sockets, power and level translation. DDR4 has an external 9 V protection-control path; DDR5 has 5 V bulk power and 3.3 V sideband adaptation. This is not DDR waveform analysis or memory-cell testing. | Niche but concrete repair/identification fixture. Big sockets can remain bench accessories rather than dictate the portable panel. [DDR4](https://docs.buspirate.com/docs/overview/ddr4-ram-i2c-adapter/), [DDR5](https://docs.buspirate.com/docs/overview/ddr-ram-i2c-adapter/) |
| Programming-voltage SMPS plank | Adjustable nominal 5–16 V programming supply with target switching/feedback | Explicitly “in development.” Higher voltage alone does not implement a PIC/AVR/EEPROM algorithm, sequencing, calibration or device support. Supplies and output behavior need their own design. | Possible fixture for otherwise inaccessible legacy parts; does not close programmer coverage today. [VPP](https://docs.buspirate.com/docs/overview/vpp-smps/) |
| Infrared Toy v3 | 940 nm LED stimulus; learner output and several demodulated receiver outputs | Learner covers nominal 20–60 kHz; barrier and remote-control receivers have different filtering/AGC/timeouts. LED drive and pulse duty affect load/heat. BP firmware supplies protocol/timing; AnalysIR is a separate host integration. | More informative IR frontend than one remote receiver, but overlaps Flipper IR. It is not an optical power meter or arbitrary analog photodiode recorder. [IR Toy](https://docs.buspirate.com/docs/overview/infrared-toy-v3/) |
| AP33772S USB-PD plank | Negotiates as a USB-PD **sink**, exposes status and shifted CC observation | I2C-controlled sink; documented profiles up to 21/28 V, board fuse 500 mA. Raw USB pins are not a USB protocol analyzer. Page remains work-in-progress with “manufacturing after March 2026” notice. | Useful charger/negotiation test fixture; not a general USB-PD source or the instrument's chosen charger/power tree. Delivery/current revision unresolved. [PD adapter](https://docs.buspirate.com/docs/overview/usbpd-adapter/) |
| PS/2 and USB keyboard pass-through plank | PS/2 and **low-speed** USB observations; documented external trigger output | Current firmware decodes specified keyboard modes, not arbitrary USB 2/3 traffic. Board joins PC/keyboard/BP grounds and selects external versus BP bus power. | A bounded interface-timing example and possible legacy fixture; does not justify a generic USB-analyzer capability. [Plank](https://docs.buspirate.com/docs/overview/ps2-usb-sniffer-adapter/) |
| CAN plank | No established capability from the accessory page | Current official page is explicitly a placeholder for a future plank. | A named catalogue entry must not close the CAN gap. [CAN placeholder](https://docs.buspirate.com/docs/overview/can-bus-adapter/) |

Two subtle electrical distinctions matter. The DDR4 board's optocoupled control
of its programming pin does **not** isolate the whole interface: the adapter also
has common ground. Similarly, the MAX3232 board changes voltage/signaling without
establishing galvanic separation. The acquired RS-232 schematic contains the
two transceivers; its visible component/net content does not show an isolator.
Any product-level isolation claim needs the complete power and return paths.

### Useful capabilities already hidden in BP firmware

Current BP documentation includes **blueTag JTAG/SWD pin finding**, which actively
tests candidate pins; pin discovery is different from a complete GDB target
debugger. Available pins, target voltage and installed firmware constrain it.
Existing Flipper Wi-Fi debug firmware may already supply part of the latter
role, so compare actual target support before adding another probe.
[Pin-finder documentation](https://docs.buspirate.com/docs/devices/jtag-swd-pin-finder/)

The RP2040 scope display is another stash-first lead: nominal **0.5 MS/s**,
selectable IO pin, triggering and a capture buffer, with magnification that can
interpolate displayed samples. The documentation loosely mentions 500 kHz
signals, but 500 kS/s is not a 500 kHz arbitrary-waveform bandwidth. Uniform
sampling at that rate has a 250 kHz Nyquist boundary; useful waveform fidelity
also depends on conditioning, anti-aliasing and higher samples per cycle.
Treat this as a limited low-frequency observation mode to check against the
actual BP5 firmware, not closure of the portable scope requirement.
[BP scope documentation](https://docs.buspirate.com/docs/scope/)

The existing [BP5 report](2026-10-15-bus-pirate5-possibilities.md) remains decisive:
BP5 and BP6 have different capture topology; BP5 driven-output capture can observe
the MCU side rather than the external pin. Target power rating differs by
revision and is not the programmable trip threshold. Current BPIO2 automation,
interactive terminal and legacy BBIO compatibility are different interfaces.
An accessory does not confer the newest firmware mode on this uninspected unit.

## 2. Adjacent interface engines: where another tool adds something

These are alternatives or references, not a proposal to install all of them.

| Engine/ecosystem | Distinct capability and actual host/timing path | Ranges, support and integration limits | Stash comparison |
| --- | --- | --- | --- |
| **Glasgow** | FPGA gateware handles pins; host applets use FIFO-backed USB transport. Specific applets include old memories/CPLDs, ARC/ARM/MIPS debug, Spy-Bi-Wire, MDIO and unusual sensor interfaces. | Production revC3: 16 I/O, 1.8–5 V, up to 150 mA/port. Pre-launch revD: 32 I/O, 1.2–5 V, up to 300 mA/port, new analog path. Sustained USB combined figure 42 MB/s; per-pin maxima are applet/timing dependent. Integrated applet analyzer remains removed; analyzer2 is revD-only. | Best conceptual gain when an obsolete/custom bus or locally defined timing engine is missing; common SPI/UART alone duplicates BP5. Reuse the already acquired snapshot. [Revisions](https://glasgow-embedded.org/en/revisions/index.html), [applets](https://glasgow-embedded.org/en/applets/index.html) |
| **Tigard** | FT2232H MPSSE/USB; separate UART channel while another channel serves SPI/JTAG/I2C/SWD. Supports established host-tool paths and external-side observation header on v1+. | Directional shifters documented 1.8–5.5 V. Supply selector can actively source VTGT or use target reference. I2C is controller-only; docs explicitly exclude clock stretching and caution about other controllers. SPI/JTAG versus I2C/SWD mode switch changes wiring. No isolated industrial frontend. | Faster dedicated programming/debug transport and usable probe/header design; future SLogic can independently observe the external side. Does not make BP unnecessary or provide arbitrary-bus correctness. [Pinned source](https://github.com/tigard-tools/tigard/tree/0dd58e710374880a3ae988f2ddfeb46f5ec8061d) |
| **Black Magic Debug / Probe** | Probe firmware implements target debug/GDB handling; BMDA is a distinct host-side option for supported adapter backends. Target drivers determine actual ARM/RISC-V/other supported parts. | Revision-sensitive electrical hardware: v2.1 documented 1.8–5 V; v2.0 was narrower. Current hardware page lists v2.3 active but marks several expansion features pending. Release 2.1.0 supersedes some page state, including onboard flash support. Source moved to Codeberg; archived GitHub is not current upstream. | Adds integrated debugger semantics, not a scope or protocol transceiver. Compare Flipper-module debug role and named targets first. [Hardware](https://black-magic.org/docs/intro/hardware/), [2.1.0 release](https://black-magic.org/blog/release-v2-1-0/) |
| **HydraBus + HydraLINCAN** | STM32F405 peripherals/local firmware, USB serial/binary control and SD workflows. HydraFW includes smartcard, NAND/MMC, Wiegand, LIN and classical CAN modes in addition to common buses. | Bare digital IO is 3.3 V signaling with selected 5 V-tolerant inputs; ADC/DAC are 0–3.3 V and analog pins have stricter limits. Shield BOM provides two SN65HVD233 CAN and two TJA1021 LIN transceivers. Acquired schematic shares ground and has external +12 V input; no isolation established. | Real LIN/CAN frontend example, plus odd protocols, but requires HydraBus or owned adaptation. Protocol/speed menus do not establish CAN-FD or shield-wide electrical ratings. [Board](https://hydrabus.com/hydrabus-1-0-specifications/), [shield](https://github.com/smillier/HydraLINCAN/tree/5f50c83c4ea8876f1bbe63501c6c8923ef46976c) |
| **GreatFET One + neighbors** | LPC4330 MCU/SGPIO/USB instrument with interface APIs and expansion boards; an FPGA appears on particular neighbors, not the base engine. Foxglove supplies FPGA routing and advanced level adaptation. | Foxglove bank A: 1.2–5 V; bank B: 1.2–3.3 V, including supported differential signals. Source has configuration/rail-control code; this is not ±12 V field wiring. The neighbor list explicitly separates designed boards, progress and rough ideas. | Useful reconfigurable frontend architecture and special optical/USB paths. Board-name lists are not measured, maintained plug-and-play coverage. [Foxglove](https://github.com/greatfet-hardware/foxglove), [maturity list](https://greatfet.readthedocs.io/en/latest/neighbors.html) |
| **Bus Blaster** | Historical FT2232H plus reprogrammable CPLD buffer, intended for OpenOCD/UrJTAG-style JTAG work. Buffer personality changes compatibility. | Manufacturer's v3 sheet documents 1.8–3.3 V and JTAGkey image; SWD wording is conditional. Original wiki was inaccessible here. Do not transfer v3 ranges/configuration to arbitrary v4/clones. | Relevant fast-debug reference, but overlaps Tigard/probes; older stock/documentation state makes it less compelling as a new default. [Original manufacturer sheet](https://media.digikey.com/pdf/Data%20Sheets/Seeed%20Technology/102990047_Web.pdf), [designer explanation](https://dangerousprototypes.com/blog/2010/03/25/bus-blaster-high-speed-usb-to-jtag-spi-uart/) |
| **USBDM** | Dedicated local BDM-family engine with host debugger/programmer support for particular Freescale/NXP families; separate hardware designs have different capabilities. | Official hardware matrix distinguishes HCS08/HCS12/RS08/ColdFire/DSC/Kinetis and selected SWD/JTAG variants. Reset, target-power control, clock adaptation and hardware build matter. Older JS16 example is not the complete family. Published host lists do not establish current Mac compatibility. | Distinct lead for older industrial MCUs; a passive BDM-to-SWD cable cannot translate their debug protocols. Identify actual target before choosing variant. [Primary project matrix](https://usbdm.sourceforge.io/USBDM_V4.12/html/index.html), [JS16 design](https://usbdm.sourceforge.io/USBDM_V4.12/USBDM_JS16/html/index.html) |

HydraFW's [CAN guide](https://github.com/hydrabus/hydrafw/wiki/HydraFW-CAN-guide)
documents silent reception initially, switching to normal mode on transmission;
mode changes can change bus participation, not just UI. Its advertised controller
rate does not override transceiver limits, wiring, termination or classical-CAN
framing. The [smartcard guide](https://github.com/hydrabus/hydrafw/wiki/HydraFW-SMARTCARD-guide)
likewise distinguishes default 3.3 V from other card-voltage classes needing
additional hardware. Ported alternative firmware is not simultaneous HydraFW
capability: HydraBus's own Black Magic instructions retain an enumeration caveat
and an old working-build reference.

A current community branch is
[ESP32 Bit Pirate](https://github.com/geo-tp/ESP32-Bus-Pirate), formerly named
ESP32 Bus Pirate. It documents an S3-focused board set, web/serial interaction,
external radio expansions, and a dock for original BP accessories. This is a
useful UI/adapter interoperability reference. It does not establish classic
WROVER support, protected low-voltage IO, or the external physical layers by
firmware alone. Its broad “3.3V or 5V” warning is not evidence that bare ESP32
GPIO tolerates 5 V; inspect the actual board's frontend and chip limits.
No source snapshot or physical compatibility test was performed for this project.

## 3. Missing electrical classes: representative expansion paths

| Class | Primary-source representative and actual function | What remains beyond the breakout | Potential contribution |
| --- | --- | --- | --- |
| RS-422 / RS-485 | TI ISO14xx family: isolated differential transceivers with 1.71–5.5 V logic-side and 3–5.5 V bus-side supplies. ISO141x/143x/145x have different rate classes and half/full-duplex variants. | Separate isolated-side power, DE/RE turnaround, terminations, bias, grounds/shields and complete assembly layout. UART gives bytes, not Modbus/proprietary device semantics. | High-value industrial frontend for BP/owned controller when lab interfaces justify it. [Acquired TI datasheet](https://www.ti.com/lit/ds/symlink/iso1410.pdf) |
| CAN / CAN-FD | CANable 2.0 is a complete USB/controller/transceiver path; upstream slcan firmware uses explicit FD extensions. Classical CAN and FD are separate controller/firmware/host capabilities. | Exact hardware, transceiver rate, firmware dialect, timestamps, overruns and listen-only behavior. CAN wire signaling and a digital logic capture are different observables. | Possible compact internal engine or reference; software-only BP CAN placeholder is insufficient. [Firmware](https://github.com/normaldotcom/canable2-fw), [maker host guide](https://www.canable.io/getting-started.html) |
| LIN and other single-wire automotive buses | HydraLINCAN's actual TJA1021 parts supply LIN physical signaling beside an MCU UART/LIN peripheral. | External supply, role-specific pull-up/termination, wake/sleep behavior and target electrical limits. A half-duplex TTL wire is not a LIN transceiver; K-line is a separate unqualified class. | Relevant if actual controllers use it; cannot infer a vehicle interface from a connector. |
| 4–20 mA measurement/source | MikroE 4–20mA R Click has INA196 current conditioning, MCP3201 ADC/SPI, and loop-power circuitry; maker describes 4–20 mA becoming 0.4–2 V. A transmitter board is a separate function. | Burden/compliance voltage, active versus passive loop role, loop supply, calibration, return path and overrange. Historic 20 mA digital current-loop serial is another class. | Adds a missing industrial analog observable; BP PPSU current display is not a loop calibrator. [Maker explanation](https://www.mikroe.com/blog/4-20ma-receiver-click-released), [board](https://www.mikroe.com/4-20ma-r-click) |
| HART over current loop | AD5700/5700-1 performs half-duplex FSK physical-layer modulation/demodulation with UART-facing signals, using 1200/2200 Hz tones. | Analog loop coupling, appropriate load/power/isolation, transaction framing and device commands; it is not simply UART connected to loop terminals. | A physical-layer candidate if HART devices are present, not a claimed existing capability. [ADI datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ad5700_5700-1.pdf) |
| 1-Wire with powered operations | DS2482-100 is a self-timed I2C-to-1-Wire master with standard/overdrive timing and active/strong pull-up controls. | Device-specific timing and power needs; parasitic supply for conversions/writes can exceed weak resistor delivery. External power transistor may be needed; strong pull-up and normal open-drain communication are different phases. | Stash BP already speaks 1-Wire; dedicated bridge earns a role for sustained sensor networks or power/timing requirements. [ADI datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ds2482-100.pdf) |
| Contact smartcard electrical interface | NXP TDA8035 is a representative dedicated card-interface device supporting card power, contact signaling and activation/deactivation functions. | Actual voltage class, clock/reset/I/O electrical sequencing, card protocol, socket and target power budget. A socket adds none of these automatically. | More robust multi-class contact-card engine if the passive BP fixture is inadequate. [NXP datasheet lead](https://www.nxp.com/docs/en/data-sheet/TDA8035.pdf) |
| Sampled optical amplitude | GreatFET **Gladiolus** is software-defined IR using photodiode/amplifier/ADC and DAC/LED stimulus; documented receive example 10.2 MS/s, AC/DC coupling. | Optical wavelength/geometry, ambient light, gain, saturation, detector/emitter bandwidth and calibrated response. Neither ADC rate nor remote-control decoding establishes optical power accuracy. | Distinct from IR Toy/Flipper remote control; could inform an owned basic optical-test frontend beside planned analog acquisition. [Pinned design](https://github.com/greatfet-hardware/gladiolus/tree/b3314cb6485b9ae5e5e829c1d1dc9c63d02bbe4d) |

The Click/mikroBUS ecosystem is useful precisely because some boards contain
real line drivers, isolation, current conditioning, modems and power converters.
The socket standard itself supplies none of those, nor is adopting the vendor's
SDK necessary to study the circuits. For example,
[RS485 Isolator 4 Click](https://www.mikroe.com/rs485-isolator-4-click)
names ISO1450, DE/RE and separately powered bus side. Its page advertises 50 Mbps
while its board table says 5 Mbps; it also says the product is not in stock.
Do not select the larger number as demonstrated board performance. TI's acquired
Rev. I, August 2026, datasheet is stronger for chip limits, while board wiring and
complete assembly still determine usable isolation/performance. Chip withstand
ratings are not the finished r1337 input category or a working-voltage allowance.

Other unusual interfaces remain target-driven rather than forgotten: Wiegand,
MDIO, Spy-Bi-Wire, parallel NAND/EPROM, old CPLDs, UART bootloaders, SWIM, BDM,
I3C and proprietary single-wire protocols have different timing, drive and
target-algorithm needs. This pass located implemented examples for several in
Glasgow/HydraFW/USBDM; it does not claim those families cover all of them. There
is no established universal I3C, IO-Link, M-Bus or precision loop-calibration
frontend here. Add the actual interfaces found in the controller inventory to
the requirements before choosing concrete coverage.

### Optical and RF expansion maturity

The acquired Gladiolus schematic names AD9283 ADC, AD9704 DAC, AD8330 variable
gain and photodiode conditioning; these are actual analog paths, beyond a socket
or firmware menu. The design documents 850–950 nm intended over-air targets and
different optional photodiodes; read its 10.2 MS/s example as a documented
workflow, not this project's sustained-throughput measurement. A general visible
optical detector or calibrated optical stimulus needs its own spectral design.

GreatFET's **Lily** RF power detector is a worthwhile reference lead, but its
README lists several *potential* detector ICs with different frequency ranges
and only initial 10 MHz calibration data. That list is not a multi-GHz calibrated
specification. The overarching neighbors page labels multiple radio/measurement
ideas as rough ideas or partial progress. Prefer inspected circuits, firmware
and measured conditions over treating every flower name as an available product.
[Lily design](https://github.com/greatfet-hardware/lily),
[neighbor source](https://github.com/greatscottgadgets/greatfet/blob/main/docs/source/neighbors.rst)

## 4. Design implications and bounded next comparisons

1. **Make the adapter boundary explicit.** Retain connector/pinout, observed
   voltage, source/sink/reference role, bus driver type, pulls/termination,
   permitted return paths and output behavior on loss/reset. For open-drain buses,
   the pull-up rail, equivalent resistance and cable capacitance matter. BP's
   onboard 10 kΩ pulls are useful configuration, not proof of rise time for every
   speed/lead set. [Pull-up documentation](https://docs.buspirate.com/docs/tutorial-basics/pullup-resistors/)
2. **Separate fixture, transceiver, protocol engine and device knowledge.** A
   SOIC socket, MAX3232, local UART and controller-specific command profile are
   four different contributions. The service monitor can integrate those layers
   without exposing a stack of incompatible boards to its operator.
3. **Use independent observation where it helps.** Route target-facing test
   access to the expected SLogic with known electrical compatibility. Neither
   internal controller samples nor decoded success responses prove every
   externally driven waveform. AD3 remains the bench comparison instrument
   within its actual ranges; these accessories do not replace the unresolved
   portable scope/AWG or calibrated VNA/spectrum paths.
4. **Keep timing local; budget exports separately.** MPSSE, FPGA, MCU peripheral
   and dedicated modem paths differ. USB control throughput and Python/web
   interaction are not sample clocks; binary commands still need supported
   firmware, timeout/cancellation and loss reporting. Shared physical pins or
   engines constrain concurrent modes.
5. **Allocate integrated frontend space by capability.** RS-232/485/CAN, a
   controlled target-power rail, contact fixture access and sampled optical
   input are promising gaps. Small active frontends could live on serviceable
   internal carriers with deliberate panel connections. Bulky socket programmers
   can remain bench fixtures; no second collection of carried modules is implied.

## Read/acquired/unknown

Read the cited maker documentation and bounded source/schematic portions;
reused the pinned Glasgow source and earlier BP/analog/instrument reports.
Newly acquired: Tigard, HydraLINCAN and Gladiolus intact pinned source archives;
BP dual-RS232 native schematic at a pinned revision; TI ISO14xx original PDF.
Details, digests, license-source locations and restoration are in the
[acquisition manifest](2026-10-15-interface-aftermarket-acquisitions.md).

Read scope was documentary: no performance reproduced, stock comparison
completed or firmware/board interoperability established. ADI DS2482/AD5700 PDF
downloads timed out; primary PDF text was read through the web tool, originals
were not retained. NXP's TDA8035 PDF was also readable through the web tool but
returned 404 on direct acquisition. Bus
Blaster's old wiki returned access errors; its manufacturer sheet and designer
explanation were available. These are acquisition limits to report to root,
not reasons to stop this bounded survey. If one becomes a selected design input,
obtain its complete current document and inspect the relevant application circuit
before assigning electrical limits. No essential operator-only acquisition is
required to understand this pass's conclusions.
