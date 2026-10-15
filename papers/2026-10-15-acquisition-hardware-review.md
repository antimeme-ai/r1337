# Acquisition-engine review: hardware feasibility, rates and time

Review date: 2026-10-15. Reviewed [ACQUISITION.md](../docs/ACQUISITION.md)
and the [timing-engine study](2026-10-15-timing-engine-study.md), current
instructions, architecture/capability context, and existing BP/Glasgow/analog/
interface evidence. Scope is a first detailed block/contract design, not a
finished schematic, implemented engine or procurement decision. Comparison
workloads are explicitly assumptions, not operator requirements or measured
claims. No source execution, builds, devices or acquisitions in this review.

## Assessment

The complete-path comparison is sound enough to continue block design. The
numerical workload budgets are correct; on-chip versus external memory and
UP5K/HX8K distinctions are appropriately qualified. No unsupported board is
assigned an analog/RF frontend or a sustained host path. One medium contract
finding concerns time lost under backpressure; one low finding concerns the
difference between nominal frequency, average rate and sample-time accuracy.
Neither requires selecting a chip or setting finished-instrument bandwidth now.

## M1 — Medium: backpressure must not silently stretch sample time

**Section:** “Comparison workloads and arithmetic,” lines 87–91; “Acquire and
report,” lines 158–167; “Independence and contention,” lines 191–194.

**Failure:** The design considers rate mismatch and retains known gaps, but
does not specify whether backpressure may pause acquisition itself. A capture
engine can fill a FIFO, stall, and resume without dropping a stored word. It
can eventually report the requested sample count while skipping elapsed target
time. Rendering those words at one nominal sample interval silently compresses
the stall out of the measurement. The final capture buffer may have ample
capacity: a short DMA/arbitration service gap can stall an intermediate FIFO
before that buffer is full. A transaction engine may also hold a driven pin
longer while waiting for data, which is valid only if the target protocol and
mode allow it. A stimulus FIFO can underflow too: pausing a waveform may hold
its last driven level or lengthen a pulse while later sending every queued
value. Correct value count does not make the delivered stimulus correct in time.

This is concrete for the proposed PIO path. The official RP2040 datasheet's PIO
stalling/autopush descriptions state that an `IN` with autopush stalls on a full
RX FIFO. Its FDEBUG RXSTALL indication also covers a nonblocking push that lost
data; a sticky flag alone does not locate every missing interval. This is a
hardware behavior to account for, not evidence that PIO is unsuitable.
[RP2040 datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf),
sections 3.2.4, 3.4.4, 3.5.4 and FDEBUG register description.

**Proposed resolution:** Each mode declares whether its subject/source can be
paused, and where backpressure may act. Uniform sampled observation must either
maintain its sampling schedule while reporting losses, terminate the valid
record on a stall, or preserve sufficient time/index information to describe
nonuniform acquisition. A sample index tied only to successful FIFO pushes is
not elapsed acquisition time. If precise lost-time location is unavailable,
mark the affected timing/completeness unknown rather than fabricate continuity.
For a throttleable transaction, identify permissible wait points and output
state during a wait. For time-defined stimulus, define underrun detection and
the locally enforced abort/hold/completion behavior; do not silently resume and
declare the original waveform delivered. A held state is acceptable only when
the mode's electrical and timing contract permits it. Otherwise stop according
to the mode's defined policy and invalidate the affected stimulus/reference
relationship. These distinguish uncontrolled observation, throttleable protocol
work and an underflowing source rather than applying one universal pause rule.

Add the maximum local memory-service interruption/FIFO headroom to later path
qualification, alongside average sustained throughput. The proposed known-input
and fault tests can cover this directly; no separate verification framework is
needed at this stage.

## L1 — Low: record the timebase's accuracy and sample schedule explicitly

**Section:** “Configure and arm,” lines 138–141; “Acquire and report,” lines
158–167; engine comparison's clock-plan requirements.

**Failure:** A requested rate, divider-derived average rate and physically
measured/calibrated rate can all be labeled “actual sample rate.” An internally
consistent waveform may still give inaccurate periods or sweep/reference
relationships if the timebase tolerance/drift is unknown. Moreover, some local
clock dividers achieve an average frequency with unequal adjacent intervals;
representing that as uniformly spaced samples can introduce a separate timing
error even without FIFO stalls. Input synchronizer latency and cross-instrument
skew, already covered, do not resolve these effects.

The RP2040 PIO clock-divider section documents fractional division that extends
selected cycle intervals and explicitly discusses the resulting jitter.
This gives a concrete reason to distinguish an average programmed rate from a
uniform sample schedule; it is not a requirement to use fractional division.
[RP2040 datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf),
section 3.5.5. No particular oscillator tolerance is asserted for the candidates.

**Proposed resolution:** Require clock source/reference identity, applied divider
or schedule, and whether the rate is nominal, inferred or measured/calibrated.
Carry known accuracy/drift/jitter limits or state them unknown. For a nominally
uniform sampling mode, qualify the allowed interval variation against its
measurement purpose; for deliberate nonuniform/event timing, preserve the
time representation. A common reference and a PLL do not by themselves certify
absolute time accuracy or remove all sample-clock jitter. Numerical tolerances
remain operating-point requirements to choose later.

## Direct arithmetic checks

Recalculated from stated representation and duration, without testing an
implementation:

| Case | Payload bytes/s | Payload bytes | Result |
| --- | ---: | ---: | --- |
| D2 | 10000000 | 100000 | Correct |
| D3 | 40000000 | 400000 | Correct |
| A1 | 4000000 | 400000 | Correct |
| A2 | 100000000 | 2000000 | Correct |
| R1 | 40000000 | 800000 | Correct: I and Q are two stored 16-bit values per complex sample |

128 KiB / 40 MB/s is 3.2768 ms; 100000 bytes / 1 MB/s is 100 ms. The example
therefore has at least 110 ms between acquisition start and completed upload,
before re-arm/control work. This is correctly presented as an illustrative
dead-time consequence, not a guaranteed host rate. Finite duration, packed
representation, headers/alignment and exclusion of guaranteed compression are
handled correctly.

264 KiB total RP2040 SRAM and UP5K's separate 128 KiB SPRAM plus 15 KiB EBR
cannot retain a 400000-byte D3 record without another path. The design does not
improperly sum their resources into a single dual-port FIFO. A stated 512 KiB
memory fits that payload, but fit alone establishes neither service rate nor
concurrent producer/consumer operation; the document already makes this clear.

## Hardware and frontend boundaries checked

- **MCU/PIO:** Finite state machines, shared instruction memory, SRAM/DMA/bus
  contention and board export remain explicit. Existing BP5 is correctly kept
  as an occupied instrument rather than counted as a spare RP2040. A protocol
  peripheral alone is not an independent target-side observer.
- **Small FPGA:** UP5K logic/DSP/SPRAM facts are distinguished from HX8K resources.
  Larger-FPGA escalation is conditional; neither family name nor unused logic
  cells supplies an ADC, field-voltage frontend, deep capture or host bridge.
- **Development boards:** Independently reopened current maker pages. The
  [iCEBreaker listing](https://1bitsquared.com/products/icebreaker) supports
  V1.1b, USB-C and fitted 64 Mbit QSPI PSRAM; an older search result still exposed
  V1.1a. The [older hardware page](https://docs.icebreaker-fpga.org/hardware/icebreaker/)
  describes optional async-FIFO wiring, correctly not presumed qualified on the
  new board. The [Olimex page](https://www.olimex.com/Products/FPGA/iCE40/iCE40HX8K-EVB/open-source-hardware)
  supports external SRAM and the separate programming-path discussion. No
  claimed data rate is inferred merely from either board's RAM capacity.
- **Complete reference:** Glasgow's combined 42 MB/s USB figure is correctly
  treated as inadequate evidence for a particular 40 MB/s raw-capture mode,
  especially with other work and mode-specific resource constraints. The
  current analyzer maturity qualifications remain intact.
- **Analog/RF:** A1/A2/R1 require actual converters and conditioning rather than
  obtaining voltage/IQ from FPGA GPIO. ADC resolution versus stored width,
  bandwidth versus sample rate, delivered-stimulus reference plane, independent
  observation and output-state transitions are all distinguished. Selecting
  anti-aliasing, converter interfaces, channel aperture/skew, input limits and
  source loads belongs in the next actual frontend specification.

Recommended disposition: retain the comparison and proposed partition; address
M1/L1 in the acquisition contract, then continue concrete workload, pin, clock,
memory and transport budgets. FPGA timing closure, memory controllers, analogue
performance and real-host endurance remain later qualification, not results
established by this document review.

## Revision disposition — 2026-10-15

Bounded recheck of revised ACQUISITION.md against M1/L1; no additional research
or implementation review. Original findings above are preserved.

- **M1 addressed and closed at this design maturity.** “Acquire and report”
  now distinguishes uncontrolled observation, throttleable protocol waits and
  timed stimulus. It requires independent time/index accounting or explicit
  unknown timing for stalls, forbids interpreting successful FIFO-write count
  as elapsed time, and defines underrun handling and invalid stimulus/reference
  relationships. “Independence and contention” now budgets intermediate FIFO
  headroom against maximum memory-service interruption, with corresponding
  qualification questions. Exact mechanisms remain engine-specific later work.
- **L1 addressed and closed at this design maturity.** Results now identify
  clock/reference, applied divider/schedule, nominal versus inferred versus
  measured/calibrated rate, and known or unknown accuracy/drift/jitter. The text
  explicitly distinguishes fractional-divider average rate from equal adjacent
  intervals and requires qualification or nonuniform time representation.

No outstanding hardware-review finding remains for this revision. Continue the
proposed complete-path budgets and block design; these resolved contracts do not
establish measured engine, frontend, memory or host performance.
