# Bus Pirate 5 possibilities — 2026-10-15

## Identification and scope

The operator found a device marked approximately “genuine bus 5 5 pirate.”
**Bus Pirate 5 is the working identification**, with board revision, installed
firmware, accessories and electrical condition still unverified. This pass read
primary documentation only. No device was connected, operated, updated or tested;
no tools, libraries or source archives were installed or executed. The proposals
below preserve the current discussion-first direction.

## Its useful contribution

Bus Pirate 5 provides a wired interface and electrical observation surface that
complements the radio-oriented inventory. Its documented platform uses a dual-core
RP2040 at 125 MHz with PIO, eight bidirectional buffered IOs, per-pin voltage
measurement and configurable pull-ups. A Pi or other suitable USB host could
ask it to interrogate an I2C/SPI/UART/1-Wire peripheral while collecting the bus
result and power observations. This could help characterize the assorted modules
before deciding which belong inside a portable enclosure.
[Official BP5 specifications](https://docs.buspirate.com/docs/hardware/bp5rev10/introduction/).

The IO range is revision-sensitive. The overview says 1.65–5 V; the REV10 design
explains that its I-Core buffers support 1.2–5 V, while REV8 used TI parts rated
from 1.65 V. Until this board is identified, 1.2 V support is unestablished.
The VOUT/VREF connection either supplies the target rail or references the IO
buffers to an external rail. Per-pin voltage display uses an analog multiplexer;
it should be treated as electrical-state context, with acquisition timing and
accuracy characterized before making waveform claims.
[REV10 hardware design](https://docs.buspirate.com/docs/hardware/bp5rev10/hardware/).

## Power has three separate numbers

The current REV10 hardware design specifies **1–5 V target output, 300 mA
maximum**, with a **0–500 mA current-sense range** and **0–500 mA programmable
trip threshold**. A comparator/latch disables the regulator when the limit trips;
that threshold is not a promise of 500 mA continuous target power. The document
explicitly describes the threshold headroom as allowing current spikes.
[REV10 PPSU design](https://docs.buspirate.com/docs/hardware/bp5rev10/hardware/#programmable-power-supply-unit).

Older official REV8 and firmware-reference pages instead state a 400 mA rated
maximum. That is a documentation/revision discrepancy to resolve against the
actual board, rather than selecting whichever number is larger. In a portable
system the PPSU is a candidate supply for a small module under examination; the
Pi, hotspot and other system loads need their own power budget.
[REV8 design](https://docs.buspirate.com/docs/hardware/bp5rev8/hardware-rev8/),
[older firmware command reference](https://firmware.buspirate.com/command-reference/commands).

## Logic capture: distinguish BP5 from BP6

Current logic documentation lists eight channels, up to 62.5 MS/s and a 131K-sample
buffer, with follow-along capture triggered by bus activity. These are bounded
captures; a sample-rate figure alone does not establish continuous USB streaming.
Crucially, BP5 lacks BP6's second observation buffer. During driven outputs the
analyzer observes the MCU side of the IO buffer, so it can report a level that
differs from the external bus pin. Input-only analyzer use avoids that specific
topology limitation. For independent confirmation of a driven waveform, a second
observer on the external bus remains a useful conceptual role. The auxiliary
connector provides physical access for such equipment.

The same logic page lists a pin trigger in its capability summary but later says
the terminal `logic` command currently supports automatic follow-along capture
only. Treat modes and trigger capabilities as firmware-specific until identified.
[Logic command and topology caveat](https://docs.buspirate.com/docs/logic-analyzer/logic-command/),
[auxiliary connector](https://docs.buspirate.com/docs/hardware/bp5rev10/hardware/#auxiliary-io-connector).

## Automation is available, with distinct interfaces

Current documentation describes an interactive terminal on one USB CDC serial
interface, binary control on another, and USB mass storage. For new automation,
BPIO2 is the documented structured interface: FlatBuffers requests/responses,
COBS framing, version negotiation, status queries, mode configuration and bus
transactions. Those are external protocol facts; choosing a client implementation
or dependency would be a later design discussion. The actual installed firmware
may predate this interface.
[USB communication guide](https://docs.buspirate.com/docs/development/experimental/usb_communication_guide/),
[BPIO2 reference](https://docs.buspirate.com/docs/binmode-reference/protocol-bpio2/).

Legacy BBIO/raw-SPI compatibility is a separate mode aimed at Flashrom/AVRdude.
The modern menu labels it experimental, and its detailed page says its own
documentation is inaccurate/incomplete. An older script written for BP3 therefore
needs explicit compatibility checking. Local macros, scripts and button assignment
offer another way to package repeated operations.
[Legacy interface caveat](https://docs.buspirate.com/docs/binmode-reference/protocol-spi-legacy/),
[command and scripting reference](https://docs.buspirate.com/docs/command-reference/).

## USB, display and portable roles

The documented USB configuration makes BP5 a **USB device** connected to a host.
A Pi with an appropriate USB host port is a plausible controller; two USB-device
ports cannot be assumed to talk directly. Its USB connection also supplies board
power, so host/hub capacity and target PPSU load belong in the later power tree.
The documented `usbpd` function uses an **external AP33772S adapter**; it does
not establish built-in PD negotiation or a high-voltage supply on this BP5.
[USB guide](https://docs.buspirate.com/docs/development/experimental/usb_communication_guide/),
[USB-PD adapter command](https://docs.buspirate.com/docs/command-reference/#usbpd-usb-power-delivery-with-ap33772s).

BP5 already has a 320×240 IPS display for pin labels, voltage and current, plus
one button. Flipper's 128×64 monochrome screen and multiple controls serve a
different interaction pattern. Keeping BP5's local electrical readout visible
while another device handles radio views, notes or richer control is one possible
division of work; replacing either UI is not required to explore it.
[BP5 LCD](https://docs.buspirate.com/docs/hardware/bp5rev10/introduction/#lcd),
[Flipper display specifications](https://docs.flipper.net/zero/development/hardware/tech-specs).

A standalone button-driven fixture is another possibility, but firmware matters:
in May 2026 the maintainer traced operation without a USB host to a filled text
output queue and announced an autobuild fix. This pass did not verify its release
or this unit's behavior. A USB power bank alone should therefore remain an
unverified standalone arrangement.
[Maintainer's investigation](https://forum.buspirate.com/t/using-the-bus-pirate-5-without-a-usb-host/1476).

The clearest discussion options are a removable wired-bus module managed by a Pi,
a visible bench companion to the Flipper/ESP radio nodes, or a narrow local
fixture for one repeated task. Exact revision, firmware and intended workflow
should determine which, if any, becomes part of the portable system.

The newly mentioned industrial-control bin strengthens the identification and
characterization role. Controller model, pinout and electrical interface must
come first: connector shape alone does not identify TTL UART, RS-232, RS-485,
CAN or operating voltage. Any required transceiver/isolation belongs between
the identified controller and BP5's buffered GPIO, as a later explicit design.
