# 2026-10-15 — Device inventory and parallel frumentarii

## Purpose and plan

The operator authorized continuing device exploration and explicitly requested
a parallel frumentarii pass. Work proceeds on
`research/initial-reconnaissance`.

The host lane will establish a read-only CLI session, inspect the device's help
and identity output, then query power, storage metadata, and memory state using
commands grounded in official source and the installed command list. Raw output
and unit identifiers stay in ignored `context/`. No peripheral transmission,
device file-content collection, reboot, firmware installation, or flash/config
write is planned. Capture failures and unknowns rather than guessing.

Three independent frumentarii lanes cover hardware/manuals, official firmware
source/architecture, and recovery/debug/host tooling plus custom-stack references.
Each writes its report and acquisition manifest in `papers/`; the owning lane
preserves archives and cleans extracted references. Integrate their findings into
the research index, quarantine manifest, device report, and issue tracker.

The source and manual reports will support a synthesis of replacement boundaries
and concrete next experiments. This pass does not select a firmware architecture
or adopt a dependency.

## Initial source grounding

Pinned upstream CLI source registers `device_info`, `info`, `uptime`, `date`,
and `free`. The device info and power handlers read HAL state; storage `info`
and filesystem-root `stat` read metadata. CDC DTR starts the shell. No process
held either serial node when checked with `lsof`.

The installed firmware has not yet been identified, so inspect its banner/help
before relying on current upstream command names. A small host-only standard
library collector will preserve raw bytes, limit reads with explicit deadlines,
and restore serial attributes on exit. It is experiment tooling, not a firmware
runtime or library adoption.

## Results

The device reports dev 0.81.1 / 1af02211 firmware, hardware code 12, FUS 1.2.0,
radio stack 1.13.3, protobuf 0.15, 44 KiB of internal LittleFS, and a mounted
approximately 29.16 GiB FAT32 microSD filesystem. Heap/thread/power snapshots
and the exact meaning/limits of these self-reports are in `docs/DEVICE.md`.
Raw captures remain private in `context/`. Official source resolves the reported
short hash to a 2023-04-08 commit; binary authenticity was not established.

Hardware, firmware, and recovery frumentarii wrote separate reports and
acquisition manifests in `papers/`. Eight source archives and three literature
PDFs were acquired. Source trees include modern and historical official
firmware, selected modern submodules, qFlipper, two upstream-based firmware
forks, and Rust application bindings. The manifests preserve exact revisions,
hashes, restoration commands, and acquisition scope. No acquired code was run.

Important findings: firmware owns flash-base vectors; a preserved independent
Flipper bootloader partition cannot be assumed. Historical `/int` is flash
LittleFS while modern `/int` aliases SD storage and can create its backing
directory. Retaining CPU2 requires explicit shared-resource coordination.
Published CPU2 execution research qualifies the supported ST-signed-update
boundary; no CPU2 method was reproduced. qFlipper discovery writes the clock,
bare CLI invocation initiates update/repair, and normal backup is `/int` only.
The synthesis in `docs/RECONNAISSANCE.md` links exact report/source support.

Original ST document downloads and expired schematic links remain unresolved.
`SHOPPING_LIST.md` records those gaps without preventing other source work.
No language, runtime, library, or final replacement boundary was selected.

## Owned inventory utility and direct checks

Promoted the host collector to `scripts/flipper_inventory.py` with fixed
source-reviewed metadata queries, bounded prompt reads, exact raw capture,
partial-output retention, and refusal to continue past identity reads when the
reported firmware differs from the inspected historical profile. It uses the
host Python standard library and native `lsof`; it is not production firmware.

Independent recovery-lane review identified two real defects: TIOCEXCL did not
exclude a pre-existing serial owner, and DTR was not restored. Fixed both:
inspect existing owners of both serial aliases under exclusivity, then restore
the observed DTR bit, termios state, and exclusivity flag in cleanup. A native
Darwin PTY with a second process holding the port directly confirmed rejection
before configuration or commands. No command-injection finding was raised.

The ownership check exposed two host details in direct execution: lsof returns
1 when an unused alias has no matching descriptor, even while reporting our PID;
and default tty.setraw flushes a banner already queued while lsof runs. Accept
that observed no-match return only with valid owner output and no diagnostics,
and use TCSANOW to retain queued bytes. The final collector completed a live
inventory. Earlier failed attempts retained their partial captures privately.

Six direct stream/profile tests cover fragmented prompts, disconnect retention,
deadline failure, oversized output, matching identity and mismatched/incomplete
identity. Seven collected metadata responses were checked for expected fields
and complete returned prompts. Physical recovery, debugger access, peripheral
health, and scoped backup/restore remain open; there was no firmware update,
reset, flash/config write, debugger attach, radio test, or device file-content
collection in this pass.

## Delivery

Closed GitHub #1 with the repeatable baseline and its explicit limits. Updated
#2 and #3 with the recovery/source findings and remaining work; #4 remains the
future reviewed custom-system design. The local issue index matches those
statuses. All 45 relative document links, the shared doctrine symlink,
project-only Git scope, and diff whitespace checks passed. Publish this coherent
research/tooling checkpoint on the feature branch with a pull request.

## Operator steering after reconnaissance

The operator wants to understand the device and consider possibilities before
further experiments or implementation. They have more equipment and ideas to
introduce, including a Bus Pirate. Its revision is unknown. Updated project and
agent guidance to preserve this discussion phase and avoid treating recovery or
custom-firmware work as the automatic next action.

Read current official Bus Pirate hardware/logic-analyzer documentation and
Flipper specifications/GPIO documentation to ground the initial discussion.
Potential complementary roles are RF/IR/NFC stimulus and portable interaction
on Flipper, wired protocol/measurement functions on Bus Pirate, and host-side
coordination/analysis. Exact electrical, capture, power and control-interface
capabilities are model-dependent; no pairing design is selected. No device
access or code change occurred during this discussion turn.
