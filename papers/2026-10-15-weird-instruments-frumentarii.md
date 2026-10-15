# Weird instruments: RF, electromagnetic observation, and adaptable interfaces

Research date: 2026-10-15. Primary documentation and source reading only. No
equipment was connected, software executed, firmware built, or purchase selected.
This is a bounded six-family reconnaissance for the folding-tablet/cyberdeck
discussion. The acquired references are described in the
[lane acquisition manifest](2026-10-15-weird-instruments-acquisitions.md).

The most useful new directions are **measuring complex RF networks**, **capturing
power/EM activity against a hardware event**, and **reconfiguring interface timing
in local logic**. These are concrete capabilities beyond another radio board or
another collection of GPIO commands. Existing Flipper/BP5/Pi/ESP/TI equipment can
remain instruments, subjects, and controlled counterparts without all becoming
boards inside the finished portable object.

| Family | Concrete attraction | Complement to the reported stash | Integration implication |
| --- | --- | --- | --- |
| HackRF + PortaPack/Mayhem | Wide tuning range and autonomous instrument applications | General I/Q exploration beyond Flipper's protocol radios and ESP32's WiFi-derived capture | RF frontend and local processing; selected results can travel remotely |
| Glasgow; GreatFET comparison | Reconfigurable digital timing and unusual interfaces | Stronger case for obsolete/custom buses than duplicating BP5's common-bus terminal | FPGA/MCU handles edges; tablet handles interpretation |
| tinySA Ultra family | Swept level measurements and portable emission inspection | RF troubleshooting of boards, clocks, antennas, and the deck itself | Quiet analog section, controlled gain, suitable probes and input conditioning |
| LibreVNA | Complex reflection/transmission measurements | Antenna, filter, matching, and cable characterization absent from current identified stash | Calibration fixtures and connector geometry belong in the product design |
| ChipWhisperer-Husky | Synchronous power/EM traces and rich hardware triggers | Time-correlated observation beyond slow supply-current readout | Acquire locally, retain traces and trigger context, compare remotely |
| Proxmark3 / Chameleon Ultra | Dedicated contactless timing/trace workflows and compact UI patterns | Considerable overlap with Flipper; useful only where specific depth is missing | Coupling coils and protocol timing matter more than generic CPU capability |

## 1. HackRF and PortaPack/Mayhem: a coherent handheld software instrument

The manufacturer's HackRF One specification documents 1 MHz–6 GHz tuning,
half-duplex operation, up to 20 million complex samples/s, 8-bit I and Q, and
USB power/data. Its clock input/output allows synchronization arrangements with
additional hardware. That makes it a general radio sample source rather than a
collection of fixed protocol peripherals. These are **HackRF One** specifications;
they must not be transferred to similarly named newer boards or clones.
[HackRF One](https://greatscottgadgets.com/hackrf/one/)

PortaPack turns that radio into a self-contained instrument with display,
physical controls, and local applications; Mayhem is the active open firmware
family. Its current repository identifies H1/H2/H4/H4M support, while its hardware
guide distinguishes materially different displays, charging arrangements, and
board implementations. The project recommends checking the exact manufacturer's
compatibility. Public sources and releases exist; this pass did not verify stock,
an exact assembly, or sustained local SD recording throughput.
[Mayhem source](https://github.com/portapack-mayhem/mayhem-firmware),
[hardware versions](https://github.com/portapack-mayhem/mayhem-firmware/wiki/PortaPack-Versions)

The lesson for r1337 is the complete interaction: select an instrument,
perform a useful local task, inspect a result, save it, and return to the menu.
It supplies a better UX reference than making the user manage several attached
development boards. The maximum host stream implies 40 MB/s of unframed sample
payload by arithmetic; it does not establish that every standalone application
records at that rate. A polished core could preserve compact decoded results and
short raw captures without making the remote support station a timing dependency.

## 2. Glasgow: interface personalities implemented in logic

Glasgow packages each interface as an applet with FPGA gateware and host
software. The FPGA side exchanges data through FIFOs; the host gets a socket-like
interface. This places edge timing close to the pins. Published applets cover
common buses, several MCU/debug families, old programmable logic, memories,
environmental sensors, and unusual archival tasks. The interest for a lab spanning
four decades is adaptable timing and interpretation, including obsolete interfaces.
[Introduction](https://glasgow-embedded.org/en/intro.html)

Hardware revision is decisive. The currently documented production revC3 has
16 pins in two independently powered 1.8–5 V ports, with up to 150 mA supplied
per port. RevD, currently described as **pre-launch**, has 32 pins across four
1.2–5 V ports, up to 300 mA per port, and analog measurement at 24 bits/500 kSPS
shared across enabled channels. Both use USB 2; the documented sustained combined
throughput is 42 MB/s. The approximate 100 Mbps/pin figure is an achievable design
bound, not a promise for every applet. These are logic interfaces; the listed
voltages do not qualify an unknown industrial connector or provide an isolated
RS-232/485/CAN frontend.
[Revision comparison](https://glasgow-embedded.org/en/revisions/index.html)

A particularly useful oddity is the new **curve-trace** applet: vary a port supply,
measure voltage/current, subtract an open-circuit baseline, and produce a V–I
curve for a two-terminal part. Reading the pinned implementation confirms that
this is a slow stepped supply/current-monitor procedure, with a default 50 ms
settle interval, not a high-speed analog curve tracer. Its current limits and
electrical range require the exact board and fixture. This suggests an owned
measurement workflow worth exploring around existing BP5 supply/measurement
capabilities before adding another generic interface board.
[Curve tracer documentation](https://glasgow-embedded.org/en/applets/measure/curve_trace.html),
[pinned implementation](https://github.com/GlasgowEmbedded/glasgow/blob/d259cd44f643e9762b529f9e92b3c4ca758fe0aa/software/glasgow/applet/measure/curve_trace/__init__.py)

There are important current software boundaries: introduction text still describes
an integrated cycle-accurate applet analyzer, then explicitly says it was removed
pending redesign; the separate `analyzer2` is currently revD-only. Applet developer
documentation also says the API is not stable. Study the timing/FIFO separation;
do not assume every advertised historical capability is usable on a purchased
revC today. The pinned source contains these qualifications.
[Introduction](https://glasgow-embedded.org/en/intro.html),
[applet development](https://glasgow-embedded.org/en/develop/applet.html)

GreatFET One is a useful comparison: a Python-controlled board with 100 expansion
pins, two USB ports, GPIO, serial buses, acquisition functions, and expansion
“neighbors.” Its USB-oriented applications and expansion architecture are worth
reading, but common-bus access alone overlaps the owned BP5. It becomes a distinct
candidate only when a named USB or interface job warrants its particular hardware.
[GreatFET One](https://greatscottgadgets.com/greatfet/one/)

## 3. tinySA: portable RF metrology and the device's own noise

The tinySA family is a swept spectrum analyzer and signal generator. Exact model
matters: current official comparison distinguishes ZS405 Ultra, ZS406 Ultra+, and
ZS407 Ultra+. Their direct/Ultra/harmonic ranges are different; “can observe” a
high-frequency signal does not establish calibrated direct coverage. Ultra units
have a screen, battery, microSD, USB PC control, adjustable attenuation, and an
optional LNA. Generator and analyzer functions cannot operate simultaneously.
[Official overview](https://tinysa.org/wiki/pmwiki.php?n=Main.HomePage),
[source](https://github.com/erikkaashoek/tinySA)

The high-frequency Ultra path uses repeated measurements to reject images.
Official documentation warns that short and wide signals can defeat that process;
the Ultra and limitations pages give differing width warnings around hundreds
of kHz to MHz. A full wide sweep takes time. This complements a live I/Q waterfall
but cannot substitute for one. The technical description also identifies internal
clock-related artifacts—valuable motivation for measuring the finished deck's
self-noise, not just its external environment.
[Ultra mode](https://tinysa.org/wiki/pmwiki.php?n=TinySA4.Ultra),
[limitations](https://www.tinysa.org/wiki/pmwiki.php?n=TinySA4.Limitations),
[technical description](https://tinysa.org/wiki/pmwiki.php?n=TinySA4.TechnicalDescription)

A small near-field probe could turn this measurement class toward locating noisy
DC converters, displays, digital clocks, and enclosure leakage. That is a design
possibility, not a demonstrated probe calibration. It contributes emission
inspection rather than duplicating packet decoding. Product/documentation paths
are live; exact model stock and measurement performance were not checked.

## 4. LibreVNA: understand the antenna/filter/cable, not only the transmission

LibreVNA is an open two-port 100 kHz–6 GHz vector network analyzer with public
hardware, FPGA, firmware, and host software. It measures complex reflection and
transmission. That lets an instrument characterize antennas, filters, matching
networks and cables, a distinct gap in the reported stash. The architecture uses
RF/IF hardware and FPGA processing before the host performs further calculation.
[Project source and architecture](https://github.com/jankae/LibreVNA)

The acquired manual's sections 3.1, 3.5 and 3.6 describe the order: raw four-port-
relationship S-parameter measurements, calibration, optional fixture removal,
then traces/math/export. Here “four” means S11/S21/S12/S22 from a **two-port**
instrument. Saved calibration includes raw measurements and kit definitions;
Touchstone/CSV export allows useful offline reuse. Calibration plane and fixture
description therefore belong beside the capture. Port extension is not a universal
replacement for fixture characterization.
[Pinned manual](https://github.com/jankae/LibreVNA/blob/c47781910221ba2b02636229920a7c8d48aeb8f8/Documentation/UserManual/manual.pdf)

The manual's power section specifies 5 V and up to 1.2 A through USB-C or suitable
external power, while the data connection is USB 2 **Full Speed**. This is an
excellent contrast with raw SDR streaming: local RF acquisition can produce small
complex sweeps without an enormous transport requirement. A folding instrument
could expose two protected, mechanically supported RF ports and use one main
display instead of reproducing a second standalone UI. Source and manuals are
available; live assembly availability and an in-enclosure thermal/noise budget
remain uninvestigated. No product adoption is implied.

## 5. ChipWhisperer-Husky: correlate an event with power and EM activity

Husky's distinctive feature is synchronous capture: the target and sampler can
share a clock, with hardware triggers for edges, UART bytes, analog thresholds/
patterns, and Arm trace. The documented ADC is 12-bit/200 MS/s (250 MS/s for
Husky-Plus), with an AC-coupled, adjustable low-noise analog input and local FPGA.
High-rate buffered acquisition and USB streaming have different limits. Current
overview and device pages disagree on exact buffer counts, so this pass does not
select one as a firmware-independent capacity.
[Husky](https://chipwhisperer.readthedocs.io/en/latest/Capture/ChipWhisperer-Husky.html),
[comparison](https://chipwhisperer.readthedocs.io/en/latest/Capture/overview.html)

NewAE documents external EM probes and low-noise amplification as another source
for that acquisition input. This could support comparing a known board's physical
activity across boots, firmware states, or attached loads. It adds time-correlated
observation, whereas BP5's slower current measurement describes another timescale.
Probe position, clocking, gain, trigger, and wiring must accompany the trace.
The AC-coupled input is not a general DC oscilloscope input. Digital I/O is 3.3 V;
unknown industrial signals need appropriate frontends. Public source and current
products exist; no particular kit, probe, or stock was selected.
[EM probe documentation](https://chipwhisperer.readthedocs.io/en/latest/cw_tips_tricks/common_questions/em_probe.html),
[source](https://github.com/newaetech/chipwhisperer)

## 6. Proxmark and Chameleon: dedicated coupling and compact interaction

Proxmark3 is an LF/HF contactless research platform with MCU/FPGA division,
protocol traces, and host scripting. Its published trace notes describe retaining
and exporting protocol observations. Exact hardware support and client/firmware
pairing matter; reduced-flash variants lose features. It complements Flipper only
where specific protocol depth, timing, or trace analysis is required.
[Source](https://github.com/RfidResearchGroup/proxmark3),
[trace representation](https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/trace_notes.md)

A timely curiosity in that repository is **Proxmark5**: a newer MCU/FPGA platform
with swappable antennas and a connectivity/battery addon. The current README
explicitly marks firmware unstable, tells users not to install that addon yet,
and calls the UHF addon **not developed yet**. Those roadmap entries are not
available capabilities. This is a watch lead, not a component recommendation.
[Current maintainer README](https://github.com/RfidResearchGroup/proxmark3/blob/master/README.md)

Chameleon Ultra provides another pattern: a compact nRF52840-based contactless
device with separate applications, including BLE clients. It has public firmware,
hardware, CLI and documentation. Its lesson is a pocket companion whose timing
and coupling stay local while the main display handles configuration/results.
It is a dedicated LF/HF protocol instrument, not a general-purpose wideband SDR.
Both families overlap existing Flipper capabilities substantially; establish a
specific missing function before assigning the one permitted pocket module to
this role. Current maintainer distribution links exist; no stock checked.
[Chameleon source](https://github.com/RfidResearchGroup/ChameleonUltra),
[documentation source](https://github.com/RfidResearchGroup/ChameleonUltraDocs)

## Implications worth carrying into design discussion

1. **Design the measurement classes before counting radios.** I/Q, swept power,
   complex S-parameters, logic edges and synchronous analog traces answer different
   questions. A larger catalogue of radio protocols does not automatically cover
   those measurement gaps.
2. **Put time-critical work beside the connectors.** FPGA/MCU acquisition and
   triggers can run locally. The tablet provides a coherent UI, stored captures,
   and tailnet-assisted interpretation. Losing connectivity must not destroy a
   locally running acquisition or its original data.
3. **Make fixtures and calibration part of the object.** Antenna coupling,
   reference clocks, probe placement, ground paths, analog gain, and cable
   reference planes can dominate results. Finished connector placement, probe
   storage, quiet power, and shielding deserve space alongside processors.

Read scope: official capability/revision/architecture pages and the cited protocol/
measurement documentation; bounded source inspection of Glasgow's introduction,
revC hardware description, applet documentation, and curve tracer; selected
LibreVNA manual sections on power, data flow, calibration, and fixture removal.
Other project repositories were inspected at their public documentation level,
not exhaustively audited. No measured performance or interoperability was
reproduced. One attempted Mayhem architecture wiki URL was nonexistent; no claim
rests on it. The two useful references were acquired successfully; no essential
inaccessible document was identified for operator acquisition.
