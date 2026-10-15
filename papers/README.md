# Research index

The first parallel frumentarii pass combined source study and literature with
an independently collected device inventory. Read the
[reconnaissance synthesis](../docs/RECONNAISSANCE.md) for consequences and next
experiments, and [device inventory](../docs/DEVICE.md) for direct observations.

## Reports and acquisitions

| Lane | Research report | Acquisition/restoration record |
| --- | --- | --- |
| Hardware/manuals/CPU2 | [Hardware findings](2026-10-15-hardware-frumentarii.md) | [Three PDFs and download gaps](2026-10-15-hardware-acquisitions.md) |
| Firmware source | [Startup, memory, storage, CLI/RPC and ownership](2026-10-15-firmware-frumentarii.md) | [Four source snapshots](2026-10-15-firmware-acquisitions.md) |
| Recovery and tooling | [Recovery mechanisms, host effects and independent references](2026-10-15-recovery-frumentarii.md) | [Four source snapshots](2026-10-15-recovery-acquisitions.md) |

The source snapshots retain exact upstream revisions, original archives,
checksums, restoration commands, and license locations. Acquired code was not
executed and no dependency was adopted. Reports distinguish material actually
read from sources merely located. Original PDFs are ignored in
`papers/hardware/`; extracted source and archives are ignored in `quarantine/`.

## Two source baselines

- [Modern official firmware reference](https://github.com/flipperdevices/flipperzero-firmware/tree/3fb1d51727733d2007abc5ec636a89328857803e),
  retained from bootstrap for comparison.
- [Historical official reference matching the reported device hash](https://github.com/flipperdevices/flipperzero-firmware/tree/1af022116e3d6b262289c5668a90f0fa353592c2),
  used to inspect the observed 0.81.1 command and storage behavior.

A matching self-reported identity is not binary authentication. Modern source
must not stand in for the installed-reference behavior. The reports record
source-path links for concrete findings and identify which baseline they use.

## Open literature work

[SHOPPING_LIST.md](../SHOPPING_LIST.md) records original ST PDFs and fresh
schematic links still needed. Several ST documents were readable through web
access while local transfers failed; RM0434 and revision-matched schematics
remain important unread gaps. The CPU2 research paper was acquired and read;
its conclusions were not reproduced on this device.

Next research should reconcile actual chip/protection/layout information with
the historical firmware and published manuals, then support the recovery design
and first owned CPU1 milestone. No project language/runtime or firmware
replacement boundary has been selected.
