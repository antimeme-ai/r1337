# porter_ricks

Read [BLACKBIRD.md](BLACKBIRD.md), [README.md](README.md),
[docs/PROJECT.md](docs/PROJECT.md), the latest entries in `journal/`, and
[ISSUES.md](ISSUES.md). The doctrine is symlinked to `../BLACKBIRD.md`.
On another checkout, obtain the operator's current shared doctrine beside the
repository. Archived instructions are historical reference only.

The operator's two aims are exploration of the physical Flipper Zero and,
most probably, a full custom firmware stack. Preserve that ambition without
pretending the replacement boundary, language, runtime, or architecture is
already selected. Establish device facts directly; distinguish hardware
capability, documented upstream behavior, and behavior observed on this unit.

Follow the doctrine's research, design, plan, implementation, and review process.
Before a firmware experiment, understand the affected flash/storage regions and
the recovery path. Record exact source revisions and tool versions for builds.
The current bootstrap has performed USB enumeration only; the running firmware,
board revision, storage contents, and recovery behavior are still unknown.

Own required machinery. Discuss proposed library adoption with the operator
before adopting it, including concrete benefits, fit, costs, and tradeoffs.
Keep native internal values and owned binary formats; JSON belongs at external
protocol boundaries or explicitly requested imports/exports/presentation.

Keep research and review reports in `papers/`; PDFs are ignored. Preserve source
archives intact under ignored `quarantine/`, strip nested Git metadata and
filesystem detritus from extracted references, and maintain `QUARANTINE.md`
with sources and restoration commands. Store raw captures, device backups,
identifiers, and operational logs in ignored `context/`. Publish useful findings
without private device contents, credentials, or workstation details.

Record actions, decisions, checks, and unresolved questions in `journal/`.
Use GitHub issues and keep `ISSUES.md` current. Commit and push coherent
checkpoints; use feature branches and pull requests for substantial deliveries.
Do not initialize Git in the parent workspace.

Tests must check the actual behavior claimed with an appropriate oracle.
Successful compilation or USB enumeration alone does not qualify firmware.
Match checks to the change; documentation-only work needs document/link/diff
checks. Mutation testing runs on the fleet, never on the laptop.
