# Weird instrument reference acquisitions — 2026-10-15

Owner: hardware/instrument frumentarii lane. Research inputs only. No downloaded
source was run or selected as a dependency. Original archive/PDF bytes are retained
under ignored `quarantine/weird-devices/instruments/archives/`.

## Glasgow source snapshot

- Upstream: <https://github.com/GlasgowEmbedded/glasgow>.
- Revision: `d259cd44f643e9762b529f9e92b3c4ca758fe0aa`; upstream commit date
  2026-10-15T08:44:09Z (GitHub API inspected at acquisition).
- Exact archive: <https://codeload.github.com/GlasgowEmbedded/glasgow/tar.gz/d259cd44f643e9762b529f9e92b3c4ca758fe0aa>.
- Local archive:
  `quarantine/weird-devices/instruments/archives/GlasgowEmbedded--glasgow--d259cd44f643e9762b529f9e92b3c4ca758fe0aa.tar.gz`.
- Size: 51,676,789 bytes.
- SHA-256: `dc65dbfc6059e46b34f303e762674624aadc270c744f5b34b48cbe648e328fba`.
- Extracted tree: `quarantine/weird-devices/instruments/GlasgowEmbedded--glasgow/`.
- Sanitization: strip the archive's leading directory; omit `.git`, `.DS_Store`,
  `__MACOSX`, `__pycache__`, and `._*`; reject path traversal and omit link entries.
  Original archive remains intact. No submodules/dependencies fetched.
- Read: `docs/manual/src/intro.rst`, `revisions/index.rst`, portions of
  `revisions/revC3.rst`, `develop/applet.rst`, and
  `software/glasgow/applet/measure/curve_trace/__init__.py`. Other files retained
  for subsequent research, not claimed read.
- License source: root `LICENSE*` and `docs/manual/src/license.rst`; component
  notices remain in the snapshot. No license assessment or adoption performed.

## LibreVNA manual

- Upstream: <https://github.com/jankae/LibreVNA>.
- Revision: `c47781910221ba2b02636229920a7c8d48aeb8f8`; upstream commit date
  2026-10-04T15:52:44Z (GitHub API inspected at acquisition).
- Exact PDF: <https://raw.githubusercontent.com/jankae/LibreVNA/c47781910221ba2b02636229920a7c8d48aeb8f8/Documentation/UserManual/manual.pdf>.
- Local file:
  `quarantine/weird-devices/instruments/archives/LibreVNA--c47781910221ba2b02636229920a7c8d48aeb8f8--manual.pdf`.
- Size: 3,403,243 bytes.
- SHA-256: `ae8c3d627242322914778a2a5bc7b698c626d9157412ab142f702719e466a6e8`.
- Kept intact; no source-tree extraction or source acquisition.
- Read with the already-installed `pdftotext`: power/data section 1.1; data-flow
  and export context 3.1; selected calibration sections 3.5; fixture-removal
  sections 3.6. No exhaustive full-manual reading claimed.
- License/source locations: upstream root notices and hardware/FPGA/software
  directories. These were located, not evaluated for adoption.

## Restoration

Run from the project root. This downloads the same original external bytes and
recreates the sanitized reference tree without executing project code. It is a
restoration recipe, not a checked-in project utility or dependency.

```sh
python3 - <<'PY'
from pathlib import Path, PurePosixPath
import hashlib
import tarfile
import urllib.request

base = Path('quarantine/weird-devices/instruments')
archives = base / 'archives'
archives.mkdir(parents=True, exist_ok=True)
items = (
    ('GlasgowEmbedded--glasgow--d259cd44f643e9762b529f9e92b3c4ca758fe0aa.tar.gz',
     'https://codeload.github.com/GlasgowEmbedded/glasgow/tar.gz/d259cd44f643e9762b529f9e92b3c4ca758fe0aa',
     'dc65dbfc6059e46b34f303e762674624aadc270c744f5b34b48cbe648e328fba'),
    ('LibreVNA--c47781910221ba2b02636229920a7c8d48aeb8f8--manual.pdf',
     'https://raw.githubusercontent.com/jankae/LibreVNA/c47781910221ba2b02636229920a7c8d48aeb8f8/Documentation/UserManual/manual.pdf',
     'ae8c3d627242322914778a2a5bc7b698c626d9157412ab142f702719e466a6e8'),
)
for name, url, expected in items:
    path = archives / name
    if not path.exists():
        request = urllib.request.Request(url, headers={'User-Agent': 'porter-ricks-research'})
        with urllib.request.urlopen(request, timeout=120) as response:
            path.write_bytes(response.read())
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, path

destination = base / 'GlasgowEmbedded--glasgow'
assert not destination.exists(), 'Use a fresh destination; preserve existing notes.'
destination.mkdir()
with tarfile.open(archives / items[0][0], 'r:gz') as archive:
    for member in archive:
        parts = PurePosixPath(member.name).parts[1:]
        if not parts or any(p in ('.git', '.DS_Store', '__MACOSX', '__pycache__')
                            or p.startswith('._') for p in parts):
            continue
        if member.name.startswith('/') or '..' in parts:
            raise ValueError(member.name)
        target = destination.joinpath(*parts)
        if member.isdir():
            target.mkdir(parents=True, exist_ok=True)
        elif member.isfile():
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.extractfile(member) as incoming:
                target.write_bytes(incoming.read())
        # Omit symlinks, hardlinks, device nodes, and other special entries.
PY
```

Document verification: inspect cited source text and the two acquired byte
digests; check extracted reference for nested Git metadata/filesystem detritus;
check report-relative links. Root integrates this manifest into the shared
quarantine index and journal. No essential blocked acquisition remains.
