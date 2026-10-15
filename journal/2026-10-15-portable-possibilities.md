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

## Acquisition preference

The operator is open to acquiring key components but explicitly prefers putting
the existing stash into practice over adding more equipment blindly. Recorded
this in agent guidance, project intent and the possibility map. Hardware
proposals must identify a useful gap or integration need; existing equipment
may contribute as final components, detachable instruments, development/test
fixtures or subjects. No part was selected, ordered or operated. This is a
text-only preference update; diff whitespace was checked.

## Physical direction: integrated core and one companion

The operator described a folding tablet or a cyberdeck with high production
values, portable and reasonably ordinary-looking. At most one detachable pocket
module is acceptable. They explicitly reject an improvised exterior assembled
from loose modules. Updated current project/agent guidance and the possibility
map so the earlier many-probe/distributed-kit research is not mistaken for the
product direction. Fit/finish, hinges, controls, ports, retained cable paths,
antenna placement, serviceability and a finished companion dock become inputs
to the design. No particular dimensions, keyboard/display layout, pocket-module
electronics or enclosure has been selected. No CAD or device work performed.

## Expected SLogic32U3

The operator backed Sipeed SLogic32U3 and expects a compact logic analyzer in
the medium term. Recorded it as expected future equipment, separately from
hardware in hand. Read current vendor introduction/hardware documentation;
published channel/rate tiers, USB 3.2 Gen2 and compact enclosure suggest an
independent digital observer alongside BP5 bus control and electrical context.
Current and older mirrored specifications differ, so no final mechanical
cutout, accessory configuration or delivered performance is assumed. No new
purchase, software dependency or device experiment was selected. Updated
inventory/possibility documents and checked diff whitespace; no source change
or source tests accompanied this text-only update.

## Two TI LaunchPads

The operator confirmed two LAUNCHXL-CC1312R1 boards. Updated the inventory and
possibility map: the pair can serve as controlled radio counterparts without
requiring another purchase. This is an available experiment arrangement, not a
selected build or authorization to operate the radios. The next discussion
should identify concrete desired uses, available host/display hardware and
comfortable carrying size before comparing integrated designs. Checked diff
whitespace; no device operations or source changes.

## Capability breadth and heterogeneous control systems

The operator clarified the primary goal as a capability-dense RF/EM/debug/
sense/device-firmware access and assessment many-tool. They added a secondary
focus on interfacing with and managing control systems; the lab contains
equipment from roughly 25 vendors spanning four decades. Updated the project
brief, entry point, agent guidance and possibility map. Capability breadth is
the objective, rather than requiring a narrow initial application; Flipper
firmware is a candidate component of this broader system. The finished portable
core and at most one pocket companion remain requirements.

Recorded electrical adaptation, protocol transport, device semantics and
coordinated operation as distinct design concerns. Persistent lab-side gateways
are an option to study, not a selected architecture. Model/connector/manual
identification remains useful input. No new research claim, dependency,
purchase or device operation was introduced. Checked the document diff and
whitespace; no code tests were needed.

## Tailnet and remote support

The operator proposed a tailnet-connected instrument supported by a remote
station with LLM inference, library lookup and heavier analysis. Recorded
this in the brief, agent guidance and possibility map; named host/library
details are in ignored context. Read current Tailscale primary documentation
for local service publishing and SSH. These establish network options without
selecting an application protocol or asserting an existing deployment.

The design direction keeps acquisition timing and device operations local,
transfers selected original captures with metadata, and returns source-linked
analysis. Offline use, resumable transfers and avoiding duplicate state-changing
commands are concrete design concerns. No host inspection, remote execution,
network configuration, service deployment, dependency adoption or device
operation occurred. Checked document diff and whitespace; no code tests needed.
