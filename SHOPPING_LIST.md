# Sources still needed

The first frumentarii pass acquired eight source snapshots and three literature
PDFs. The remaining gaps concern original schematics and local copies of ST
manuals. No purchase is currently identified.

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
