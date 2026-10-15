# Issue index

GitHub issues track project work. Keep this readable index synchronized when
opening, closing, or materially changing an issue.

| Issue | Work | Status | Inputs |
| --- | --- | --- | --- |
| [#1](https://github.com/antimeme-ai/r1337/issues/1) | Record the connected Flipper Zero baseline | Complete | Repeatable metadata collector; explicit unobserved items in device report |
| [#2](https://github.com/antimeme-ai/r1337/issues/2) | Understand and exercise the device recovery path | Open: source study complete; physical trial pending | #1; historical layout; available probe/access |
| [#3](https://github.com/antimeme-ai/r1337/issues/3) | Research portable instrument hardware, firmware, and integration boundaries | Open: initial, weird-device, aftermarket and unusual-interface passes assembled | Research index, capability discussion, pinned reference corpus; manual/schematic gaps remain |
| [#4](https://github.com/antimeme-ai/r1337/issues/4) | Design the first useful custom firmware milestone | Open | #1, #2, #3 |
| [#6](https://github.com/antimeme-ai/r1337/issues/6) | Resurrect TMTSOYP as a core application | Deferred to software-loadout discussion | Operator requirement; locate and understand prior project before design |
| [#7](https://github.com/antimeme-ai/r1337/issues/7) | Develop and review the service-monitor system design | Open: first proposal reviewed; detailed requirements/block design next | Architecture, capability matrix, three review reports; actual host/interfaces and measurement targets remain open |

The [first reconnaissance](docs/RECONNAISSANCE.md) records the current findings
and proposed next conceptual units. Current operator direction puts device
understanding and [portable possibilities](docs/POSSIBILITIES.md) first while
the [hardware inventory](docs/HARDWARE_INVENTORY.md) grows. The missing manuals,
source/layout reconciliation and scoped recovery experiment remain future work.
CPU2 replacement remains a research question; an owned CPU1 milestone is a
concrete candidate for #4, not a selected design.

The [first system architecture](docs/ARCHITECTURE.md) and
[capability matrix](docs/CAPABILITIES.md) now advance #7. The design proposes
local instrument engines, local host/records, remote assistance and an
articulated service-monitor body; component roles remain proposals. Physical
experiments and implementation still require detailed design and a reviewed plan.


The [aftermarket/unusual-interface synthesis](papers/2026-10-15-aftermarket-and-interface-synthesis.md)
adds #3 inputs for #7: explicit frontend/fixture gaps, UHF/contact-card roles,
overlooked physical/temporal channels and checked protocol-tool references.
No new hardware or software dependency was selected.
