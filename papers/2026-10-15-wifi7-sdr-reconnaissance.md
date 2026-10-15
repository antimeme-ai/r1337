# Wi-Fi 7 router SDR reconnaissance — 2026-10-15

## The concrete project behind the recent reports

**[h0m3us3r/w1700k-sdr](https://github.com/h0m3us3r/w1700k-sdr)** is a substantive
match for the operator's observation. It turns supported Gemtek **W1700K HW 1.x**
and **W1700K2 HW 2.1** routers into raw-I/Q receivers using a MediaTek **MT7996**
radio and Airoha **AN7581** host SoC. This is a particular board/chip/firmware
combination, not a capability established for every router sold as Wi-Fi 7.

The GitHub API reports repository creation on **2026-10-11**. This pass acquired
revision **`0b0413e4309f0c083702fa4eb2d1c2bca4532163`**, committed
**2026-10-13 03:25:39 UTC**. All source-specific findings below refer to that
snapshot, rather than assuming later `main` is unchanged. Acquisition and
restoration details are in
[the companion manifest](2026-10-15-wifi7-sdr-acquisitions.md).

We read its architecture, roadmap, firmware, platform, driver and host-stream
documentation and selected capture/export/packing source. No source was built or
executed, no device operated, and no hardware or dependencies selected. Results
described as measured are the project's author reports, not reproductions here.

## What this receiver actually supplies

| Property | Source-grounded capability and boundary |
| --- | --- |
| Output | Complex baseband I/Q sample values with 14 useful bits per component; host representation is complex int16 |
| Rates | 40, 80, 160 or 320 million complex pairs/s on each selected band |
| RF chips | MT7976 A-die for 2.4 GHz; two MT7977 A-dies for the 5 and 6 GHz paths |
| Capture scope | One selected band streams; bands can be switched during a stream. Three front ends do not establish three simultaneous exported channels |
| Tuning | Unit A reports approximately 2.081–2.748 GHz and combined 4.647–7.576 GHz; roadmap qualifies reception above 7.41 GHz as lock-flag-only evidence |
| Receive controls | LO, manual gain/AGC, filter and selected band; new sample rates currently require a between-stream operation |
| Transmit | Project firmware is receive-only and keeps MAC transmit disabled |
| Data transport | PCIe into router DRAM, then raw-sample UDP export over 10 GbE |

[Pinned architecture](https://github.com/h0m3us3r/w1700k-sdr/blob/0b0413e4309f0c083702fa4eb2d1c2bca4532163/docs/architecture.md),
[coverage qualifications in roadmap](https://github.com/h0m3us3r/w1700k-sdr/blob/0b0413e4309f0c083702fa4eb2d1c2bca4532163/docs/roadmap.md).

The output is genuine time-domain waveform data before Wi-Fi packet decoding,
not only CSI subcarrier estimates, a radar-detection indication, an FFT test
screen, or monitor-mode packet bytes. It can therefore feed arbitrary *receive*
DSP within the capture path's analog and sampling limits. It does not establish
a programmable-I/Q transmitter or calibrated 14-bit receiver dynamic range.

## What changed in the firmware

This goes considerably further than clicking a factory test mode. The project
supplies its own MT7996 ROM patch, WM radio-controller firmware and WA packing
firmware. Its bring-up reconstructs the relevant cold-start register procedures,
reads the unit's calibration EEPROM and performs receive setup. Host commands
reach the WM through a mailbox; selected RF controls run between sample chunks.
The source contains the corresponding radio procedures and packing implementation.
[Firmware description and source](https://github.com/h0m3us3r/w1700k-sdr/tree/0b0413e4309f0c083702fa4eb2d1c2bca4532163/firmware).

The authors describe tracing and reducing vendor initialization rather than
loading vendor radio firmware at runtime. That is their bounded ownership claim.
The whole router is not replacement software from reset: the platform retains
the stock first-stage boot path and adds its own U-Boot loader, Linux and root
filesystem. Its platform inputs also include Ethernet PHY firmware. The supplied
installation replaces the normal router OS; ordinary AP service is not a
documented concurrent role of this SDR image.
[Platform stages and upstream inputs](https://github.com/h0m3us3r/w1700k-sdr/blob/0b0413e4309f0c083702fa4eb2d1c2bca4532163/platform/README.md).

## The export path is as important as the radio

The capture engine writes a 1 MiB radio-SRAM ring; the producer sends chunks
through PCIe DMA into a **1 GiB router-DRAM ring**. The kernel exports each slice
as a jumbo UDP datagram. At 320 MS/s, storing each pair as a 32-bit word produces
**1.28 GB/s**. Half the chunks are losslessly packed to 28 bits/pair by the radio's
cores, reducing the average to 30 bits/pair: **9.6 Gbit/s sample payload**, before
network overhead. This explains the reported roughly 9.75 Gbit/s wire rate and
why a 10 GbE interface is part of the result. The ring absorbs only about
0.8 seconds of full-rate stalls. A slower Ethernet path does not inherit that
sustained stream merely because it can display the browser UI.
[Architecture throughput account](https://github.com/h0m3us3r/w1700k-sdr/blob/0b0413e4309f0c083702fa4eb2d1c2bca4532163/docs/architecture.md),
[packing source](https://github.com/h0m3us3r/w1700k-sdr/blob/0b0413e4309f0c083702fa4eb2d1c2bca4532163/firmware/stream/pack.S).

The documented host uses Linux, eight receive threads by default, six processing
workers and multiple memory rings. Its NIC needs an MTU of at least 8236 and large
socket buffers. Sample sequences, loss tags and stale-data checks expose several
failure classes; they do not promise zero loss for any host or workload. The
radio driver's documentation also reports that PCIe power saving limited DMA to
about 0.33 GB/s and is disabled for this mode.
[Host ingest and data integrity](https://github.com/h0m3us3r/w1700k-sdr/blob/0b0413e4309f0c083702fa4eb2d1c2bca4532163/host/stream/README.md),
[driver transport](https://github.com/h0m3us3r/w1700k-sdr/blob/0b0413e4309f0c083702fa4eb2d1c2bca4532163/kernel/w1700k_sdr/README.md).

Calculated from the published host format, full-rate int16-I/int16-Q recording
would produce **1.28 GB/s, or about 4.6 TB/hour**, before other recording overhead.
A pocket instrument would likely need a deliberate choice between raw recording,
decimation/channel extraction and compact spectral/event summaries. That is a
system-design consequence, not an implemented reduction feature established by
this pass.

## Sample rate, passband and calibration remain different claims

Normal decimated modes lose level toward the sampled span's edges. The source's
optional “flatten” filter applies the inverse of an author-measured roll-off,
capped at +24 dB, directly to samples. The published unit-A comparison uses its
noise floor and gives relative before/after response values. This corrects a
particular response; it does not establish absolute input power or recover
information already lost to clipping or aliasing.

The special band-2 **640/2** mode captures every other sample of a 640 MS/s path.
It reports a flatter response to about ±155 MHz, with a stated tradeoff: signals
160–320 MHz from the LO can fold into the output. Thus “320 MS/s” should always
be accompanied by the chosen capture/filter mode when comparing receivers.
[Response correction details](https://github.com/h0m3us3r/w1700k-sdr/blob/0b0413e4309f0c083702fa4eb2d1c2bca4532163/host/stream/README.md),
[capture-mode qualification](https://github.com/h0m3us3r/w1700k-sdr/blob/0b0413e4309f0c083702fa4eb2d1c2bca4532163/docs/architecture.md).

The roadmap explicitly leaves **dBFS-to-dBm calibration**, a validated **24-hour
stream**, a build on a fresh machine and some second-unit update/recovery cases
open. It reports install/return-to-stock on a second W1700K2, while one NAND
variant remains hardware-untested. This is useful engineering candor. The code
and bench account substantiate a working research receiver; this pass found no
independent calibration campaign establishing sensitivity, noise figure, effective
resolution or blocking performance across its claimed envelope.
[Pinned maturity checklist](https://github.com/h0m3us3r/w1700k-sdr/blob/0b0413e4309f0c083702fa4eb2d1c2bca4532163/docs/roadmap.md).

## Related work that should stay distinct

Daniel Wegemer and Edoardo Mantovani's **Nullcon 2025** slides document MediaTek
ICAP raw-I/Q reception on MT6769 in a Realme 6i and separately document CSI on
MT7981 boards. The slides put raw-I/Q transmission and Wi-Fi 7 MT7925/MT7927
investigation under **future research**. They therefore provide background on
diagnostic paths, not evidence that these Wi-Fi 7 models already provide the
W1700K's continuous export. Slides were read through the web tool; local download
returned HTTP 403. [Primary conference slides](https://nullcon.net/wp-content/uploads/2026/04/Unlock-hidden-Superpowers-in-MediaTek-WiFi-Chips.pdf).

`openwifi` is another genuine software-radio project, but its Linux driver and
FPGA-based 802.11 design describe a different hardware platform. It is not a
general firmware switch for commodity Wi-Fi 7 routers.
[Primary openwifi repository](https://github.com/open-sdr/openwifi).

This bounded search located the W1700K project as the concrete current router
example. It did not establish an equivalent working QCN9274/ath12k or generic
MT7996-card replacement. Same chip family or a factory waveform command alone
does not establish board initialization, continuous capture, export throughput
and calibration.

## Fit with the operator's hardware and form factor

Relative to our [ESP32 reconnaissance](2026-10-15-esp32-sdr-reconnaissance.md),
this is a substantial capability jump: wider continuous raw capture, higher
sample precision and 5/6 GHz front ends. The classic WROVER remains an already
owned short-capture candidate; it cannot be assigned the router's export path or
sample rate. The user-identified **MR6150 is Wi-Fi 6**, with a 1 GbE port in
NETGEAR's specifications. It is neither the named Gemtek target nor an established
substitute SDR receiver or full-rate stream relay.
[NETGEAR MR6150 specifications](https://www.netgear.com/mobile-wifi/hotspots/mr6150/).

For the preferred **finished folding tablet/cyberdeck plus at most one pocket
module**, three concrete implications follow:

1. The tablet could be a browser/control surface while a receiver-side component
   performs acquisition and DSP. The current demonstration still uses a separate
   Linux host; putting sufficient processing and interfaces in the allowed pocket
   module would be additional engineering.
2. A full-rate raw capture role demands a suitable 10 GbE ingress, sustained
   memory/compute, power and thermal design. A spectral-summary role could expose
   a much lighter UI connection after processing, but that reduction must run
   somewhere explicit.
3. Identify the prosumer networking hardware already in the stash before any
   purchase discussion. Exact model, radio chips, revisions, interfaces and power
   requirements matter. A discovered supported board would give us a specific
   research candidate; “Wi-Fi 7” on a box would not.

This work establishes a promising optional wideband receiver branch. It does not
choose the deck, radio module, or acquisition hardware, and no buying or flashing
is proposed as the next step.
