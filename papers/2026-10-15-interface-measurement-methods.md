# Electrical signatures, reflectometry and why frequency is insufficient

Research date: 2026-10-15. Root supplement to the parallel aftermarket and
unusual-interface surveys. This studies reusable measurement paths; primary
descriptions and proposed experiments are distinguished. No stimulus occurred.

## UHF RFID is a useful counterexample

[GS1 Gen2 release 3.0.1](https://ref.gs1.org/standards/gen2/3.0.1/), February
2026, describes passive tags receiving operating energy from a reader. During
tag response the reader supplies a continuous carrier and receives backscatter.
Signaling/timing go beyond an ordinary packet transceiver's tuning frequency.
The link's half-duplex command/reply description does not remove the carrier
requirement during reception.

This edition describes 860–930 MHz; older editions and module marketing can give
other ranges. Do not substitute a standard's scope for a module's regional RF
configuration or optional commands. Reader, tag emulator and passive observer
are distinct roles. Engineering conclusion: CC1101/CC1312 frequency overlap
alone does not fill the UHF-reader gap.

[SAMadams](https://www.redteamtools.com/sam-adams-for-flipper-zero/) adds a
secure-element interface. Its maker separates UHF SIO processing from the
absent UHF radio reader and describes its supplied SAM as reader-configured,
without credential-encoding APIs. It is neither a new-frequency radio nor a
universal source of credential keys. See the Flipper aftermarket report for
carrier/reader/SAM configurations.

## Measure a port before naming its protocol

Huntron's [analog-signature introduction](https://huntron.com/sales-support/pdf/ASA-paper-extract.pdf)
describes current-limited AC excitation and voltage-versus-current observation.
Frequency, source impedance and amplitude change the reactive/nonlinear behavior
visible. It commonly compares known-good and suspect assemblies. A node measures
its connected network, not necessarily an isolated component; a difference
suggests a problem without uniquely locating its cause.

Engineering proposal: bounded stimulus plus simultaneous voltage/current
observation could characterize candidate ports, sensors and cables and compare
channels before choosing a driver. AD3 can support development within its actual
capabilities; portable implementation still needs its own frontend. BP5's slower
voltage/current context is not automatically this analog acquisition path.

An unpowered target need not be inert: applied stimulus can charge nodes or
conduct through junctions. Define energy state, amplitude/current and returns.
Parallel circuits/nonlinear state permit several explanations for one signature.

Proposed comparison: known R, C, diode and mixed networks under specified
source conditions, then repeatable measurements on a known accessible board.
Check predicted response changes and fixture repeatability before interpreting
unknown traces. No circuit, experiment or component identification is selected.

## The proposed VNA could investigate interconnects too

Keysight's [time-domain documentation](https://helpfiles.keysight.com/csg/m9485a/applications/timedomain.htm)
describes transforming calibrated complex frequency measurements into delayed
responses. Reflections indicate impedance changes relative to the calibration
plane. Span/window affect resolution; spacing affects alias-free time range.
Changing plot density cannot improve measurement resolution. Loss may limit
useful range even when the unambiguous time window is long enough.

Engineering proposal: suitable VNA bandwidth/calibration/adapters might support
cable delay/fault-location and connector-path investigation alongside antennas/
filters. This does not identify the digital protocol on a cable or image behind
an arbitrary metal case. A VNA transform and pulse/step TDR are different
implementations. A slow sweep requires sufficient subject stability; transient
faults can be missed or distort the synthesized result. Physical length needs
propagation-speed information.

Low-frequency I/V impedance, RF S-parameters and fast-edge reflectometry need
different useful ranges/fixtures. No unspecified source/ADC is assigned all three.
Proposed comparison: documented cables, open/short/load and known discontinuity,
a named calibration plane, varied span/spacing/window and predicted delay/alias
behavior. No nominal bandwidth or spatial resolution is promised.

## Shared functions worth designing

These are r1337 design candidates, not claims about an existing product:

| Function | What it could unlock | Required context |
| --- | --- | --- |
| Protected, defined-impedance V/I observation | Port/sensor/load characterization, signatures | Ranges/common-mode/loading, bandwidth, target energy and returns |
| Bounded source with measured reference | Electrical/optical response, simple transfer/impedance measurements | Delivered stimulus, limits, settling and local output-fault behavior |
| Repeatable fixture and calibration plane | Meaningful comparison across locations/devices/states | Position, contact/coupling, harness and reference changes |
| Local trigger/clock/event context | Relate traces to target actions or another sensor | Actual synchronization, drift and missing captures |
| Several views of retained observations | Revisit protocol hypotheses | Samples, threshold decisions, fields and meanings remain distinct |

No universal crosspoint matrix is implied: routing/protection suitable for one
measurement can spoil another. A coherent set of frontends/fixtures around
shared acquisition, stimulus/reference and records is the stronger hypothesis.

Original GS1/Huntron PDFs and Keysight HTML plus read scope/restoration are in
the [acquisition record](2026-10-15-interface-methods-acquisitions.md). Keysight's
full impedance handbook and downloadable time-domain app note could not be
acquired; no unread handbook is claimed as evidence.
