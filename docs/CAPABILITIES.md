# r1337 capability matrix

Working input to the [first architecture](ARCHITECTURE.md), 2026-10-15. Except
for the [Flipper baseline](DEVICE.md), stash entries are operator-reported;
none of the candidate integrations below has been demonstrated. A gap means
coverage is not yet established, not that a purchase is necessary.

| Capability | Existing starting point / proposed role | Timing and host path | Frontend, probes and unresolved coverage |
| --- | --- | --- | --- |
| UART/SPI/I2C and device access | BP5 candidate internal wired controller; Flipper/Wi-Fi module may offer complementary access/debug roles | Local peripheral timing; exact BP5 automation and installed firmware must be identified | Verify voltage/ranges, buffers, probes, target power and recovery; GPIO does not supply RS-232 or industrial line signaling |
| Digital observation | SLogic32U3 expected future equipment; BP5's own capture may aid local transactions within its actual topology | Independent sampling; sufficient host USB/controller path and storage or bounded capture mode | Delivered revision, channel/rate combinations, input thresholds, voltage limits, probes and clock/trigger connections remain to verify |
| Voltage versus time | AD3 stays on bench; BP5 has a documented limited scope mode to verify against actual firmware; general portable scope remains unresolved | Local ADC, trigger and buffer; capture/export rates are different requirements | Choose channels, bandwidth, sample modes, coupling, input impedance, ranges, differential/common-mode behavior and probes |
| Electrical waveform stimulus | AD3 bench counterpart; evaluate a portable analog assembly shared with scope where appropriate | Local DAC/waveform timing; hardware relationships to capture need design | Define frequency, amplitude, offset, drive/load, source impedance and protection; no portable generator is assigned |
| Sub-GHz packet/timing experiments | Two CC1312R1 LaunchPads as a controlled pair; Flipper offers overlapping/complementary functions | Local radio firmware; host messages/captures depend on chosen image | Exact RF matching, antenna and supported bands matter; packet/RSSI/timing access is not general wideband I/Q |
| Wi-Fi packets and network access | Pineapple/MK7AC as conditional field instruments; Nighthawk as intact backhaul candidate | Local capture plus host/network transport; shared channels/links can constrain capture | Identify revisions, drivers, antennas and actual sustained export; control network availability and radio observation can conflict |
| Raw RF/IQ access | Classic ESP32 research is a bounded, chip-specific experiment; no general receive instrument is selected | Capture passband, depth, duty/dead time, sample format and export path are separate requirements | Define tuning range, dynamic range, protection/attenuation, antennas and reference; Wi-Fi-7 reference does not confer capability on MR6150 |
| Spectrum/emission measurement | No calibrated or general swept instrument is assigned; compare suitable receiver/swept-power paths | Distinguish instantaneous span from swept coverage, update time, event interception and dead time | Define resolution bandwidth/window/detector, relative versus calibrated level, overload and spurious-response conditions; an FFT display alone does not establish this coverage |
| Vector/scalar network response | VNA PCB study is a desired candidate; no installed VNA/SNA | Coherent RF stimulus/reference/receive paths; local sweep/detection, host processing and calibration | Define frequency range, ports, source levels, dynamic range, fixtures and calibration/verification; magnitude-only reuse is conditional |
| Power/EM behavior against events | Bench gear and probes may help characterize a design; no synchronous portable frontend is established | Local trigger/clock relationships and buffering | Select current/shunt or EM probe, gain/bandwidth/coupling, grounding and target-power path; an AC-coupled trace frontend does not replace a general scope |
| LF RFID/NFC/IR and pocket interaction | Flipper is leading optional pocket candidate; existing functions remain subject to baseline/health checks | Standalone operations and documented host interfaces; dock role needs study | Verify peripherals, dock behavior and antennas; custom firmware needs a specific benefit and recovery plan |
| UHF RFID reader candidates | Aftermarket YRM/UCM601/ThingMagic-class paths expose a distinct missing reader function | Reader supplies carrier and receives backscatter; host gets commands/results, not automatically I/Q | Select actual regional range, antenna, reader firmware and supported inventory/memory roles; reader does not imply emulator/sniffer |
| Contact-card / secure-element candidates | NARD/FlipperMeister/SAMadams and BP card fixtures add different contact/provisioning paths | Local card power/clock/reset/protocol plus host transport; SAM processing is separate from RF | Socket, sequenced card interface and provisioned secure element are different parts; no universal keys or encoding APIs |
| Legacy/industrial control | Unidentified controllers, networking gear and cable stock are subjects, fixtures and possible adapters | Adapter handles electrical layer; local bus timing; host owns model semantics and workflows | Identify representative models/pinouts; RS-232, RS-485, CAN, current/voltage loops and contacts are different candidate classes, not confirmed lab requirements |
| Visible inspection | Existing iPhones are candidate cameras/clients; dedicated camera remains open | Local images and metadata can reach host by a verified path; phone is not assumed general USB host | Working distance, focus, illumination, mounting and data export; count a carried phone within core/one-companion constraint |
| Thermal assessment | Reported owned dongle, currently unlocated | Actual host/app/API and original-data access unknown | Identify connector, optics, radiometric behavior and export; surface patterns do not establish an interior thermal image |
| Contact acoustics / ultrasound | Exploratory capability with no identified sensor/pulser/receiver | Audio/vibration sampling or dedicated ultrasonic timing; different frontend classes | Contact response may reveal activity; ultrasound may measure panels/bonds with suitable coupling; neither is a generic component map through an air-backed case |
| Optical test and stimulus | Unidentified optical parts and analog stimulus may support basic experiments | Detector conditioning and local sampling; emitter driver with defined timing | Select spectral band, geometry, intensity/range and driver/detector; imaging, optical power and spectroscopy are distinct |
| Environmental readings | Stash still needs identification; dedicated sensors are conditional | Modest data path; settling, placement and contamination matter | Ambient temperature needs separation from instrument heat; contact temperature and internal health telemetry are different measurements |
| Voice field notes | Tactile capture control, microphone and local host are proposed | Local original audio and session association; remote transcription can follow | Handling/fan noise, feedback, occupied-hand use, storage failure and clock relation to captures |
| Remote support and records | Tailnet host plus remote reference/analysis services are proposed | Bounded original captures/images/text with resumable transfer; no remote timing dependency | Actual service interfaces remain uninspected for this instrument; retain sources/uncertainty and reconcile unknown action outcomes |

## How to compare candidates

For each candidate, fill measured or documented ranges and their conditions,
available direction (observe/stimulate), timebase/trigger, capture depth and
export limits, probe/adapter, power/thermal behavior, dimensions and required
operator controls. Record whether each value is a vendor claim, inspected
implementation or observation on the actual unit. An unspecified cell is a
design question, not permission to substitute a related product's maximum.

Prioritize work that unlocks several existing resources: practical host I/O,
electrical adapters, analog measurement/stimulus and consistent records. RF
network measurement adds a distinct function and supports characterizing the
instrument's own RF accessories. Thermal/optical/acoustic sensing adds context
without displacing the primary RF/EM/debug and secondary control-system goals.

The source reports linked from [POSSIBILITIES.md](POSSIBILITIES.md) and the
[research index](../papers/README.md) support the capability distinctions.
No hardware performance target, purchase or library adoption is selected here.

Capture completeness/gaps, local configuration ownership, output behavior on
host/link/power failure, and integrated grounding/reference planes follow the
contracts in [ARCHITECTURE.md](ARCHITECTURE.md). They apply across the rows;
protocol/measurement names alone do not establish those behaviors.

## Aftermarket and unusual-interface research

The [new synthesis](../papers/2026-10-15-aftermarket-and-interface-synthesis.md)
extends candidate coverage without selecting boards. It adds concrete industrial
frontend families, sampled optical inputs, analog-transducer excitation/response,
electrical signatures and conditional cable reflectometry, documented supply/
optical maintenance channels, event sidebands and physical-panel access.

Retain physical coupling, electrical adaptation, local timing, protocol/device
meaning, provisioned capabilities and practical packaging as separate comparison
dimensions. The supplied Gemini list is checked in the
[claim/tool note](../papers/2026-10-15-interface-tool-claims.md); no library or
software loadout was adopted. Raw samples, threshold decisions, demodulated
bits, packets and decoded fields preserve different information.

The scope/AWG, raw RF, calibrated spectrum and network measurements remain open
requirements. BP5's limited scope, DigiLab frequency indication and packet-radio
expansions do not establish those complete functions. Any new acquisition should
fill an identified range/interface/fixture/timing gap or improve use of the stash.
