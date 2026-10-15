# Timing engines: source study for the acquisition design

Research date: 2026-10-15. Inputs to [ACQUISITION.md](../docs/ACQUISITION.md).
The operator directed that we proceed after discussing iCE40. Root interpreted
that as further system/block design within the current phase, not a selected
FPGA purchase, firmware replacement or hardware experiment. An optional question
requested actual Pi and representative lab-equipment model numbers; comparison
work proceeds without assuming an answer.

## Evidence and engineering consequences

### MCU peripherals and PIO

[Raspberry Pi's chip documentation](https://www.raspberrypi.com/documentation/microcontrollers/microcontroller-chips.html)
lists RP2040's SRAM, DMA, native peripherals, USB1.1 and two PIO blocks. The
[RP2040 datasheet](https://pip-assets.raspberrypi.com/categories/814-rp2040/documents/RP-008371-DS-1-rp2040-datasheet.pdf),
chapter 3 overview/programmer model at printed pp.311–313, describes four state
machines per block sharing 32 instruction slots. These are finite engines, not
unrestricted FPGA fabric. Shared SRAM/bus/DMA and the assembled board still
matter after a pin program fits.

The acquired official [PIO logic-analyzer example](https://github.com/raspberrypi/pico-examples/blob/0d62f75bafc2c8120d3276c3343d1a9195e909e9/pio/logic_analyser/logic_analyser.c)
uses a one-instruction sampling loop, packed FIFO words, DMA to a finite buffer,
an injected level wait, and later text output. It explicitly handles packing
when channel count does not divide 32 and clears FIFO/shift state when arming.
The demonstration uses two internally generated PWM signals and 96 samples.
It does not establish long, continuous, loss-qualified field capture, independent
pretrigger storage or accuracy on our hardware.

Engineering consequence: bounded PIO capture is a real implementation pattern;
its sample-clock ceiling is not an application performance specification.
We should compare actual pin programs, memory service, host drain and timing
error against the workload. The existing BP5's RP2040 already serves its own
firmware/frontends, so its silicon is not automatically spare engine capacity.

The earlier [TI/ESP report](2026-10-15-radio-module-possibilities.md) remains
the basis for stash MCU candidates. Classic WROVER peripherals and its actual
USB/UART bridge, TI local radio/application roles and S2 debug firmware are
different resources. No assumed Pico or RP2350 was added to inventory.

### Small FPGA resources versus board resources

[Lattice's UltraPlus table](https://www.latticesemi.com/Products/FPGAandCPLD/iCE40UltraPlus)
lists UP5K resources used in the design comparison. Its SPRAM and EBR have
different structures; total bits are not automatically one large dual-port FIFO.
The [earlier iCE40 note](2026-10-15-interface-measurement-methods.md#ice40-follow-up-small-fpga-as-a-local-engine)
records dated board prices and the broad assessment.

The current [iCEBreaker V1.1b maker listing](https://1bitsquared.com/products/icebreaker)
adds USB-C and 64 Mbit QSPI PSRAM. The [older hardware page](https://docs.icebreaker-fpga.org/hardware/icebreaker/)
instead describes V1.0-era connections, UART/programming and optional FTDI
async-FIFO wiring sharing GPIO. The optional path must not be assumed present
and qualified on a current board. Extra memory capacity is not its sustainable
write bandwidth.

[Olimex HX8K-EVB](https://www.olimex.com/Products/FPGA/iCE40/iCE40HX8K-EVB/)
lists external SRAM and programming/power/connectors. Those give a comparison
path; RAM timing and a programming interface do not establish an acquisition
host link. Engineering conclusion: compare a complete carrier/frontends/memory/
bridge/clock assembly, including pins consumed by those functions.

The [ECP5 manufacturer page](https://www.latticesemi.com/Products/FPGAandCPLD/ECP5)
was located as a growth-family reference, not a detailed part/board study.
No family-wide transceiver, memory-interface or host-rate guarantee is used.
Escalate only after the smaller complete paths fail a named requirement.

### Glasgow as a complete-path reference

Reused exact pinned source
d259cd44f643e9762b529f9e92b3c4ca758fe0aa from the
[existing acquisition manifest](2026-10-15-weird-instruments-acquisitions.md).
Additional read scope:

- docs/manual/src/revisions/index.rst: production/pre-launch distinctions and
  documented combined USB throughput;
- docs/manual/src/revisions/revC3.rst: relevant power, FX2/FPGA/translator,
  VIO sequencing and target-side connector sections;
- software/glasgow/gateware/iostream.py: initial signatures/buffer selection/
  latency paths through the first 160 lines;
- docs/manual/src/develop/applet.rst: missing stable applet API notice.

The [primary hardware description](https://glasgow-embedded.org/en/revisions/revC3.html)
shows a full engine's additional components. The source has explicit platform/
buffer latency handling; it is not evidence for zero-delay sampling. The
[revision guide](https://glasgow-embedded.org/en/revisions/index.html) documents
up to 42 MB/s combined USB throughput, not a per-mode guarantee on our host.
Do not reinterpret logic translation as galvanic isolation. Existing analyzer/
analyzer2 maturity distinctions remain in the earlier instrument report.

These patterns inform owned boundaries; no Glasgow/Amaranth code was adopted,
imported, built or run.

## Comparison assumptions and arithmetic

D1/D2/D3/A1/A2/R1 in the design are chosen engineering comparison workloads.
They are not recovered from an operator specification or claimed on a board.
Their purpose is to identify which decisions need actual target/host inputs.

Packed digital payload is channels × samples/second ÷ 8. Analog/IQ payload uses
the stated stored bytes per sample. Multiply by duration for record size.
Subtract existing memory allocations to obtain usable buffer capacity; sustained
rate mismatch consumes free memory at producer rate minus consumer rate.

A host's advertised USB generation, MCU clock, FPGA RAM bit count and a graph's
horizontal resolution do not substitute for those budgets. No data-rate test
was run. Numerical design calculations are checked directly from their inputs;
their physical feasibility remains a later qualification question.

## Acquisition and restoration

Retained one unmodified primary source file, not a source-repository archive:

- URL: https://raw.githubusercontent.com/raspberrypi/pico-examples/0d62f75bafc2c8120d3276c3343d1a9195e909e9/pio/logic_analyser/logic_analyser.c
- Upstream commit: 0d62f75bafc2c8120d3276c3343d1a9195e909e9,
  committer timestamp 2026-09-03T14:14:44Z.
- Path: quarantine/acquisition-engines/pico-logic-analyser-0d62f75bafc2c8120d3276c3343d1a9195e909e9.c
- Bytes: 6,693.
- SHA-256: 3188addd92a1a7949487b0226a9c619618170d3f8ec983b67193a279024bc205.
- Read all 159 source lines. Header: Copyright 2020 Raspberry Pi (Trading) Ltd.,
  SPDX BSD-3-Clause. No SDK/dependencies or repository-wide license files
  acquired; no code reuse selected.
- A single original file requires no source-tree extraction. No nested metadata
  or filesystem detritus is included.

Restore original only, from the repository root:

```sh
mkdir -p quarantine/acquisition-engines
curl --fail --location 'https://raw.githubusercontent.com/raspberrypi/pico-examples/0d62f75bafc2c8120d3276c3343d1a9195e909e9/pio/logic_analyser/logic_analyser.c' --output quarantine/acquisition-engines/pico-logic-analyser-0d62f75bafc2c8120d3276c3343d1a9195e909e9.c
shasum -a 256 quarantine/acquisition-engines/pico-logic-analyser-0d62f75bafc2c8120d3276c3343d1a9195e909e9.c
```

Compare with the hash above. Restoring the source does not build or execute it.

Original-manual download gaps:

- RP2040 datasheet: current pip-assets URL and legacy
  https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf returned HTTP403
  on direct download. Selected primary PDF text was readable in the web tool.
- iCE40 UltraPlus datasheet: versioned 2.4 URL and canonical family-datasheet
  URL under the Lattice publisher path returned HTTP404 on direct download.
  This pass uses the live manufacturer resource table, not an acquired/read
  full datasheet or an asserted timing/configuration guarantee.

No PDF originals were retained by this study. Empty ignored working directories
are not acquisitions. Full manuals and actual board schematics are needed
before implementing register-level timing, memory or reset/configuration behavior.
