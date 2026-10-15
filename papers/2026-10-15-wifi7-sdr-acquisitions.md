# Wi-Fi 7 SDR acquisitions — 2026-10-15

Research report:
[Wi-Fi 7 router SDR reconnaissance](2026-10-15-wifi7-sdr-reconnaissance.md).

## Acquired source

- Repository: [h0m3us3r/w1700k-sdr](https://github.com/h0m3us3r/w1700k-sdr).
- Exact revision: `0b0413e4309f0c083702fa4eb2d1c2bca4532163`.
- Commit date reported by GitHub: 2026-10-13 03:25:39 UTC.
- Original source archive URL:
  [pinned codeload archive](https://codeload.github.com/h0m3us3r/w1700k-sdr/tar.gz/0b0413e4309f0c083702fa4eb2d1c2bca4532163).
- Intact ignored archive:
  `quarantine/wifi7-sdr/archives/h0m3us3r--w1700k-sdr--0b0413e4309f0c083702fa4eb2d1c2bca4532163.tar.gz`.
- Archive size: 12,937,709 bytes.
- Archive SHA-256:
  `602cbff06dbbbecba968f5970fbe432c9d4f52115130b9764d16bc248c8fff02`.
- Extracted ignored tree: `quarantine/wifi7-sdr/h0m3us3r--w1700k-sdr/`.

Original archive bytes were preserved. Extraction filtered nested `.git`,
`.DS_Store`, `__MACOSX`, `__pycache__` and Apple `._*` entries, skipped links,
and rejected path traversal. Archived instructions remain historical reference.
No code was executed or built. None of the platform's external downloads,
toolchains, Linux/Buildroot trees, firmware images or runtime dependencies were
fetched. Original external JSON source files remain upstream material; no new
internal JSON persistence was created.

Restore from the project root:

```sh
python3 - <<'PY'
from pathlib import Path, PurePosixPath
import shutil, tarfile, urllib.request
revision = '0b0413e4309f0c083702fa4eb2d1c2bca4532163'
base = Path('quarantine/wifi7-sdr')
(base / 'archives').mkdir(parents=True, exist_ok=True)
archive = base / 'archives' / f'h0m3us3r--w1700k-sdr--{revision}.tar.gz'
url = f'https://codeload.github.com/h0m3us3r/w1700k-sdr/tar.gz/{revision}'
with urllib.request.urlopen(url, timeout=120) as response:
    archive.write_bytes(response.read())
destination = base / 'h0m3us3r--w1700k-sdr'
destination.mkdir(exist_ok=True)
with tarfile.open(archive, 'r:gz') as bundle:
    for member in bundle.getmembers():
        parts = PurePosixPath(member.name).parts[1:]
        if not parts or any(p in ('.git', '.DS_Store', '__MACOSX', '__pycache__')
                            or p.startswith('._') for p in parts):
            continue
        if member.issym() or member.islnk():
            continue
        relative = Path(*parts)
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError(member.name)
        target = destination / relative
        if member.isdir():
            target.mkdir(parents=True, exist_ok=True)
        elif member.isfile():
            target.parent.mkdir(parents=True, exist_ok=True)
            with bundle.extractfile(member) as source, target.open('wb') as out:
                shutil.copyfileobj(source, out)
PY
```

License-source locations are the root `LICENSE`, full texts in `LICENSES/`, and
per-file SPDX identifiers. The report distinguishes the project's radio-firmware
ownership claim from retained ROM, stock first-stage boot software and external
platform inputs. No dependency or project license decision follows from reading
this reference.

## What was read

Read the root README; `docs/architecture.md`; `docs/roadmap.md`;
`firmware/README.md`; `platform/README.md`; `kernel/w1700k_sdr/README.md`;
`host/stream/README.md`; `host/spectrum/README.md`; and `host/recv/README.md`.
Inspected selected packing assembly and kernel export source to ground the
format/throughput account. This is a bounded source reconnaissance, not a code
audit or an experimental replication.

Also read primary NETGEAR MR6150 specifications, the openwifi repository overview,
and Wegemer/Mantovani's Nullcon 2025 slides through web access. The conference
PDF's original URL returned HTTP 403 during local download, so no local PDF was
acquired. That background document is readable online and is not necessary to
restore the W1700K source; no operator acquisition request is raised for it.
