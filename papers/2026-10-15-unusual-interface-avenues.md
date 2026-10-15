# Unusual interface avenues: find the interaction boundary

2026-10-15. Frumentarii research for r1337, read against the current architecture,
capability matrix and stash. This is an exploration of mechanisms and experiments,
not a selected build, procurement list or permission to stimulate equipment. No
device was operated. Established niche techniques below are distinguished from
our proposed combinations; this research cannot establish what “everybody misses.”

The most promising expansion is a service instrument that can **find, preserve
and test an interaction boundary**, including boundaries that do not resemble a
data connector. Several especially useful boundaries are light, supply current,
excitation-dependent transducers, startup timing, and the human control panel.
The transferable investment is protected analog acquisition/stimulus, local
timing and physical fixtures. More protocol names or radios alone do not supply
these abilities.

## Four different accomplishments

This is our synthesis, not a hierarchy claimed by the papers:

| Accomplishment | Example | What remains unproved |
| --- | --- | --- |
| Find an intended channel | Identify a documented optical readout or programming interface | Its electrical compatibility, current enablement and command semantics |
| Measure a correlated observable | A magnetic burst accompanies a motor movement | The burst's cause, exact position or success of the operation |
| Establish a stimulus-response relationship | A known optical modulation produces a repeatable detector response | A unique internal model, general behavior outside the experiment |
| Obtain verified control | A bounded action produces independently observed expected state | Behavior in other modes, on restart, or after communications failure |

An instrument should keep the original waveform, decoded candidates, observed
state and proposed explanation separable. A decoder emitting plausible bytes is
not an identity oracle. A recognizable correlation is not an acknowledgement.
An actuator completing its motion is not equipment completing its task.

## 1. Optical heads can find intended ports and observe status

**Established examples.** TI's TIDUCF0 describes an IrDA physical-layer optical
port for meter readout/configuration. An unusual implementation uses the same IR
LED for emission and reception; the demonstrated implementation uses CC1350/
CC1310-era hardware at 9600 bps. Its spectral response and receive method matter.
The document also distinguishes traditional two-element optical arrangements;
it does not establish that an arbitrary front-panel LED can receive commands.
Neither this hardware nor its software has been demonstrated on the stash's
CC1312R1 boards. [TI reference design, especially §§1–2](https://www.ti.com/lit/ug/tiducf0/tiducf0.pdf)

**Our opportunity.** A retained optical probe with controlled alignment, an
ambient-light shroud, interchangeable emitter/detector geometry and a raw
detector output could serve three distinct experiences: documented maintenance
ports, precise observation of indicator timing, and controlled reflectance/
interruption tests. Preserve raw optical timing before attempting a framing
interpretation. Offer a separate demodulated remote-control path only when that
is the intended signal class; its output can discard carrier and pulse details
that a different optical protocol needs.

An integrated camera helps locate a window and read its labels. A locally sampled
photodetector addresses edge timing; camera exposure/frame cadence is a different
measurement path. A simple clip or probe rest may contribute more than an
elaborate computer-vision model by keeping distance and angle stable.

**Negative cases and discriminating experiment.** A dark window may have a
different wavelength, be disabled, or only respond in a documented service mode.
No light is weak negative evidence. On an identified, documented low-voltage
counterpart, compare known transmitted timing with the raw detector capture;
then change ambient light and alignment. A successful test establishes that
specific optical head/geometry and signal class, not generic optical access.

## 2. Power wires and current loops may carry another conversation

**Established examples.** TI's HART input reference separates a DC loop-current
measurement path from an AC-coupled modem path for 1200/2200 Hz FSK. Reading
the process current and decoding the digital overlay are different operations.
[TI TIDUEG0, §§2.1–2.2](https://www.ti.com/lit/ug/tidueg0/tidueg0.pdf)
More surprisingly, PGA300 provides a calibration/configuration interface on its
power-supply pin. It requires a specified activation sequence and operating-mode
transition; the target does not spontaneously transmit until commanded.
[PGA300 datasheet Rev. D, §§6.4–6.5](https://www.ti.com/lit/ds/symlink/pga300.pdf)

Legacy carrier-current systems add another timing relationship: Microchip's
historical X-10 note describes carrier bursts synchronized to AC zero crossings.
This is an example of information riding a power network, not a suitable generic
GPIO coupling circuit for r1337. Its mains-referenced implementation is not
adopted here. [Microchip AN236](https://ww1.microchip.com/downloads/en/AppNotes/00236a.pdf)

**Our opportunity.** Treat “power connector” as a hypothesis about a boundary,
not proof that only DC is present. A future protected frontend could retain DC
level and small AC variation separately, with explicit bandwidth, loading and
common-mode limits. Identify whether it is observing an existing powered loop,
providing loop power, measuring current, or emulating a transmitter. These are
different roles, and the architecture's composed return/power map applies.

The strongest experimental question is narrow: *does this identified interface
carry a documented overlay in this mode?* Establish that on a known counterpart
before interpreting unexplained ripple. Switching-regulator noise and deliberate
communications can look similar in a spectrum. A silent PGA300-like interface
would not refute its existence because activation changes the measurement state.

**Limits.** A historical 20 mA serial loop is not automatically a 4–20 mA analog
loop; a two-wire sensor is not automatically HART; a supply-modulation interface
is not Dallas 1-Wire. Mains carrier-current requires its own rated coupling and
isolation design. None of those frontends is conferred by a BP5 GPIO, Flipper
pin, scope input or a common connector.

## 3. Maintenance access may be a temporal state rather than a live console

**Established examples.** ST's SWIM manual specifies an activation sequence and
describes interactions with reset and multiplexed pins. Microchip documents
UPDI as a bidirectional half-duplex single-wire programming/debugging interface.
These are intentional maintenance paths, but neither should be treated as an
always-running UART console. [ST UM0470 Rev. 4, §§3–4](https://www.st.com/resource/en/user_manual/cd00173911-stm8-swim-communication-protocol-and-debug-module-stmicroelectronics.pdf),
[Microchip UPDI physical interface](https://onlinedocs.microchip.com/oxy/GUID-9D10622A-5C16-4405-B092-1BDD437B4976-en-US-4/GUID-9B349315-2842-4189-B88C-49F4E1055D7F.html)

**Our opportunity.** Make startup a first-class capture context: supply behavior,
reset, candidate signal transitions, visible indicators and operator actions on
one session timeline. An identified MCU and its exact documentation may turn an
apparently inert pad into a meaningful experiment. Pogo fixtures, reversible
connectors and known reference grounds are reusable assets; trial-driving every
pad is a poor substitute for identification.

Separate passive observation of normal startup from entry into a boot, test or
debug state. The latter can stop execution, change pin ownership or expose
state-changing commands even when the eventual goal is reading. A documented
activation sequence is part of the device profile and recovery model, not a
universal discovery waveform. Hidden maintenance also includes service keys,
straps and panel sequences; those require model-specific evidence.

**Experiment and negative case.** After identifying an actual stash/lab subject,
compare its documented startup/maintenance states with locally timestamped
observations. Begin with recording an operator-performed normal startup under a
later reviewed plan. Lack of an idle waveform says little about an interface
that only talks after activation. Valid-looking serial output can still be an
unrelated multiplexed function. Protection/locked access remains a legitimate
terminal result, not a prompt to invent more aggressive activation.

## 4. Analog transducers and encoded physical media are interfaces too

**Established examples.** TI's resolver note describes an excitation carrier and
two angle-dependent amplitude-modulated outputs, then synchronous demodulation.
That is a measurement conversation with a passive electromechanical device.
[TI SBAA144, pp. 1–4](https://www.ti.com/lit/pdf/sbaa144)
But demodulation is model-specific: ADI's AD598 LVDT circuit processes a ratio of
secondary magnitudes without synchronous detection. Its difference/sum method
can become nonlinear on LVDTs that do not meet the required sum relationship.
[ADI CN0288](https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/cn0288.html)

**Our synthesis: classify by the missing frontend, not by connector count.**

| Interface family | Reusable machinery worth studying | Additional condition / negative case |
| --- | --- | --- |
| Strain/pressure bridges | Differential low-noise measurement, measured excitation/reference, force/sense wiring | Excitation, common-mode range, bridge completion and transfer calibration; voltage alone is not force/pressure |
| RTD/resistive sensors | Controlled current, differential measurement, Kelvin connections, reference resistor | Lead resistance, sensor type and self-heating; an unknown resistor is not a thermometer |
| Thermocouples | Low-offset voltage path plus connector-temperature measurement | Correct thermocouple type, cold-junction compensation and thermal layout; instrument internal temperature is not necessarily connector temperature |
| Analog voltage / 4–20 mA process signals | Protected voltage/current paths, known shunt and load, isolation where required | Source/sink/powered-loop roles, compliance and burden; digital overlay is separate |
| Pulse/frequency, quadrature and index | Conditioned inputs, counters/edge timestamps and simultaneous channels | Open-collector/differential/current outputs need actual adaptation; frequency needs a scale, quadrature direction needs channel relationship |
| Resolver / LVDT / synchro candidates | Known excitation, simultaneous analog responses, ratio/phase processing | Device-specific wiring, carrier, drive/load and transformation; not every coil assembly is interchangeable |
| Magnetic stripe or other magnetic media | Suitable contact head, low-noise AC amplification, waveform/timing capture and mechanical guide | Read geometry and encoding matter; observing flux transitions does not establish a general tape/floppy reader or a writer |
| Optical code/disc/scale | Illumination, focus or optical head, controlled travel, timing or imagery | Absolute code, incremental count and printed identifier are different interpretations; resolution and contrast bound recoverable detail |

The bridge and wiring distinction follows [ADI's transducer-excitation note](https://www.analog.com/en/resources/analog-dialogue/articles/transducer-sensor-excitation-and-measurement-techniques.html).
RTD current, lead and self-heating tradeoffs follow [ADI's RTD system note](https://www.analog.com/en/resources/technical-articles/2022/07/16/12/06/rtd-measurement-system-design-essentials.html).
Thermocouples produce a small voltage without excitation and require a reference
junction at a measured, appropriate temperature; see [Jim Williams, AN28](https://www.analog.com/en/resources/app-notes/an-28f.html).
TI distinguishes optical and magnetic quadrature implementations in
[SBOA200](https://www.ti.com/document-viewer/lit/html/SBOA200).

Microchip's magstripe reference is particularly instructive: it amplifies magnetic
head waveforms, detects peaks and retains their timing before F2F decoding. The
UART is the decoded-data output, not the magnetic sensing frontend. This
distinction applies widely: a convenient host interface can hide the actual
transduction and clock recovery. [Microchip card-reader guide, §§2–4](https://www.microchip.com/content/dam/mchp/documents/OTH/ProductDocuments/MISC/Magnetic%20Card%20Reader%20User%20Guide.pdf)

**Proposal.** Inventory a few actual lab transducers/encoders and their original
readouts before deciding which frontend families deserve portable coverage.
Unknown analog hardware can be a valuable subject or bench fixture without
entering the portable body. An identified bridge or encoder offers a better
first test than a mystery high-power industrial connector. Start with a known
reference response and measure the effect of wiring/load changes; do not claim
engineering units until transfer and reference conditions are established.

## 5. Repeatable multi-physics observations can expose operational state

**Established examples.** Near-field H/E probes can locate local emissions, but
ordinary EMI-debugging probes support relative measurements rather than absolute
emission-limit verification. [Rohde & Schwarz, §6.3](https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_common_library/dl_brochures_and_datasheets/pdf_1/Educational_Note_-_Understanding_EMI_Precompliance_Testing.pdf)
Synthetic Sensors combines multiple physical measurements to classify demonstrated
events. The study explicitly used labels and null examples; its two-hour noisy
observation still produced 13 false triggers. It is evidence for useful
context-dependent sensing, not automatic semantic understanding of arbitrary
equipment. [Laput, Zhang & Harrison, CHI 2017, evaluation](https://chrisharrison.net/projects/syntheticsensors/syntheticsensors.pdf)

**Our opportunity.** Pair a repeatably positioned H-field loop or capacitive
pickup with contact vibration, optical status and a current observation where
accessible. Ask whether the equipment is in a particular *observed operational
state*: motor active, repeated retry, power cycling, relay actuation, fan-speed
change. The reusable asset is a probe fixture and a comparison protocol. Relative
observations can be valuable without promising decoding or calibrated radiometry.

Use the instrument's own screen, fan, converters, storage and radios as explicit
confounders. Record operating mode; compare with the subject absent/off where
possible, displace/rotate the pickup, and repeat across different sessions. A
signal that survives arbitrary target changes but follows host activity is an
instrument problem, not a breakthrough about the subject. Contact vibration
depends on mounting force and location; capacitive pickup depends on nearby
conductors and operator position. A scan is not automatically a map of internal
parts, and an emission signature is not proof of firmware identity.

**Experiment.** On an identified stash counterpart, collect normal idle/action
transitions with operator labels and independent visible readback. Hold out an
entire later session, including reattachment and no-action periods, when judging
a proposed detector. Test a specific distinction and its false-trigger behavior;
do not lead with a classifier trained on adjacent windows of the same capture.

## 6. Deliberate, coded excitation can make a weak interaction measurable

**Established techniques.** A lock-in uses a stable frequency/phase reference to
measure the corresponding response component, trading detection bandwidth for
noise rejection. Its result is that component, not the full waveform's peak
amplitude. [SRS, Lock-In Amplifier Basics](https://www.thinksrs.com/downloads/pdfs/applicationnotes/Lock-In%20Basics.pdf)
SweepSense demonstrates reflected acoustic sweeps for configuration sensing on
particular earphones and a laptop. The authors require training and explicitly
identify device dependence and acoustic-leakage limitations.
[Laput, Chen & Harrison, IUI 2016](https://chrisharrison.net/projects/sweepsense/SweepSense.pdf)
Touché demonstrates swept-frequency capacitive sensing of touch configurations.
[Sato, Poupyrev & Harrison, CHI 2012](https://la.disneyresearch.com/publication/touche-enhancing-touch-interaction-on-humans-screens-liquids-and-everyday-objects/)

**Our opportunity.** Treat the generator, reference and response channels as a
reusable experiment engine. The exciter might be an LED, low-energy electrical
source, acoustic transducer or contact piezo; each needs its own appropriate
driver/coupling. The response might be optical, electrical or mechanical.
Coherent electrical paths also support the impedance/network work researched in
parallel, without assuming an audio detector becomes an RF receiver.

There are two different goals. A small-signal transfer measurement asks for
gain/phase under stated operating conditions and checks whether the system is
approximately linear/stationary there. A configuration classifier asks which
previously demonstrated state best explains a response. A sweep that separates
two states need not identify the physical object, recover hidden geometry or
remain valid when mounting changes.

**Experiment and negative cases.** First measure a known, deliberately simple
path on the bench: direct reference, response with subject, response with subject
removed/blocked, and changed coupling. Check that the measured feature follows
the intended path rather than emitter-to-receiver leakage. Vary stimulus within
the reviewed limits to expose saturation/nonlinearity. Longer averaging cannot
recover an analog frontend that clips, an absent coupling path, or a response
that changes faster than the estimator. Phone/audio sample-rate labels do not
establish useful ultrasonic emitter/microphone bandwidth. No universal
through-case ultrasound or capacitive tomography claim follows from these demos.

## 7. The physical panel may be the best documented control API

**Established example.** RetroFab combines scans/annotations, fitted structures,
actuators and light sensors to retrofit basic physical interfaces. Its limitations
include small controls, actuator size/force and placement immediately in front of
controls. Cameras and more complex display interfaces are future work in that
paper, not demonstrated general visual control. [Ramakers et al., CHI 2016](https://www.research.autodesk.com/app/uploads/2023/03/retrofab-a-design-tool.pdf_recq46gvQ9Haa6erl.pdf)

**Our opportunity.** For old equipment with no useful digital port, a tailored
panel fixture may be more tractable than firmware replacement: read an indicator
optically; turn a documented control through a bounded range; press one control
and verify the visible result. Camera assistance can start with inspection,
operator-guided annotation and before/after records. Proposed visual automation
requires its own review and success criteria.

Use a per-device fixture and state model. Account for backlash, slipping knobs,
switch detents, screen glare, multiplexed displays, modal menus, covers and local
operator intervention. Position feedback reports actuator position; equipment
readback reports the controlled state. Neither substitutes for the other. A beep
or lit button can precede a failed process. If a command's outcome is unknown,
do not repeat the physical action merely because the network reconnects.

**Physical fit.** A core-mounted camera/probe rest or a stored precision head can
support field assessment. Persistent lab fixtures/gateways can remain attached
to understood equipment; they are infrastructure, not extra carried companions.
This does not propose a general robotic arm inside the service monitor.

**Experiment.** Select one identified, noncritical panel with clear independent
readback. Compare human operation with a proposed fixture's accessible control,
alignment, force and readback geometry before building automation. A good result
may be a passive optical reader and better operator instructions rather than a
motorized solution.

## 8. Timing and sideband events can be more useful than payload decoding

**Established example.** GPIB has asynchronous SRQ requests, EOI message
termination and interlocked handshake signals as well as data. The NI manual
also explains serial polling to discover which device requested service. Bus
management operations such as interface clear or remote enable change behavior;
they are not passive discovery. [NI-488.2 historical manual, chs. 1 and 7](https://download.ni.com/support/manuals/370904a.pdf)

**Our opportunity.** Capture event relationships before pursuing every byte:
panel action → ready/contact line → current change → emission burst → visible
completion. This can answer “where does the workflow stall?” even when the
protocol remains partly unknown. It also helps distinguish a command queue from
the physical operation it initiates. Rare-event/pretrigger capture is a useful
system capability for this purpose.

Keep a local sample-clock basis, explicitly measured trigger relationships and
uncertainty between independent instruments. Host arrival times, camera frames,
PTT annotations and remote transcripts have different temporal precision.
Narration is valuable context, not a precise electrical event marker. Correlated
events may share an unobserved cause; causal claims need a reviewed intervention
or independent model, not merely a cross-correlation peak. Don't clock every
instrument from a remote service or assume ordinary USB timestamps establish
phase coherence.

## How these avenues should influence detailed design

These are design implications proposed by this report, not newly verified
capabilities of the inventory:

1. **Specify a family of frontend roles.** Protected differential voltage/current,
   high-impedance pickup, photodetector, contact acoustic and conditioned digital
   inputs have different loading/noise/range needs. A common internal timing and
   session contract is plausible; a single undifferentiated “universal input” is
   not established. Keep exciter/loop-power/writer roles explicit and separately
   controlled.
2. **Make fixtures part of the instrument concept.** Retained probe heads, guides,
   shrouds, strain relief, known reference surfaces and repeatable alignment can
   turn one-off traces into useful comparisons. CAD can provide these without
   forcing every transducer into the enclosure. Keep the one-core/at-most-one-
   companion constraint and accessible articulated screen.
3. **Reserve local reference/trigger relationships.** Match analog response,
   conditioned edge timing and actual stimulus at the measurement plane. A
   waveform file name or a host “start” event does not prove what was emitted.
   Qualify output shutdown/loss/restart behavior through the existing architecture.
4. **Treat experiment recipes as structured knowledge.** Retain subject identity,
   current mode, wiring, fixture geometry, ranges, actual excitation, clock
   relationships, calibration state, raw response, operator action and negative
   cases. A remote colleague can suggest interpretations and discriminating next
   measurements while acquisition and control stay local.
5. **Keep breadth by reusing mechanisms.** An optical head serves status and
   intended data; a coherent analog engine serves transducers and system response;
   edge timing serves buses, encoders and event sequencing. Specialized carriers,
   exciters, physical heads and device semantics still remain real gaps.

## Stash-first experiments to choose after subject identification

No experiment below has been performed or selected for execution. AD3 remains
bench-only, useful as a reference within its actual ranges. CC1312 pairs, the
Freenove board, Flipper and eventually SLogic can be controlled counterparts or
timing subjects once their exact interfaces and plan are established. Their
presence does not fill the analog/probe gaps by itself.

| Question worth answering | First suitable counterpart | Direct discriminating observation | Named gap to resolve before a proposal |
| --- | --- | --- | --- |
| Can an optical head preserve this timing under field alignment? | Identified optical emitter/receiver or documented meter port | Compare emitted/reference and received waveform while changing light/alignment | Detector/driver bandwidth, spectral response, shroud and reference timing |
| Can a panel's operational states be observed without a data port? | Identified low-voltage motor/fan/indicator subject | Independent visible state plus current/EM/vibration; later session and null trials | Actual probes, frontend ranges and repeatable mounting |
| Can analog infrastructure be reused rather than replaced? | Identified lab bridge, encoder or temperature probe and original readout | Compare with a known reference while varying one physical input | Pinout/excitation, units, termination and reference instrument |
| Is an intended service path silent or absent in normal operation? | Known MCU/board with exact maintenance manual | Normal startup capture and documented state distinctions | Recovery/entry plan, electrical adapter and local sequencing |
| Can controlled excitation separate a useful state? | Simple known optical/acoustic/electrical bench path | Subject/bypass/blocked-path comparisons and repeated attachment | Exciter/receiver coupling, reference channels and permitted operating range |
| Can a physical UI bridge reliably observe completion? | One identified panel with unambiguous readback | Equipment readback independent of actuator motion | Fixture geometry, force/stops, state model and manual intervention handling |

## Literature gaps and corpus

Six original PDFs were acquired unchanged and selected sections read; their
source URLs, hashes, rights notices and restoration commands are in the
[lane acquisition manifest](2026-10-15-unusual-interface-acquisitions.md).
Other primary documents are linked at the relevant claims above. No reference
implementation or dependency was adopted or run.

The actual lab model manuals, transducer/encoder labels and existing cable/
probe identification are the main missing inputs. Obtain the applicable meter
optical-port specification or industrial physical-layer standard only after
identifying a subject; reference designs are not complete conformance standards.
If needed, operator acquisition of licensed IEC 62056-21/IrDA or IEEE 488 material
should follow that concrete need. No unavailable paper currently blocks this
conceptual research pass. Initial failed publisher/author URLs were replaced with
accessible primary copies, as recorded in the manifest.
