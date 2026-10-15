# ESP32 SDR reconnaissance — 2026-10-15

## Finding and scope

The recent reports describe a real capability: software can capture raw complex
I/Q from an ESP32's integrated radio through an undocumented diagnostic path,
bypassing its fixed Wi-Fi modem. This is distinct from Wi-Fi packet capture,
CSI sensing, attaching a tuner, or generating RF with GPIO/DAC peripherals.
ESPARGOS lists the original ESP32 and ESP32-S2 as supported receivers, making
both the Freenove WROVER and, conditionally, the Flipper Wi-Fi module relevant
research hardware. Neither physical board was inspected or programmed here.
[ESPARGOS project explanation](https://espargos.net/espsdr/).

This is a discussion input for a portable instrument. No hardware experiments,
source execution, builds, flashing, or library adoption occurred. Three source
snapshots and one measurement PDF were acquired; exact revisions, checksums and
restoration instructions appear in
[the acquisition report](2026-10-15-esp32-sdr-acquisitions.md).

## Five different meanings of “ESP32 radio”

| Technique | What software receives or emits | Hardware boundary |
| --- | --- | --- |
| Native raw-I/Q receiver | Time samples of complex baseband, from the radio's own downconverter/ADC | The new ESP-SDR/eSpDR route; narrow tuning envelope around the chip's RF design, not arbitrary HF-to-GHz coverage |
| Wi-Fi CSI | Complex channel estimates for Wi-Fi subcarriers, obtained from received packets | Useful for propagation and motion sensing; not a continuous waveform recorder |
| Wi-Fi promiscuous capture | Decoded Wi-Fi frames and reception metadata | Useful protocol observation; not an arbitrary modulation receiver |
| External tuner or quadrature front end | I/Q produced by a separate radio/ADC, with the ESP32 doing transport or DSP | Coverage and analog performance come from that external hardware |
| Peripheral waveform generation | A waveform emitted through GPIO or the general-purpose DAC | Can create RF signals; this does not establish any receiver path |

Espressif documents CSI as subcarrier channel responses estimated when Wi-Fi
packets arrive, while promiscuous mode exposes specified 802.11 frame classes.
Those are documented APIs and remain useful independently of the new raw capture
path. [ESP-IDF v5.5.1 Wi-Fi guide, “Wi-Fi Sniffer Mode” and “Wi-Fi Channel State Information”](https://docs.espressif.com/projects/esp-idf/en/v5.5.1/esp32/api-guides/wifi.html).

## What the hardware already mentioned might do

The following table describes source-supported candidates, not results observed
on the operator's hardware. Rates are complex sample pairs per second.

| Candidate | Current project support | Consequence for this inventory |
| --- | --- | --- |
| Classic ESP32, including the WROVER family | ESPARGOS snapshot I/Q at nominal 16/40/80 MS/s, UART; snapshot FFTs | Freenove board is a plausible existing spectrum/short-capture node; no S3-style continuous USB claim |
| ESP32-S2 | ESPARGOS snapshot I/Q at 16/40/80 MS/s; native USB-OTG CDC or UART; snapshot FFTs | Conditional second candidate if the Wi-Fi module is the documented ESP32-S2-WROVER model |
| ESP32-S3 | Snapshot/raw capture plus native USB continuous decimated I/Q, 15.625–250 kSa/s; continuous acquisition with on-chip FFT | Substantially different transport and DSP path from classic WROVER |
| ESP32-C3 | Snapshot capture at 80 MS/s, native USB Serial/JTAG or UART | Newer chip alone does not imply continuous wideband export |
| ESP32-C5 | Native receiver also covers its 5 GHz radio path | Relevant if later discussion calls for 5 GHz; not a feature of classic WROVER |
| ESP32-S31 | Experimental receive stream up to 20 MS/s USB or 40 MS/s Gigabit Ethernet | Requires the specific new board/interface arrangement; not any ESP32 with Ethernet added |
| ESP32-P4 | No integrated RF receiver in ESPARGOS support table | Can host external SDR hardware; it does not inherit the native RF capture trick |

Support/rate claims are from the pinned source's chip table and target backends.
Source version: [ESPARGOS/esp-sdr `e2b35dc`](https://github.com/ESPARGOS/esp-sdr/tree/e2b35dc593a378e4c5eb69cb8db59313117c9838).

Espressif's WROVER-B and WROVER-E datasheets identify classic ESP32 LX6 chips,
not S2/S3 processors. The exact suffix, flash, USB bridge and board revision still
need identification on the Freenove unit. PSRAM capacity is not evidence of a
larger radio capture buffer. [WROVER-B datasheet](https://documentation.espressif.com/esp32-wrover-b_datasheet_en.html),
[WROVER-E datasheet](https://documentation.espressif.com/esp32-wrover-e_esp32-wrover-ie_datasheet_en.html),
[Freenove board repository](https://github.com/Freenove/Freenove_ESP32_WROVER_Board).

The module research lane identifies the official Flipper Wi-Fi Module V1 design
as ESP32-S2-WROVER-N4R2; matching that design to the physical module remains open.
“S2-WROVER” and classic “ESP32-WROVER” must remain distinct. Replacing its firmware
with SDR research firmware would change the module's present debugging role;
that is an architectural tradeoff to discuss before device work.

## The classic WROVER limitation is transport and capture duty

The original ESP32 backend reserves a 64 KiB internal-SRAM aperture and permits
up to 16,380 complex samples per capture. It stops the dump engine before packing
and sending the result. The default UART is 2,000,000 baud. The S2 backend uses
48 KiB and at most 12,284 pairs, retaining another bank for ROM USB state.
Read source: `main/targets/esp32/receiver.c`, `sdkconfig.defaults.esp32`,
`main/targets/esp32s2/receiver.c`, and `docs/rx-controls.md` in
[the pinned ESPARGOS tree](https://github.com/ESPARGOS/esp-sdr/tree/e2b35dc593a378e4c5eb69cb8db59313117c9838).

Calculated from those source values, a maximum classic capture covers about
1.024 ms at 16 MS/s or 0.205 ms at 80 MS/s. At 2 Mbaud with ordinary 8N1 UART,
the ideal payload ceiling is 200 kB/s, equivalent to only 100,000 pairs/s for
8-bit I plus 8-bit Q, before protocol overhead. Thus a high internal sample rate
does not mean an equally fast continuous host stream. Dropping short events
between snapshots is intrinsic to this implementation.

S3's continuous mode instead processes a 16 MS/s ring on its second core and
filters/decimates before USB export. Its wire protocol carries sample indices
and explicit gap flags; host stalls and work overruns still lose samples. The
16-bit output option is a processing/storage format, not a claim of a 16-bit RF
ADC. FFT display modes can keep the RF writer running while analyzing only
selected windows, so a lively waterfall does not prove every short event was
observed. [Pinned `docs/iq-stream.md`](https://github.com/ESPARGOS/esp-sdr/blob/e2b35dc593a378e4c5eb69cb8db59313117c9838/docs/iq-stream.md),
[pinned `docs/spectrum.md`](https://github.com/ESPARGOS/esp-sdr/blob/e2b35dc593a378e4c5eb69cb8db59313117c9838/docs/spectrum.md).

## The 80 MS/s headline with an FPGA

h0m3us3r's eSpDR reports an S3 receiver exporting 80 million 10-bit-I/10-bit-Q
pairs per second through **16 GPIO data wires to an Alchitry Au FPGA**, DDR3
buffer and FT600 USB 3 interface. The packed payload is 200 MB/s before headers;
the FPGA compresses typical input enough to fit the measured USB path, with
buffering and reported gaps when the pipeline falls behind. This is a genuine
high-throughput architecture, but its FPGA, buffer, wiring and USB bridge are
essential parts of the result. A USB cable on the existing WROVER cannot reproduce
it. Its own documentation also distinguishes sampled span from the non-flat
analog passband and warns of aliasing. Acquired/read: README plus the source
and documentation layout, not an exhaustive FPGA audit.
[eSpDR pinned revision `f279bf8`](https://github.com/h0m3us3r/eSpDR/tree/f279bf823eee41796dfd1ac21f13e1ed9b418c82).

## New transmit work is also real, with separate prerequisites

The upstream ESPARGOS snapshot is receive-only. The separately developed
`esp-sdr-zephyr` describes S3 I/Q playback through the internal RF DAC, including
gapless streaming needing PSRAM. It also describes CPU-paced C5/C6 receive and
transmit up to 250 kS/s. Those statements are project claims tied to specific
chips and versions, not classic WROVER capabilities. Its current library takes
over the radio after Wi-Fi initialization and tells applications not to scan,
connect or run an AP while using it. Selected hardware-quirk notes describe gain
state loss, clock offsets, analog transmitter compression and phase differences
between loop repetitions. These are useful questions for an owned design.
[Pinned Zephyr port README and hardware notes](https://github.com/cyber-murmel/esp-sdr-zephyr/tree/8463f88f6d59c4cd1c657169d80ae099b5eaf19d).

Another S3 project uses the internal tone generator with polar modulation for
experimental FM/SSB voice. This differs from both I/Q playback and the older
general-purpose DAC technique. Its author explicitly bounds measurements to one
or two boards and discusses crystal heating/drift.
[jochenhammes/esp32-sdr-trx](https://github.com/jochenhammes/esp32-sdr-trx).

For comparison, bitluni's older AM example drives the classic ESP32 general DAC
through I2S to synthesize an approximately 835 kHz carrier on GPIO25. The source
really generates a waveform; it does not tap the 2.4 GHz receiver. We inspected
the README and short `.ino` source only, without acquiring or executing it.
[AM transmitter source](https://github.com/bitluni/ESP32AMRadioTransmitter/blob/master/AMTransmitterI2S/AMTransmitterI2S.ino).

## External hardware remains a distinct option

`hardcoreerik/esp-rtl-sdr` describes a USB-host driver for RTL2832U dongles on the
ESP32-P4 with high-speed USB; the current README explicitly does not claim S2/S3
full-speed hosts. `thaaraak/ESP32-A1S-Tayloe` is an older external quadrature/audio
approach, with ES8388 and Si5351-related machinery. These are reference leads
for a modular instrument, not proof of external radio/ADC availability in the
operator's assorted modules. No external receiver was identified or acquired.
[ESP32-P4 RTL-SDR project](https://github.com/hardcoreerik/esp-rtl-sdr),
[ESP32-A1S-Tayloe project](https://github.com/thaaraak/ESP32-A1S-Tayloe).

## Measurements read and limits still open

Zoltan Doczi's October 2, 2026 report is a primary author account of S3 FFT and
USB improvements. Its published comparison separates capture continuity from
the fraction actually analyzed. The acquired companion PDF reports a roughly
90-minute IQ stream exercise, explicit host-loss events and a frequency sweep;
its near-field RF arrangement gives relative results rather than absolute
receiver calibration. We read those bounded sections. They are stronger than a
waterfall screenshot but remain author measurements on a particular assembly,
unreproduced here. [Author report](https://blog.z2labs.io/article/esp32-s3-sdr-mode-throughput-improvement),
[pinned measurement PDF](https://github.com/z2labs/esp-sdr-bridge/blob/7da8aea5b667513dec8abd52675923cce1aefae3/docs/ESP32-S3_IQ_bridge_measurements.pdf).

The actual tuning envelope, analog response, absolute gain, overload behavior,
images, DC artifacts, frequency error and useful duty cycle on our boards remain
unknown. A software API accepting 100–6000 MHz does not demonstrate reception
across that range. Extended LO techniques have board-dependent lock and RF
response. None of the sources establishes calibrated laboratory-instrument
performance for our hardware.

## Implications for a portable instrument

These are design possibilities, not an implementation plan:

1. **A small spectrum scout from existing hardware.** The classic Freenove board
   or conditional S2 module could emit spectrum summaries and short I/Q captures
   for a handheld interface or Pi to display and store. This is useful even when
   captures have gaps, provided those gaps remain visible in the product model.
2. **A modular instrument with different radio personalities.** Packet decoding,
   Wi-Fi CSI, native raw I/Q, Sub-GHz transceivers and wired-bus interrogation
   produce different observations. A common time/event model could let the user
   compare them without pretending one receiver supplies every band and protocol.
3. **A processor and transport chosen after the measurement question.** A local
   FFT display, a narrow continuous demodulator and a full-band recorder have
   different bandwidth, memory, power and storage demands. The highest headline
   rate should not choose the enclosure or compute platform for us.
4. **A separate management path.** SDR firmware owns the RF chain; we should not
   assume that same radio also supplies dependable Wi-Fi networking. Wired UART,
   USB or a separate radio/host are candidate boundaries to discuss.
5. **Arrays as a separate research branch.** ESPARGOS demonstrates deliberately
   phase-synchronized multi-radio hardware. Merely installing the same firmware
   on several ESP32 boards does not provide shared phase/time references or a
   calibrated direction finder. [ESPARGOS array description](https://espargos.net/).

For the specific “wireless WROVER SDR” temptation: the acquired classic backend
starts Wi-Fi in `WIFI_MODE_NULL`, enables promiscuous receive and uses UART for
its host protocol. It does not implement an AP/STA network uplink concurrent
with raw acquisition. The Zephyr port explicitly prohibits scans, connections
and AP operation after takeover. Shared RF hardware and these implementation
choices give us no basis to promise same-chip Wi-Fi I/Q streaming; such
concurrency remains unestablished. A Pi or separate ESP32 could provide wireless
uplink while receiving observations over a wire, subject to a later throughput
and power design.

The existing hardware is enough to make this discussion concrete. Nothing in
this reconnaissance requires buying another ESP32 board or committing to an SDR
architecture before identifying the actual modules and intended observations.
