# Sources still needed

The research corpus is indexed in papers/README.md and QUARANTINE.md. These
are source/document acquisition gaps, not a hardware purchasing list. Earlier
Flipper/ST gaps remain live alongside the later instrument-design references.

| Priority | Item | Why needed | Acquisition gap |
| --- | --- | --- | --- |
| First | Revision-matched Flipper schematics: MCU, reset/buttons, power, peripheral buses | Establish actual routing and recovery/debug wiring | Official index links return HTTP 403 with expired signed URLs |
| First | RM0434 STM32WB reference manual | Register-level startup, memory/protection, IPCC, clocks and peripheral design | Web fetch exceeds size limit; local ST transfers failed |
| Next | DS11929 datasheet and ES0394 errata | Exact chip limits and silicon-revision-specific behavior | Relevant sections read on web; local ST transfers failed |
| Next | AN5185 plus FUS 1.2.0 release documentation | Installed FUS compatibility, transitions and recovery constraints | Current note read on web; local copy and historical reconciliation outstanding |
| Next | AN5289 wireless integration | CPU1/CPU2 mailbox, clock and flash coordination | Relevant sections read on web; local ST transfers failed |
| Next | AN2606 boot ROM | ROM entry, memory use and supported recovery commands | WB55 sections read on web; local ST transfers failed |
| Next | SA0024 CPU isolation advisory | Preserve the exact vendor statement alongside CPU2 research | Read on web; local copy still needed |
| Later | A working MR6150 open-source firmware bundle matching an identified release | Establish application-side OS, architecture and driver details before treating it as a general computing platform | NETGEAR lists packages, but its two MR6150 archive targets returned HTTP 404 during the router-internals pass |

Exact primary URLs, served document revisions, acquisition failures, and
restoration details are in the
[hardware acquisition report](papers/2026-10-15-hardware-acquisitions.md).
The newer NETGEAR source gap is documented in
[MR6150 internals](papers/2026-10-15-mr6150-internals.md); its
[manufacturer catalog](https://www.downloads.netgear.com/files/GDC/2649_GPLv1.html)
points MR6150 releases to `NTGX65_10.04.13.00-OSC.tgz` and
`NTGX65_12.01.11.00.zip`, both unavailable when checked.
Fresh official links or operator-provided original PDFs can fill these gaps.
Continue independent source work while these downloads remain unresolved.


## Aftermarket and measurement-source gaps

| Priority | Source needed | Concrete reason | Current gap |
| --- | --- | --- | --- |
| If UHF path advances | UCM601/UCM601NC original module manual, actual FZUHF PCB schematic/pinout and firmware information | Reconcile app/source/store features and reader control/RF limits | No original module RF/protocol manual retained; maker's pin-number table conflicts with official Flipper numbering |
| If FlipperMeister integration advances | Currently deliverable carrier revision, reader/SAM configuration, cable pinout and maker instructions | Compare complete packages and provisioned operations | Original RTT listings returned 404; published CAD and seller branding do not establish shipping configuration |
| If CAN Commander advances | Current board schematic, board firmware and actual supported CAN-FD operations | Separate FD-capable parts from implemented end-to-end modes | New board differs from the older MCP2515 project; termination/isolation/FD mode evidence incomplete |
| Later design literature | Keysight 5950-3000, Impedance Measurement Handbook, 6th Edition | Broader comparison of impedance methods, fixtures and compensation | Official go.keysight.com download returned 403; www variant served HTML instead of a PDF; not read |
| Later design literature | Keysight 5989-5723, Time Domain Analysis Using a Network Analyzer | Full application note beyond acquired/read HTML help | Official literature CDN returned 403; HTML help acquired as partial alternative |

Exact source links, acquisition failures and alternatives are recorded in the
[Flipper survey](papers/2026-10-15-flipper-aftermarket-frumentarii.md) and
[measurement acquisition manifest](papers/2026-10-15-interface-methods-acquisitions.md).
The [interface manifest](papers/2026-10-15-interface-aftermarket-acquisitions.md)
also records ADI/NXP original-download gaps; primary text was readable, so those
become acquisition priorities only if their circuits enter detailed design.
None blocks the present survey or requires a purchase.

## Timing-engine design sources

| Priority | Source needed | Concrete reason | Current gap |
| --- | --- | --- | --- |
| Before RP2040 register-level design | Original RP2040 datasheet | Preserve FIFO/stall/divider/DMA details beside the engine design | Both current pip-assets and legacy original URLs returned HTTP403 on direct download; selected primary text was readable on web |
| Before iCE40 implementation | Original UltraPlus datasheet and revision-matched candidate board schematics | Pin/bank, memory-port, clock, configuration/reset and actual transport design | Attempted versioned/canonical Lattice PDF targets returned HTTP404; resource table and maker pages read, full original not retained; old iCEBreaker hardware documentation must not substitute for V1.1b |

Exact attempted sources and the original-source acquisition are recorded in the
[timing-engine study](papers/2026-10-15-timing-engine-study.md). These gaps do not
block the current comparison or select a board/toolchain.
