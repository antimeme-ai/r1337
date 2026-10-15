# 2026-10-15 — MR6150 internals and Wi-Fi 7 SDR

The operator asked what is actually inside the Nighthawk MR6150 and pointed to
recent Wi-Fi 7 router SDR work. This remains understanding/research only under
the finished-core/one-pocket-companion direction. No device opening, probing,
network access, firmware changes or implementation is planned.

Two parallel lanes cover exact-model MR6150 internals using manufacturer and
regulatory evidence, and actual Wi-Fi 7 raw-I/Q projects using original source
and author measurements. Root is reading the primary findings and will connect
them to the current possibility map. Keep identified chips, visual inferences,
software-access evidence and unknowns separate. A modem's supported carrier
bands or factory-unlocked status does not establish an accessible raw-I/Q path.

Early primary sources identify MR6150 as an X62/Wi-Fi 6 device and locate its
North American filing, FCC ID PY322100564. The recent router SDR project is
`h0m3us3r/w1700k-sdr`, targeting Gemtek W1700K/W1700K2, MediaTek MT7996 and an
Airoha AN7581 host SoC with 10 GbE export. Exact capability and measurement
limits belong in the lane reports, rather than assuming all Wi-Fi 7 or M6
routers share that path. No hardware purchase or source dependency is selected.

## Findings and source handling

The two lane reports and acquisition records are complete in `papers/` and
linked from the possibility map and research index. Exact MR6150 documentation
confirms its X62 platform, Wi-Fi 6 and network/USB/display/battery interfaces.
The FCC spot-check report explicitly describes shared PCB layouts with other
M6 variants, while the filing's photographs include MR6110 labels and MR6500
silkscreen. Root viewed two board figures as well. Preserve visible chip
markings as family evidence; do not turn them into an exact-unit BOM. The
application CPU, OS, RAM/storage and programmable raw-RF access remain unknown.

The Wi-Fi 7 lane acquired W1700K SDR source at the recorded exact revision and
studied the radio, platform, stream and roadmap material. It describes actual
receive-only raw I/Q, replacement radio firmware and 10 GbE export, with host
throughput and calibration limits. These are author-reported results and
source-supported mechanisms, not measurements reproduced here. A polished
deck could expose its UI, but sample ingest/DSP would still need explicit
hardware, power and thermal provision. No new receiver is selected; identify
the networking stash before any acquisition proposal.

Preserved one new source archive and eight PDF downloads with manifests; the
technical sheet duplicates a previously acquired original. There are now twelve
source snapshots. Root checked both distinct MR6150 archive targets from the
NETGEAR catalog; both returned HTTP 404. Recorded the matching source bundle
gap in `SHOPPING_LIST.md`. No downloaded source was executed, no tools installed,
and no device was operated or opened.

Validated 84 relative document links, the shared doctrine symlink, project-only
Git scope and diff whitespace. This checkpoint changes research documents only;
no source or device tests were run. Publish the checkpoint on the existing
research branch and refresh its pull request.
