# ESP32 SDR acquisitions — 2026-10-15

Research report:
[ESP32 SDR reconnaissance](2026-10-15-esp32-sdr-reconnaissance.md).

## Source snapshots

GitHub HEAD was resolved using its public API, then each exact commit's codeload
archive was downloaded. Original archives remain intact under ignored
`quarantine/esp32-sdr/archives/`. Extraction filtered `.git`, `.DS_Store`,
`__MACOSX`, Apple `._*` entries and archive links; it rejected path traversal.
A scan of extracted trees found no nested Git metadata, Python bytecode/cache,
or filesystem detritus. Archived instructions are historical reference only.

| Source | Exact revision | Archive bytes | SHA-256 |
| --- | --- | ---: | --- |
| [ESPARGOS/esp-sdr](https://github.com/ESPARGOS/esp-sdr) | `e2b35dc593a378e4c5eb69cb8db59313117c9838` | 4,145,463 | `55b988483bd25c661564216f7539253106875be8cb807a3e3276b271ae0d7ae4` |
| [cyber-murmel/esp-sdr-zephyr](https://github.com/cyber-murmel/esp-sdr-zephyr) | `8463f88f6d59c4cd1c657169d80ae099b5eaf19d` | 502,010 | `eaa45d42a310a67ab969690fa73c82d4e02ecc4f2bed891b525e24bf1358a1cb` |
| [h0m3us3r/eSpDR](https://github.com/h0m3us3r/eSpDR) | `f279bf823eee41796dfd1ac21f13e1ed9b418c82` | 7,903,716 | `1650af2f8ef0f0fa32ae91c6303d9caaee6269e80d5a47f70078452ae32aa84e` |

Extracted roots are respectively `quarantine/esp32-sdr/ESPARGOS--esp-sdr/`,
`quarantine/esp32-sdr/cyber-murmel--esp-sdr-zephyr/`, and
`quarantine/esp32-sdr/h0m3us3r--eSpDR/`. Archive filenames use
`OWNER--REPO--REVISION.tar.gz` with the exact revisions above.

Restore from the project root with the standard library; this downloads and
extracts references and does not execute their source:

```sh
python3 - <<'PY'
from pathlib import Path, PurePosixPath
import shutil, tarfile, urllib.request
base = Path('quarantine/esp32-sdr')
(base / 'archives').mkdir(parents=True, exist_ok=True)
sources = (
    ('ESPARGOS', 'esp-sdr', 'e2b35dc593a378e4c5eb69cb8db59313117c9838'),
    ('cyber-murmel', 'esp-sdr-zephyr', '8463f88f6d59c4cd1c657169d80ae099b5eaf19d'),
    ('h0m3us3r', 'eSpDR', 'f279bf823eee41796dfd1ac21f13e1ed9b418c82'),
)
for owner, name, revision in sources:
    url = f'https://codeload.github.com/{owner}/{name}/tar.gz/{revision}'
    archive = base / 'archives' / f'{owner}--{name}--{revision}.tar.gz'
    with urllib.request.urlopen(url, timeout=120) as response:
        archive.write_bytes(response.read())
    destination = base / f'{owner}--{name}'
    destination.mkdir(exist_ok=True)
    with tarfile.open(archive, 'r:gz') as bundle:
        for member in bundle.getmembers():
            parts = PurePosixPath(member.name).parts[1:]
            if not parts or any(p in ('.git', '.DS_Store', '__MACOSX')
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

No submodules, Zephyr workspace dependencies, vendor blobs or toolchains were
downloaded. In particular ESPARGOS's `components/esp-dsp` submodule is not
populated, and Zephyr's `west.yml` dependencies are not fetched. These trees are
bounded source-reading references, not prepared build environments. Original
external JSON-format files in the snapshots remain upstream source material;
we created no internal JSON model or persistence format.

License source locations: each repository's root `LICENSE`; additionally
eSpDR's README identifies third-party PHY/startup notices, ESPARGOS's README
identifies derived FFT kernels and its S2 compatibility component, and the
Zephyr README/manifest identifies its external components. No dependency or
license selection for `porter_ricks` follows from acquisition.

## Literature

Acquired original:
`papers/esp32-sdr/2026-10-esp32-s3-iq-bridge-measurements.pdf` (ignored), 578,176
bytes, SHA-256
`2f36b3d73c5bc798cd21acdc70e9e51a656546918c3e74a1f5c22c4cd22bba04`.
The source is z2labs/esp-sdr-bridge at revision
`7da8aea5b667513dec8abd52675923cce1aefae3`, path
`docs/ESP32-S3_IQ_bridge_measurements.pdf`.

Restore:

```sh
mkdir -p papers/esp32-sdr
curl -fL --connect-timeout 10 --max-time 120 \
  -o papers/esp32-sdr/2026-10-esp32-s3-iq-bridge-measurements.pdf \
  'https://raw.githubusercontent.com/z2labs/esp-sdr-bridge/7da8aea5b667513dec8abd52675923cce1aefae3/docs/ESP32-S3_IQ_bridge_measurements.pdf'
```

Read the report's overview, transport, long-run and sweep results. The
reconnaissance records the measurement arrangement and its limits. No results
were reproduced. Espressif documentation, the ESPARGOS project page and the
other primary project pages cited in the reconnaissance were read live and were
not acquired as complete source archives. No inaccessible source in this lane
requires operator purchase or a shopping-list addition.
