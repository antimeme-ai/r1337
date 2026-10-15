# Checking the supplied hardware and protocol-tool leads

Research date: 2026-10-15. The operator supplied a Gemini-generated list during
the aftermarket/unusual-interface survey. It contains useful references and
incorrect hardware attributions. This note checks consequential claims against
primary documentation and selected pinned source. No tool, library or runtime
is adopted; no device experiment was performed.

## Hardware claims

| Supplied claim | Source-supported correction | Consequence for r1337 |
| --- | --- | --- |
| Application-specific chips cannot analyze unknown devices | Too broad. A specialized frontend/engine can provide the required physical interaction or useful decoded observations; discarded information and supported modes set its limit. UHF readers/SAM interfaces are concrete examples. | Combine suitable protocol engines with lower-level observations where needed; an FPGA does not recreate every analog frontend. |
| FTDI is the underlying engine of Bus Pirate | BP5 uses RP2040. Older Bus Pirate FTDI transport must not be confused with an MPSSE implementing the target protocol. | Evaluate actual BP5 before buying overlapping common-bus machinery. |
| MPSSE provides arbitrary bus interception | It generates/clocks configured synchronous exchanges; the chips also have UART/bit-bang modes. This does not establish arbitrary passive sniffing, target/slave operation or real-time host branching. | Specify controller/target/sniffer role, electrical and timing requirements per mode. |
| All FT4232H channels are equivalent engines | FTDI documents MPSSE on A/B, with C/D providing UART/bit-bang modes. FT2232H has MPSSE on both channels. | Count actual engine resources/concurrency. |
| FPGAs match any clock, delay or encoding | Reconfigurable logic has finite I/O, fabric, timing, buffering and export limits; analog/frontend limits remain. | Define useful operating points before comparing FPGA families. |
| GreatFET and Saleae Logic Pro both use onboard FPGAs | GreatFET One uses LPC4330/SGPIO for documented logic streaming. Saleae documents FPGA sampling for Logic Pro. | MCU peripheral engines and FPGA gateware are different timing tools. |
| MAX2870 is a HackRF I/Q transceiver | MAX2870 is a PLL/VCO synthesizer. HackRF One lists MAX2837, MAX2839 for r9, MAX5864 ADC/DAC and RFFC5072 mixer/synthesizer. HackRF Pro has a different block diagram/MAX2831. | Separate oscillators, mixers, transceivers, ADC/DAC, processing and export; preserve revision. |
| RTL2832U alone is a complete RF frontend | RTL-SDR Blog V4 identifies R828D tuner plus RTL2832U and a designed RF/filter/upconverter path; receive-only. It repurposes a digital-TV architecture. | Frequency coverage, instantaneous bandwidth, dynamic range and TX are separate requirements. |
| Promiscuous CC2531/CC2540/CC2650 firmware captures arbitrary air traffic | TI documents device/protocol/PHY combinations: CC2531 examples concern 802.15.4-family traffic, CC2540 examples BLE. Packet output depends on configured acquisition behavior. | Disabling address filters does not provide arbitrary modulation, simultaneous channels, decryption or raw I/Q. |

Primary hardware sources read:

- [BP5 hardware](https://docs.buspirate.com/docs/hardware/bp5rev10/introduction/)
- [FT2232H MPSSE datasheet](https://ftdichip.com/wp-content/uploads/2020/07/DS_FT2232H.pdf)
  and [FT4232H description](https://ftdichip.com/products/ft4232hl/)
- [GreatFET hardware](https://github.com/greatfet-hardware/azalea) and
  [SGPIO capture](https://greatfet.readthedocs.io/en/latest/greatfet_logic.html)
- [Saleae recording path](https://www.saleae.com/support/troubleshooting/capture-and-recording-issues/digital-and-analog-appear-different)
- [HackRF components](https://hackrf.readthedocs.io/en/stable/hardware_components.html)
  and [MAX2870](https://www.analog.com/en/products/max2870.html)
- [RTL-SDR Blog V4 datasheet](https://www.rtl-sdr.com/wp-content/uploads/2024/12/RTLSDR_V4_Datasheet_V_1_0.pdf)
- [TI packet-sniffer support/releases](https://www.ti.com/tool/PACKET-SNIFFER)

TI lists LAUNCHXL-CC1312R1 among SmartRF Packet Sniffer 2 hardware. Release notes
say silicon revision C (1.1) needs older 1.6.0; the page combines stale overview
installation text with newer release notes. Our two boards are a concrete
source-study opportunity, not evidence for flashing an unidentified revision
or running that package on the eventual portable host.

## Software references and inspected source

| Reference | Useful capability | Boundary |
| --- | --- | --- |
| [URH](https://github.com/jopohl/urh) | Signal inspection/demodulation, customizable decoding, manual fields and rule-based field inference | Requires suitable captures. Original repository is archived, not an automatically selected maintained dependency. |
| [Netzob](https://github.com/netzob/netzob) | Message alignment/clustering, vocabulary and state modeling, passive/active approaches | Alignment proposes structure; framing, sample diversity and controlled observations determine inference quality. |
| [Wireshark Lua](https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm.html) | Record an understood interpretation as a dissector, tap or file adapter | Does not discover electrical signaling or command meaning by itself. |
| [Scapy](https://scapy.readthedocs.io/en/latest/introduction.html) | Structured packet construction/dissection and retained request/response observations | Does not supply a missing physical interface, hardware timing or target-state semantics. |

Capabilities follow primary descriptions; their boundaries here are engineering
judgments. Retain originals so interpretations can change without repeating a
physical experiment.

Acquired URH pin 1403d92987cc3d01d41aff64250955ce455dabd2 and Netzob pin
088fe769e98e0bfbd3ed99e66b3982446bf8d197. URH FormatFinder constructs specific
length/address/sequence/checksum engines; its modulation detector makes
particular ASK/FSK/PSK-family decisions. Netzob ClusterByAlignment uses scores
and UPGMA; FieldSplitAligned calls Needleman-Wunsch alignment. These inspected
paths support the descriptions, not universal recovery or reproduced accuracy.

GitHub metadata on the research date reports URH archived, acquired commit
dated 2025-12-19. Netzob is not archived; its acquired default-branch commit is
dated 2023-01-08. Evaluate maintenance/build fit if adoption is ever proposed;
these facts do not make the ideas obsolete. Exact source paths, hashes,
restoration and read scope are in the [acquisition record](2026-10-15-interface-methods-acquisitions.md).

## Information lost during acquisition

Analog voltage/IQ samples, threshold crossings, demodulated bits, framed packets
and decoded fields are different records. A packet engine may discard invalid
preambles/CRCs before software sees them. A logic analyzer retains threshold
decisions rather than analog edge shape. RF capture retains only its selected
passband and available dynamic range. Software cannot reconstruct observations
never acquired.

Choose the lowest useful observation layer for the question and retain original
data, settings, completeness and transformation history. Use protocol engines
where useful; add raw capture for concrete unresolved questions. Infer fields/
state from controlled changes and independent readback where possible. A
plausible parser remains a hypothesis until it predicts new observations.
This extends the architecture without selecting these tools, a new FPGA or a
software loadout.
