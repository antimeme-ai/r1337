# 2026-10-15 — Portable instrument possibilities

## Operator direction

The operator is gathering equipment and wants us to think about possible
combinations in a new portable form factor. They identified a Flipper Wi-Fi
module v1, several Pis, TI LAUNCHXL-CC1312R1, a Freenove ESP32-WROVER and GPIO
extension, an unspecified Xilo flight controller, and assorted other modules.
The Bus Pirate is still being located. CAD and recent ESP32 SDR developments
are explicit interests. Preserve the understanding/discussion phase: no device
experiments, wiring changes, firmware installation, or implementation.

Recorded the incomplete, operator-reported inventory in
`docs/HARDWARE_INVENTORY.md`. Reused three frumentarii lanes for independent
research: ESP32 SDR claims and exact chip support; complementary RF/module
capabilities; and portable physical/system arrangements. Reports belong in
`papers/`, with source acquisition/restoration recorded where applicable.

## Questions guiding the pass

- Which recent SDR claims describe raw I/Q from the internal receiver, and
  which concern external front ends, CSI, packet capture, or RF generation?
- What do the classic WROVER, the Flipper Wi-Fi module's actual chip, and the
  TI LaunchPad add individually and together?
- Which experiences benefit from a single enclosure, removable probes, a small
  host, or distributed nodes? Which functions need local timing?
- What could a CAD-designed carrier improve in antennas, shielding, connectors,
  power, serviceability, and physical use? What hardware identities remain
  necessary before geometry or wiring can be specified?

Sources are research input, not dependency choices. No firmware/runtime,
transport, enclosure or architecture is selected by this pass.

## Findings and acquisitions

The three discussion reports are complete and linked in `docs/POSSIBILITIES.md`
and `papers/README.md`. ESP-SDR exposes real native raw I/Q. The classic ESP32
backend uses short internal-SRAM snapshots and UART export; continuous modes
and high-throughput examples require chip-specific hardware and transports.
The conditional S2 Flipper Wi-Fi board is a second possible snapshot platform,
with a firmware/debugging-role tradeoff. Same-chip Wi-Fi uplink during SDR and
phase-coherent reception from independently clocked boards are not established.

The module lane separates the CC1312R1's autonomous sub-GHz computer role from
Flipper's transceiver role, distinguishes classic WROVER from S2-WROVER, and
keeps the actual Freenove board/peripherals unverified. The physical lane
compares handheld/probes, a separate compute pack, a fold-out bench and remote
nodes by the experience each favors. No preferred architecture was selected.
CAD discussion concerns replaceable carriers, probe access, connectors and
antenna/power/service constraints; no geometry was produced.

Acquired three additional unchanged source archives with exact revisions and
restoration manifests, an author SDR measurement PDF, and the original TI
LaunchPad hardware guide. Updated `QUARANTINE.md`; the corpus now contains
eleven source snapshots and five literature PDFs. Acquired source was read but
not executed. No SDK, library, dependency, toolchain or firmware was adopted.

Exact Pi, Xilo, Bus Pirate, Freenove and accessory identities remain discussion
inputs. The original Flipper manual/schematic gaps remain recorded separately;
this pass did not require a new operator acquisition request. No device was
accessed or changed during this research turn.

## Validation and checkpoint

Checked all 65 relative document links, the shared doctrine symlink,
project-only Git scope and diff whitespace. This delivery changes research and
discussion documents only; no source tests were rerun. Publish the notes on the
existing research branch and update its pull request around the expanded scope.

## Further inventory: Bus Pirate, network/USB equipment and power

The operator located a device marked approximately “genuine bus 5 5 pirate”;
Bus Pirate 5 is the working identification, with revision/firmware unknown.
They also identified an unlocked MR6150, Pineapple Mark VII, MK7AC, candidate
O.MG Plug, Bash Bunny, additional Pis, FPV packs, prosumer network equipment,
light industrial controls and assorted legacy/current cables. The Nighthawk
battery is described as flat, 3.85 V and 19.4 Wh. Updated the inventory without
inferring unknown models, electrical signaling or pack configuration.

Two parallel research lanes documented BP5 and Hak5 platform roles. Root read
MR6150 primary specifications plus relevant manual sections and preserved two
original PDFs with hashes/restoration. The corpus now has eleven source
snapshots and seven original PDFs. No new source archive or dependency was
added by this increment.

Concrete findings: BP5 has meaningful wired/electrical functions, while its
revision-dependent rated output is distinct from the current-limit setting;
its capture topology differs from BP6. Pineapple is an active network computer,
MK7AC a host-dependent Wi-Fi interface, and the USB gadgets have device roles.
MR6150 supplies a candidate backhaul independently of any battery reuse. Label
arithmetic implies approximately 5.04 Ah nominal; ideal runtime examples are
energy calculations, not measured system runtime. All exact citations and
unknowns remain in the three new papers and possibility map.

Industrial/network equipment may serve as subjects to characterize or known
counterparts, and cable collections may supply identified adapters. Neither
connector shape nor an informal equipment category establishes electrical
compatibility. The current phase remains discussion. No additional device was
connected, activated, interrogated, opened or modified.

Checked the expanded set of 73 relative document links, shared doctrine
symlink, project-only Git scope and diff whitespace. This increment changes
documents only; no source tests or hardware experiments were run.
