# Interface methods and protocol-tool acquisitions

Acquired 2026-10-15 for the
[measurement-method report](2026-10-15-interface-measurement-methods.md) and
[claim/tool check](2026-10-15-interface-tool-claims.md). Originals remain ignored;
reports contain analysis and links. No acquired source was built, imported,
installed or executed. No dependency or hardware adoption occurred.

## Originals

| Item | Original path | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| [GS1 Gen2 3.0.1](https://ref.gs1.org/standards/gen2/3.0.1/) | papers/interface-methods/gs1-gen2-3.0.1-2026.pdf | 3758225 | 0dc79b03a8c3b1a1497b4f6b7843d4192399e76e8ba7641bde7952be43b263b9 |
| [Huntron ASA extract](https://huntron.com/sales-support/pdf/ASA-paper-extract.pdf) | papers/interface-methods/huntron-asa-extract.pdf | 2172636 | 0631a44ff8a40e91d7c26ead48e7064fb45599c871c7007fea22908cdaace495 |
| [Keysight VNA time-domain HTML](https://helpfiles.keysight.com/csg/m9485a/applications/timedomain.htm) | quarantine/interface-methods/keysight-vna-time-domain.html | 58707 | 5bbbf73f23162615edfa97c98aeb4769f4433858df54240033ee60753b2c31b5 |
| [urh source 1403d92987cc3d01d41aff64250955ce455dabd2](https://codeload.github.com/jopohl/urh/tar.gz/1403d92987cc3d01d41aff64250955ce455dabd2) | quarantine/interface-methods/urh-1403d92987cc3d01d41aff64250955ce455dabd2.tar.gz | 13188059 | 59d81ec4a950887617590afe982bee12e3eb49360eb4dce8cafdc8a962c0f428 |
| [netzob source 088fe769e98e0bfbd3ed99e66b3982446bf8d197](https://codeload.github.com/netzob/netzob/tar.gz/088fe769e98e0bfbd3ed99e66b3982446bf8d197) | quarantine/interface-methods/netzob-088fe769e98e0bfbd3ed99e66b3982446bf8d197.tar.gz | 5198824 | 70c28e70fa80a70a1bf322ce6e8e06f1365e4aa261e3a48d415e4eee5f490cae |

## Exact read scope and rights

- GS1: retained release 3.0.1, Ratified February 2026, 204 pages. Read introduction
  and scope at printed pp. 14–15 and tag-backscatter physical-layer text at
  pp. 39–40, plus edition identification. Not an exhaustive standards audit or
  claim of implementing optional commands. Original GS1 copyright/terms remain.
- Huntron: retained publisher's 19-page extract, not the full 51-page manual.
  Read printed pp. 7–16: ASA source model, nonlinear/reactive signatures,
  comparison, ranges and stimulus. No original plot used as numerical design
  data; no redistribution permission inferred from public download.
- Keysight: original HTML bytes, not a source-code archive. Read overview,
  frequency-to-time transform, calibration plane, resolution/span/window and
  range/alias/loss discussion. No linked images/dependencies acquired, no
  numerical accuracy claim on our hardware. Keysight notices remain upstream.
- URH: README/license and selected source
  src/urh/ainterpretation/AutoInterpretation.py (detector/estimator paths) and
  src/urh/awre/FormatFinder.py (initialization and field-engine selection).
  Exact pin 1403d92987cc3d01d41aff64250955ce455dabd2, commit 2025-12-19.
  GPLv3 notice in LICENSE; retained tree is a reference, not adopted code.
- Netzob: README.rst/COPYING.txt and selected source
  src/netzob/Inference/Vocabulary/FormatOperations/ClusterByAlignment.py and
  FormatOperations/FieldSplitAligned/FieldSplitAligned.py (documented method,
  clustering/dispatch and alignment paths). Exact pin
  088fe769e98e0bfbd3ed99e66b3982446bf8d197, commit 2023-01-08.
  COPYING.txt contains GPLv3; file headers specify GPLv3-or-later. Neither full
  algorithms nor runtime/dependency compatibility were validated.

Current repository/archive state was read from GitHub metadata and primary
project pages. URH was archived on the research date. Local copies do not
include subsequent upstream changes; no submodules or dependencies were fetched.
API acquisition metadata in ignored quarantine is working provenance.

## Extraction and restoration

The two tar.gz originals were preserved byte-for-byte. Source files were
extracted under quarantine/interface-methods/urh and netzob, dropping the single
archive-root directory. Only ordinary files/directories were retained; absolute
and traversal paths were rejected. Nested .git, .DS_Store, __MACOSX and AppleDouble
entries are excluded. No links/special entries or excluded detritus occurred.
Archived instructions have no workspace authority.

From repository root, download originals with these commands. Compare hashes
above before using a restored copy; mutable publisher content can change.

```sh
mkdir -p papers/interface-methods quarantine/interface-methods
curl --fail --location 'https://ref.gs1.org/standards/gen2/3.0.1/' --output 'papers/interface-methods/gs1-gen2-3.0.1-2026.pdf'
curl --fail --location 'https://huntron.com/sales-support/pdf/ASA-paper-extract.pdf' --output 'papers/interface-methods/huntron-asa-extract.pdf'
curl --fail --location 'https://helpfiles.keysight.com/csg/m9485a/applications/timedomain.htm' --output 'quarantine/interface-methods/keysight-vna-time-domain.html'
curl --fail --location 'https://codeload.github.com/jopohl/urh/tar.gz/1403d92987cc3d01d41aff64250955ce455dabd2' --output 'quarantine/interface-methods/urh-1403d92987cc3d01d41aff64250955ce455dabd2.tar.gz'
curl --fail --location 'https://codeload.github.com/netzob/netzob/tar.gz/088fe769e98e0bfbd3ed99e66b3982446bf8d197' --output 'quarantine/interface-methods/netzob-088fe769e98e0bfbd3ed99e66b3982446bf8d197.tar.gz'
```

For source archives, restore only into fresh directories using the following
owned extraction procedure; it does not execute upstream code.

```sh
python3 - <<'RESTORE'
from pathlib import Path, PurePosixPath
import tarfile

base = Path('quarantine/interface-methods')
items = (
    ('urh-1403d92987cc3d01d41aff64250955ce455dabd2.tar.gz', 'urh'),
    ('netzob-088fe769e98e0bfbd3ed99e66b3982446bf8d197.tar.gz', 'netzob'),
)
for original, name in items:
    destination = base / name
    assert not destination.exists(), 'Use a fresh tree; preserve existing notes.'
    destination.mkdir()
    with tarfile.open(base / original, 'r:gz') as archive:
        for member in archive:
            raw = PurePosixPath(member.name)
            if raw.is_absolute() or '..' in raw.parts:
                raise ValueError(member.name)
            parts = raw.parts[1:]
            if not parts or any(p in ('.git', '.DS_Store', '__MACOSX')
                                or p.startswith('._') for p in parts):
                continue
            target = destination.joinpath(*parts)
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.extractfile(member) as source:
                    target.write_bytes(source.read())
RESTORE
```
Derived PDF text is only a reading aid under ignored context/interface-methods,
created with the existing pdftotext -layout. No tool installation was needed.

## Download gaps

- Keysight 5950-3000, Impedance Measurement Handbook 6th Edition:
  https://go.keysight.com/us/en/assets/7018-06840/application-notes/5950-3000.pdf
  returned HTTP 403; the corresponding www.keysight.com URL served HTML rather
  than a PDF. No local original or claim of reading the handbook.
- Keysight 5989-5723, Time Domain Analysis Using a Network Analyzer:
  https://literature.cdn.keysight.com/litweb/pdf/5989-5723EN.pdf returned HTTP 403.
  The official HTML help above was read/acquired instead. A separate archived
  TDR app-note URL also returned HTML, not a PDF.
- ADI AN-1302 direct PDF acquisition timed out; the web tool redirected to the
  primary HTML app note. This was a supporting lead, not a retained source or
  a required basis for either report. No claim that its full text was read.

The two full Keysight references are useful later acquisition targets and are
listed in SHOPPING_LIST.md. They do not block the conclusions supported by the
retained and linked primary sources.
