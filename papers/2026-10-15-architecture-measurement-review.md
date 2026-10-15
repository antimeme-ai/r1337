# Architecture review: measurement, electrical paths, timing and data

Reviewer: hardware/instrument frumentarii. Date: 2026-10-15.

Reviewed the first versions of [ARCHITECTURE.md](../docs/ARCHITECTURE.md)
and [CAPABILITIES.md](../docs/CAPABILITIES.md), with current AGENTS/doctrine,
brief, inventory, issue index and relevant research reports. This judges a first
system architecture, not a finished schematic or performance specification.
No new acquisition, source execution or device work was needed. Section names
are the stable references; line numbers below refer to the reviewed text.

## Assessment

The proposed partition is technically credible at this maturity. There is no
identified blocker to continuing requirements, block schematics and geometry
studies. No assigned board is claimed to supply an unsupported measurement
class. The architecture appropriately leaves the portable scope/AWG and RF
network assembly unresolved, treats AD3 as bench equipment, and makes host and
frontend suitability conditional. Two medium findings need architectural
behavior defined before a prototype plan; one low finding improves RF coverage
requirements. None requires selecting components or narrowing the brief to a
single application.

## M1 — Medium: capture completeness and overruns have no explicit contract

**Section:** Architecture, “Timing, storage and remote support,” lines 184–205;
capability matrix, “Digital observation,” “Voltage versus time,” and “Raw RF/IQ
and spectrum observation.”

**Practical failure:** The design retains originals and budgets throughput, but
does not state what happens when a device FIFO overruns, a transport loses blocks,
storage stalls, or acquisition stops partway through a requested record. A file
can be an original byte-for-byte capture while still containing unreported gaps.
A rendered waveform could then imply a continuous interval that was never
observed; intermittent-fault analysis could mistake a recorder gap for silence.
This is especially relevant when a Pi/hub path cannot sustain the requested
stream, even though the local acquisition engine continues sampling.

**Evidence:** The architecture already distinguishes bounded acquisition from
streaming and computes 800 MB/s for packed 32-channel/200 MSa/s data. That
calculation is correct. The [ESP32 SDR report](2026-10-15-esp32-sdr-reconnaissance.md)
documents a concrete external protocol with sample indices and gap flags, and
shows how a live FFT can skip acquisition windows. The
[portable-system report](2026-10-15-portable-system-possibilities.md) explicitly
calls for overrun/incomplete-capture reporting. This finding carries that
existing research requirement into the architecture; it does not propose a
second validation system.

**Proposed resolution:** Add one instrument-recording rule: declare whether each
mode is bounded capture, continuous samples or decoded events; preserve source
indices/sequence information when available; retain discontinuity, overrun,
truncation and completion state; and expose unknown completeness when the device
cannot report it. Decide whether a mode stops, reduces offered work, or records
gaps when buffers fill. Do not silently stitch intervals. Bounded capture must
fit a known local buffer and report whether trigger/acquisition/retrieval
completed; it is not a general substitute for an unbounded data path.

## M2 — Medium: autonomous stimulus needs defined output behavior on failure

**Section:** Architecture, “Functional boundaries,” lines 75–78, “Power, noise and
operating modes,” lines 168–180, and “Timing, storage and remote support,” lines
206–210; capability matrix, “Electrical waveform stimulus” and “Vector/scalar
network response.”

**Practical failure:** Local engines correctly own waveform timing and target
transactions, so a host stall or disconnected control channel need not stop an
engine. The design does not assign responsibility for what a running generator,
RF source or target power output does when cancellation is requested, the host
restarts, an engine loses configuration, or orderly shutdown begins. An output
can continue stimulating a target while the UI has stopped reporting its state.
Conversely, indiscriminately switching off every rail can interrupt an operation
whose completion state is already unknown. The remote retry rule addresses
duplicate dispatch but does not resolve these electrical states.

**Evidence:** The architecture deliberately gives the supervisor shutdown
coordination and local engines waveform execution. The
[analog/control report](2026-10-15-analog-control-frumentarii.md) identifies local
cancellation as a useful interface pattern. The
[BP5 report](2026-10-15-bus-pirate5-possibilities.md) shows that target power and
trip behavior are their own electrical mechanisms, not consequences of host
application state. No particular failure behavior has been demonstrated on the
owned units.

**Proposed resolution:** State that each stimulus/target-power mode declares
its armed/running/terminated/unknown states and its output policy on normal
completion, cancellation, control-link loss, engine reset and host shutdown.
Assign which local component enforces that policy and how actual output state
is shown after recovery. Use policies appropriate to the mode rather than a
universal disconnect action. Reference this requirement in the later frontend/
supervisor block design; no interlock circuit or implementation is selected here.

## L1 — Low: raw I/Q access and spectrum measurement need separate coverage

**Section:** Capability matrix, “Raw RF/IQ and spectrum observation”; architecture,
“What the instrument does,” lines 29–32 and “What remains to resolve,” line 243.

**Practical failure:** The combined row can eventually be marked covered by an
ESP burst receiver plus FFT while the emission-inspection workflow still lacks
the required frequency span, level interpretation or probability of observing a
short event. The current text does not make that false claim, so this is a
requirements ambiguity rather than an incorrect hardware assignment.

**Evidence:** The [instrument report](2026-10-15-weird-instruments-frumentarii.md)
distinguishes wideband I/Q, swept power and complex network response. The
[ESP32 report](2026-10-15-esp32-sdr-reconnaissance.md) distinguishes internal
sample rate, actual passband, exported rate and capture duty. A wide tuning
range, a plotted FFT, and absolute RF level accuracy are separate properties.

**Proposed resolution:** Separate raw waveform access from spectrum observation
in the requirements, either as two rows or explicit submodes. For spectrum add
instantaneous span versus swept coverage, resolution bandwidth/window/detector,
update time and dead time, relative versus calibrated level, and overload/spurious
response conditions. This does not select a dedicated spectrum-analyzer board;
one physical frontend can cover several modes when justified.

## Boundaries already handled correctly

- **Board roles:** BP5 is a candidate controller, not a general scope or an
  independent observation of every driven pin. The expected SLogic is conditional,
  with no optional analog accessory assumed. CC1312R1 packet access is explicitly
  separated from general I/Q. Classic ESP32 research is not assigned newer-chip
  continuous modes. Flipper dock/host usefulness must still be established.
- **Measurement classes:** An AC-coupled power/EM trace frontend is explicitly
  distinguished from a general scope; VNA/SNA reuse is conditional; thermal,
  acoustic, ultrasonic and optical observables are not presented as equivalent
  images of an enclosure interior. These distinctions match the acquired reports.
- **USB arithmetic:** 32 × 200,000,000 bits/s divided by eight is 800,000,000
  bytes/s before framing. The document labels this illustrative, does not
  mistake link marketing rate for sustained payload, and does not promise every
  SLogic maximum on a Pi. Host-controller/storage selection remains a valid next
  input rather than an architecture error.
- **Timing:** Shared sessions, host timestamps and hardware clocks are kept
  separate. A common trigger alone does not remove subsequent clock drift, and
  a shared frequency reference alone does not establish sample-start phase.
  The existing requirement for supported/measured cross-instrument alignment
  should carry these distinctions into individual engine specifications.
- **Electrical compatibility:** The frontend boundary explicitly owns voltage,
  coupling, termination and grounding/isolation; industrial protocol names do
  not stand in for transceivers. Nothing claims the unidentified controllers
  can be connected directly to buffered GPIO.

## Next design questions, not additional defects

The following should be answered in the next block-design work rather than
treated as missing finished schematics in this first pass:

1. Draw the electrical domains and return paths for USB grounds, chassis,
   scope/AWG returns, RF connector shields and target power. State which inputs
   can share a target reference and where differential capability or isolation
   is intended. Separate grounds on a block picture do not establish isolation;
   USB connections can join them elsewhere. Preserve this topology when choosing
   front-panel connectors and probe storage.
2. Define useful acquisition operating points alongside maxima: channels,
   representation, duration/depth, trigger rate and acceptable dead time. Map
   concurrent modes to actual host controllers, hubs and storage once the Pi is
   identified. Preserve lower-rate/bounded modes that remain useful on the stash.
3. Carry RF/analog reference planes to the actual front-panel cable paths.
   Internal coax, switches, protection and adapters can alter loss, phase,
   matching, noise and usable bandwidth. A source/receiver assembly calibrated
   at its PCB connector is not automatically calibrated at a new panel connector.
4. Specify source levels/loads and scope differential/common-mode/input limits
   before sharing analog hardware or RF ports. Select verification fixtures and
   bench comparisons for those specific claims; possessing AD3 or ham equipment
   does not establish coverage for an unspecified RF measurement range.

Review scope was documentation and already-acquired research, including the
analog/control, BP5, portable-system, ESP32 SDR, weird-instrument and closed-case
sensing reports. No assertion here establishes measured performance of an owned
unit. Recommended disposition: retain the proposed architecture, address M1/M2
and clarify L1, then continue the stated measurement requirements and block
schematics before an implementation/prototype plan.

## Revision disposition — 2026-10-15

Re-read the revised architecture and capability matrix against M1/M2/L1 only;
no repeat source research or device checks. Original findings above are retained
as the record of the first draft.

- **M1 addressed at first-architecture maturity.** “Timing, storage and remote
  support” now declares bounded/continuous/event modes, complete versus
  gapped/truncated/unknown data, available source indices and reset continuity,
  engine overflow versus host retrieval/storage failures, full-buffer policy,
  bounded-buffer fit and trigger/acquisition/retrieval completion. It prohibits
  silently stitching intervals and makes recording indication reflect confirmed
  or unknown state. Concrete formats and buffers appropriately remain later work.
- **M2 addressed at first-architecture maturity.** “Power, noise and operating
  modes” now assigns each output-capable engine/profile behavior for completion,
  cancellation, link loss, restart, standby, shutdown, low energy and restoration.
  It requires a capable local enforcement path, preserves unknown completion,
  distinguishes stop from power-off, and requires output/target-power state
  visibility and defined restart behavior. It does not claim that the supervisor
  controls an unconnected engine. Per-engine electrical implementations remain
  necessary before those behaviors can be offered.
- **L1 addressed.** The matrix now has separate “Raw RF/IQ access” and
  “Spectrum/emission measurement” rows. The latter explicitly covers span/sweep,
  update/interception/dead time, bandwidth/window/detector, relative versus
  calibrated level, overload and spurious response; an FFT display alone cannot
  establish coverage. No extra board is prescribed.

The matrix explicitly applies the architecture's shared behavior contracts
across its rows. All three findings are closed for this document revision;
component feasibility and verification remain the subsequent design work already
identified. No new finding arose within this bounded recheck.
