# Recovery and ecosystem acquisitions — 2026-10-15

Reference acquisition for [the recovery reconnaissance](2026-10-15-recovery-frumentarii.md). No reference was built or executed, no package was installed, and no dependency was adopted. Archives retain their downloaded bytes. Extracted material has no `.git`, `.DS_Store`, AppleDouble `._*`, or `__MACOSX` entries. Archived instructions are historical material, never workspace instructions.

These are **top-level source snapshots**, with submodules deliberately unpopulated: the studied paths are present in the parent trees. They are not buildable recursive checkouts. `.gitmodules` records candidate upstream references; no claim is made that those dependency trees were acquired. qFlipper lists nanopb and Windows libwdi; the firmware forks list multiple libraries and the STM32WB copro repository.

## Source inventory

### flipperdevices/qFlipper

- Original: https://github.com/flipperdevices/qFlipper; resolved `dev` to `1d26683ff5b751f219a4e40443b7c8355eb39469` on 2026-10-15.
- Download: https://codeload.github.com/flipperdevices/qFlipper/tar.gz/1d26683ff5b751f219a4e40443b7c8355eb39469
- Archive: `quarantine/recovery/qFlipper-1d26683ff5b751f219a4e40443b7c8355eb39469.tar.gz`.
- SHA-256: `3c3f56f36b705a7ca6954c33b8957ecc9e63e5badbc0936fcfcecf5517f5152a`.
- Extracted: `quarantine/recovery/qFlipper-1d26683ff5b751f219a4e40443b7c8355eb39469/`.
- License: GPL-3.0; [upstream LICENSE](https://github.com/flipperdevices/qFlipper/blob/1d26683ff5b751f219a4e40443b7c8355eb39469/LICENSE), retained in the extracted tree. This is the parent project license; third-party material can have additional licenses.
- Scope read: CLI, serial/RPC discovery, backup, repair, update and option-byte source.

### flipperzero-rs/flipperzero-rs

- Original: https://github.com/flipperzero-rs/flipperzero-rs; resolved `main` to `0a6779a49c9fca392794bf9723a7b7c10ae150e5` on 2026-10-15.
- Download: https://codeload.github.com/flipperzero-rs/flipperzero-rs/tar.gz/0a6779a49c9fca392794bf9723a7b7c10ae150e5
- Archive: `quarantine/recovery/flipperzero-rs-0a6779a49c9fca392794bf9723a7b7c10ae150e5.tar.gz`.
- SHA-256: `18d5a843a49c9b128458bffacf09bb060863a3467c4c81331a092233d1e0baee`.
- Extracted: `quarantine/recovery/flipperzero-rs-0a6779a49c9fca392794bf9723a7b7c10ae150e5/`.
- License: MIT; [upstream LICENSE](https://github.com/flipperzero-rs/flipperzero-rs/blob/0a6779a49c9fca392794bf9723a7b7c10ae150e5/LICENSE), retained in the extracted tree. This is the parent project license; third-party material can have additional licenses.
- Scope read: README, application runtime, allocator and firmware API bindings.

### Next-Flip/Momentum-Firmware

- Original: https://github.com/Next-Flip/Momentum-Firmware; resolved `dev` to `d3f89dfe2ef6b01839201598e9be1590cba80322` on 2026-10-15.
- Download: https://codeload.github.com/Next-Flip/Momentum-Firmware/tar.gz/d3f89dfe2ef6b01839201598e9be1590cba80322
- Archive: `quarantine/recovery/Momentum-Firmware-d3f89dfe2ef6b01839201598e9be1590cba80322.tar.gz`.
- SHA-256: `fe5799ebb5f72a2ed810fd57ebd193877c064ab99486e8fbb84552f8a8b4b4ec`.
- Extracted: `quarantine/recovery/Momentum-Firmware-d3f89dfe2ef6b01839201598e9be1590cba80322/`.
- License: GPL-3.0; [upstream LICENSE](https://github.com/Next-Flip/Momentum-Firmware/blob/d3f89dfe2ef6b01839201598e9be1590cba80322/LICENSE), retained in the extracted tree. This is the parent project license; third-party material can have additional licenses.
- Scope read: README, F7 target, Furi initialization and reference submodule declarations.

### DarkFlippers/unleashed-firmware

- Original: https://github.com/DarkFlippers/unleashed-firmware; resolved `dev` to `d416e74edc338849b9c817228f44280b72cf936b` on 2026-10-15.
- Download: https://codeload.github.com/DarkFlippers/unleashed-firmware/tar.gz/d416e74edc338849b9c817228f44280b72cf936b
- Archive: `quarantine/recovery/unleashed-firmware-d416e74edc338849b9c817228f44280b72cf936b.tar.gz`.
- SHA-256: `7ca5117764008e20a4372f03d3f4c5861a232e6c2e74268f74462a7425a06727`.
- Extracted: `quarantine/recovery/unleashed-firmware-d416e74edc338849b9c817228f44280b72cf936b/`.
- License: GPL-3.0; [upstream LICENSE](https://github.com/DarkFlippers/unleashed-firmware/blob/d416e74edc338849b9c817228f44280b72cf936b/LICENSE), retained in the extracted tree. This is the parent project license; third-party material can have additional licenses.
- Scope read: README, F7 target, Furi initialization and reference submodule declarations.

## Restore the acquired snapshots

Run from the project root with Python 3. The following uses only the standard library and downloads immutable commit archives, checks the recorded digest, rejects archive traversal/link entries, extracts, and removes filesystem detritus. It does not populate submodules or execute acquired code.

```sh
python3 - <<'PY'
from pathlib import Path, PurePosixPath
import hashlib, shutil, tarfile, urllib.request
root = Path('quarantine/recovery')
root.mkdir(parents=True, exist_ok=True)
sources = [
    ('flipperdevices/qFlipper', '1d26683ff5b751f219a4e40443b7c8355eb39469', '3c3f56f36b705a7ca6954c33b8957ecc9e63e5badbc0936fcfcecf5517f5152a'),
    ('flipperzero-rs/flipperzero-rs', '0a6779a49c9fca392794bf9723a7b7c10ae150e5', '18d5a843a49c9b128458bffacf09bb060863a3467c4c81331a092233d1e0baee'),
    ('Next-Flip/Momentum-Firmware', 'd3f89dfe2ef6b01839201598e9be1590cba80322', 'fe5799ebb5f72a2ed810fd57ebd193877c064ab99486e8fbb84552f8a8b4b4ec'),
    ('DarkFlippers/unleashed-firmware', 'd416e74edc338849b9c817228f44280b72cf936b', '7ca5117764008e20a4372f03d3f4c5861a232e6c2e74268f74462a7425a06727'),
]
for repo, revision, expected in sources:
    name = repo.split('/')[-1]
    archive = root / (name + '-' + revision + '.tar.gz')
    url = 'https://codeload.github.com/' + repo + '/tar.gz/' + revision
    urllib.request.urlretrieve(url, archive)
    if hashlib.sha256(archive.read_bytes()).hexdigest() != expected:
        raise RuntimeError('Archive digest mismatch: ' + str(archive))
    with tarfile.open(archive) as source:
        for member in source.getmembers():
            path = PurePosixPath(member.name)
            if path.is_absolute() or '..' in path.parts or member.issym() or member.islnk():
                raise RuntimeError('Unsafe archive member: ' + member.name)
        source.extractall(root)
    extracted = root / (name + '-' + revision)
    for path in sorted(extracted.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if path.name in ('.git', '.DS_Store', '__MACOSX') or path.name.startswith('._'):
            shutil.rmtree(path) if path.is_dir() else path.unlink()
PY
```

Acquisition used GitHub REST commit resolution (`GET /repos/{owner}/{repo}/commits/{branch}`), followed by the exact codeload URLs above. The first qFlipper extraction attempted `extractall(filter="data")`; the host Python lacks that argument, so extraction was rerun with explicit member validation before `extractall()`. Archive bytes were unaffected.
