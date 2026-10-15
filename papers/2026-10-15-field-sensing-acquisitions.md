# Field-sensing reference acquisitions — 2026-10-15

Supports [the field-sensing report](2026-10-15-field-sensing-frumentarii.md). Two original source archives were acquired for direct study. No source was built/executed, dependency adopted, package installed or device accessed. Original downloaded bytes remain intact; extracted trees were screened for traversal/link entries, then `.git`, `.DS_Store`, AppleDouble `._*` and `__MACOSX` detritus were removed. Archived instructions have no authority in this workspace. No submodule acquisition was needed for the paths studied.

## tricorderproject/cyberdeck

- Original: https://github.com/tricorderproject/cyberdeck
- Resolved `main` on 2026-10-15 to `b2b8410a905fe13b079b8bc42ec15af540e23f07`; commit date `2026-09-27T22:10:48Z`. Archive acquisition date does not imply current development or manufacturing.
- Exact archive URL: https://codeload.github.com/tricorderproject/cyberdeck/tar.gz/b2b8410a905fe13b079b8bc42ec15af540e23f07
- Archive: `quarantine/weird-devices/field-sensing/cyberdeck-b2b8410a905fe13b079b8bc42ec15af540e23f07.tar.gz`.
- SHA-256: `f881e195ed5493379b9c0958faece208e5b98322244c88f3f1de1733c0e30804`.
- Extracted tree: `quarantine/weird-devices/field-sensing/cyberdeck-b2b8410a905fe13b079b8bc42ec15af540e23f07/`.
- License source: README.md License section: physical/non-code design and documentation CC BY 4.0; code licensing is described by the author in that section and inherited third-party terms are not resolved here. No blanket permissive code license is inferred.
- Scope read: README/errata; ESP32 loop; Python sensor/thermal/visible/UI drivers; OpenSCAD sensor-holder and camera-mount sections; assembled-back photo.

## tricorderproject/arducordermini

- Original: https://github.com/tricorderproject/arducordermini
- Resolved `master` on 2026-10-15 to `e6ff23335c06cd4f6410152471ade1856c504c26`; commit date `2014-11-10T00:58:48Z`. Archive acquisition date does not imply current development or manufacturing.
- Exact archive URL: https://codeload.github.com/tricorderproject/arducordermini/tar.gz/e6ff23335c06cd4f6410152471ade1856c504c26
- Archive: `quarantine/weird-devices/field-sensing/arducordermini-e6ff23335c06cd4f6410152471ade1856c504c26.tar.gz`.
- SHA-256: `fb8e295ff277857efc06e41651d2a7c8e67292cd3f9f53c6ded7822e14cbcb11`.
- Extracted tree: `quarantine/weird-devices/field-sensing/arducordermini-e6ff23335c06cd4f6410152471ade1856c504c26/`.
- License source: LICENSES.TXT: hardware/supporting material CC BY-SA 4.0; author software has BSD two-clause terms; included third-party libraries retain their own licenses.
- Scope read: README/LICENSES.TXT; firmware/test2k/TileGUI.h and SensorBuffer.cpp for historical UI/data patterns.

## Restoration

Run from the repository root. This uses Python standard-library modules, preserves the source archives, checks their digests, validates member paths before extraction, and sanitizes only extracted material. It does not execute acquired code.

```sh
python3 - <<'PY'
from pathlib import Path, PurePosixPath
import hashlib, shutil, tarfile, urllib.request
root = Path('quarantine/weird-devices/field-sensing')
root.mkdir(parents=True, exist_ok=True)
sources = [
    ('tricorderproject/cyberdeck', 'b2b8410a905fe13b079b8bc42ec15af540e23f07', 'f881e195ed5493379b9c0958faece208e5b98322244c88f3f1de1733c0e30804'),
    ('tricorderproject/arducordermini', 'e6ff23335c06cd4f6410152471ade1856c504c26', 'fb8e295ff277857efc06e41651d2a7c8e67292cd3f9f53c6ded7822e14cbcb11'),
]
for repo, revision, expected in sources:
    name = repo.split('/')[-1]
    archive = root / (name + '-' + revision + '.tar.gz')
    urllib.request.urlretrieve('https://codeload.github.com/' + repo + '/tar.gz/' + revision, archive)
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

Acquisition resolved exact commits with GitHub REST (`GET /repos/{owner}/{repo}/commits/{branch}`) and downloaded the codeload URLs above. Other report sources were read through their original project/vendor sites; no additional source/PDF archive was acquired.
