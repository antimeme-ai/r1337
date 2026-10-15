# Interface aftermarket acquisitions — 2026-10-15

Research inputs for [the lane report](2026-10-15-interface-aftermarket-frumentarii.md).
No source executed, built or installed. No dependency or hardware adoption.
Original bytes live under ignored `quarantine/aftermarket-interfaces/archives/`;
reference extraction directories are beside `archives/`.

## Retained originals and exact sources

| Item | Filename under archives/ | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| Tigard source | `tigard--0dd58e710374880a3ae988f2ddfeb46f5ec8061d.tar.gz` | 1079790 | `e39ff9835fa3e43e71a5dfeac434ec71a5b1a131d16685927c1b8940da64b9e9` |
| HydraLINCAN source | `HydraLINCAN--5f50c83c4ea8876f1bbe63501c6c8923ef46976c.tar.gz` | 3050889 | `5fe4c4397e235e27cd16fd1ad41549825098653f8915924c80d329be3334d98c` |
| Gladiolus source | `gladiolus--b3314cb6485b9ae5e5e829c1d1dc9c63d02bbe4d.tar.gz` | 163357 | `0647d55f8f51a75a44c14cf242750c97949ae6122ac0c771e71df63a0aff9169` |
| TI ISO14xx original datasheet, Rev. I, August 2026 | `iso1410--vendor-2026-10-15.pdf` | 2345405 | `82abfbcca01cb38301afa22717bd25cf16a2a37b1e609bb66a75fde72b14b7eb` |
| BP dual-RS232 native schematic | `bp-rs232-dual--acb9cd667ce608e7eb560a663938787343b424c4.kicad_sch` | 101720 | `1d309aca1a0194e2dfeaecde24fb167fd4b38bcd631ca4e4fd73ae534746deb6` |

Exact URLs, pins, read scope and notice locations:

- **Tigard**, revision `0dd58e710374880a3ae988f2ddfeb46f5ec8061d`, upstream
  commit date 2026-10-08T01:56:44Z:
  <https://codeload.github.com/tigard-tools/tigard/tar.gz/0dd58e710374880a3ae988f2ddfeb46f5ec8061d>.
  Extracted `tigard/`. Read README sections on interfaces, selectors, I2C
  limitations, headers/accessories, and schematic component content; no complete
  layout or timing audit. Notice: `tigard/LICENSE.txt` (CC BY-SA 4.0 text).
- **HydraLINCAN**, revision `5f50c83c4ea8876f1bbe63501c6c8923ef46976c`, upstream
  commit date 2023-03-29T13:17:53Z:
  <https://codeload.github.com/smillier/HydraLINCAN/tar.gz/5f50c83c4ea8876f1bbe63501c6c8923ef46976c>.
  Extracted `HydraLINCAN/`. Read README, `HydraLinCan_BOM.csv`, schematic component
  references and power/ground net membership in `HydraLinCan.sch`. No full
  automotive-transient qualification or firmware audit. No standalone license
  file identified in this archive; embedded library notices remain intact. Do
  not infer the hardware's terms from HydraFW's separate source license.
- **Gladiolus**, revision `b3314cb6485b9ae5e5e829c1d1dc9c63d02bbe4d`, upstream
  commit date 2021-12-06T20:13:06Z:
  <https://codeload.github.com/greatfet-hardware/gladiolus/tar.gz/b3314cb6485b9ae5e5e829c1d1dc9c63d02bbe4d>.
  Extracted `gladiolus/`. Read README's purpose, wavelength, coupling and sampled
  receive example; schematic component list for ADC/DAC/gain/photodiode path.
  GreatFET host `gnuradio/gladiolus.py` was read live, not acquired or executed.
  Notice: `gladiolus/LICENSE` (CERN-OHL-P v2 text).
- **TI ISO14xx**:
  <https://www.ti.com/lit/ds/symlink/iso1410.pdf>.
  Vendor URL is mutable; retained bytes identify SLLSF22I, April 2018/revised
  August 2026. Read first-page feature/supply/rate distinctions, relevant pin
  supply definitions and section 9 overview through the already-installed
  `pdftotext`. No diagram-derived insulation or assembly-rating claim. Notices
  and terms remain in the original TI PDF.
- **Bus Pirate dual-RS232 schematic**, hardware repo revision
  `acb9cd667ce608e7eb560a663938787343b424c4`, upstream commit date
  2025-11-04T12:10:14Z:
  <https://raw.githubusercontent.com/DangerousPrototypes/BusPirate5-hardware/acb9cd667ce608e7eb560a663938787343b424c4/adapter-rs232-dual-1REV0/rs232-dual-adapter.kicad_sch>.
  Original native text, no transformation/extraction. Inspected MAX3232
  component references and visible ground/isolator context alongside the official
  accessory page. No PCB audit or guaranteed isolation claim. Consult upstream
  hardware/documentation notices; no standalone license was acquired with this
  individual file and no license conclusion is made. The upstream root
  [LICENSE.TXT](https://github.com/DangerousPrototypes/BusPirate5-hardware/blob/acb9cd667ce608e7eb560a663938787343b424c4/LICENSE.TXT)
  was located separately; it was not acquired with the schematic.

Source commit dates were read from GitHub's external API. The archive originals
were never modified. Extracted references omit nested `.git`, `.DS_Store`,
`__MACOSX`, `__pycache__`, `._*`, backup/working-state `*.bak`, `*-bak` and
`*.kicad_prl`, and all links/special entries; traversal/absolute paths are
rejected. No matching entries required omission in these three archives. No
submodules, toolchains, dependencies or generated builds were fetched.

## Restoration

From the repository root, this recipe downloads the original bytes, checks
their acquisition digests and recreates only fresh sanitized extraction trees.
A later vendor PDF change intentionally fails the digest comparison. It does
not execute downloaded project code.

```sh
python3 - <<'PY'
from pathlib import Path, PurePosixPath
import hashlib
import shutil
import tarfile
import urllib.request

base = Path('quarantine/aftermarket-interfaces')
archives = base / 'archives'
archives.mkdir(parents=True, exist_ok=True)
items = (
    ('tigard--0dd58e710374880a3ae988f2ddfeb46f5ec8061d.tar.gz',
     'https://codeload.github.com/tigard-tools/tigard/tar.gz/0dd58e710374880a3ae988f2ddfeb46f5ec8061d',
     'e39ff9835fa3e43e71a5dfeac434ec71a5b1a131d16685927c1b8940da64b9e9', 'tigard'),
    ('HydraLINCAN--5f50c83c4ea8876f1bbe63501c6c8923ef46976c.tar.gz',
     'https://codeload.github.com/smillier/HydraLINCAN/tar.gz/5f50c83c4ea8876f1bbe63501c6c8923ef46976c',
     '5fe4c4397e235e27cd16fd1ad41549825098653f8915924c80d329be3334d98c', 'HydraLINCAN'),
    ('gladiolus--b3314cb6485b9ae5e5e829c1d1dc9c63d02bbe4d.tar.gz',
     'https://codeload.github.com/greatfet-hardware/gladiolus/tar.gz/b3314cb6485b9ae5e5e829c1d1dc9c63d02bbe4d',
     '0647d55f8f51a75a44c14cf242750c97949ae6122ac0c771e71df63a0aff9169', 'gladiolus'),
    ('iso1410--vendor-2026-10-15.pdf',
     'https://www.ti.com/lit/ds/symlink/iso1410.pdf',
     '82abfbcca01cb38301afa22717bd25cf16a2a37b1e609bb66a75fde72b14b7eb', None),
    ('bp-rs232-dual--acb9cd667ce608e7eb560a663938787343b424c4.kicad_sch',
     'https://raw.githubusercontent.com/DangerousPrototypes/BusPirate5-hardware/acb9cd667ce608e7eb560a663938787343b424c4/adapter-rs232-dual-1REV0/rs232-dual-adapter.kicad_sch',
     '1d309aca1a0194e2dfeaecde24fb167fd4b38bcd631ca4e4fd73ae534746deb6', None),
)
for name, url, expected, tree in items:
    original = archives / name
    if not original.exists():
        request = urllib.request.Request(url, headers={'User-Agent': 'r1337-reference-research'})
        with urllib.request.urlopen(request, timeout=90) as response:
            original.write_bytes(response.read())
    assert hashlib.sha256(original.read_bytes()).hexdigest() == expected, name
    if tree is None:
        continue
    destination = base / tree
    assert not destination.exists(), 'Preserve existing notes; restore into a fresh tree.'
    destination.mkdir()
    with tarfile.open(original, 'r:gz') as archive:
        for member in archive:
            parts = PurePosixPath(member.name).parts[1:]
            if not parts:
                continue
            if member.name.startswith('/') or '..' in parts:
                raise ValueError(member.name)
            if any(p in ('.git', '.DS_Store', '__MACOSX', '__pycache__')
                   or p.startswith('._') or p.endswith(('.bak', '-bak', '.kicad_prl'))
                   for p in parts):
                continue
            target = destination.joinpath(*parts)
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.extractfile(member) as source, target.open('wb') as output:
                    shutil.copyfileobj(source, output)
PY
```

## Located/read through web, originals not acquired

- ADI DS2482-100:
  <https://www.analog.com/media/en/technical-documentation/data-sheets/ds2482-100.pdf>.
  Web tool supplied the 24-page primary PDF text; read strong/active pull-up,
  timing and external pull-up-control discussion. Direct download timed out.
- ADI AD5700/AD5700-1:
  <https://www.analog.com/media/en/technical-documentation/data-sheets/ad5700_5700-1.pdf>.
  Web tool supplied the 24-page Rev. G primary PDF text; read overview/UART/FSK
  physical-layer discussion. Direct download timed out.
- NXP TDA8035:
  <https://www.nxp.com/docs/en/data-sheet/TDA8035.pdf>.
  Web tool supplied 32-page primary PDF text; read first-page power classes and
  automatic activation/deactivation/protection features. Direct acquisition
  returned 404. No local original exists.
- Bus Blaster old wiki pages returned access errors. Manufacturer v3 sheet was
  read at <https://media.digikey.com/pdf/Data%20Sheets/Seeed%20Technology/102990047_Web.pdf>;
  no local original retained.

These acquisition limits do not block this survey. Root can choose to list the
full originals for later acquisition if those circuits become active design
inputs. Neither repository archives nor documentation pages were exhaustively
audited. Verify actual board/firmware revision, data path, electrical domains
and measurement behavior before using any proposed role.
