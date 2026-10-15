# r1337

Nomad science in a man-portable field instrument. The name pays homage to the
General Dynamics R8000 the operator has long coveted. The project began as
`porter_ricks`; its broader scope led to the rename.

Develop a portable instrument with as much useful RF, electromagnetic,
debugging, sensing and device-firmware access capability as we can integrate
into a polished, man-portable field service-monitor form for the first version. A
secondary focus is interfacing with and managing heterogeneous control systems
across vendors and generations.
Camera and basic environmental sensing are desirable tertiary capabilities.

The starting point was a Flipper Zero connected to a Mac over USB-C. The growing
hardware collection now informs a broader instrument. Flipper exploration and
an owned custom firmware stack remain possible parts of that system; their
roles will follow from research and design.

For the later software-loadout discussion, **TMTSOYP is to be resurrected as a
core application**. Its previous implementation and role will be revisited then.

**Status:** read-only device inventory and parallel hardware, firmware, and
recovery research. The unit reports dev firmware 0.81.1 from 2023, hardware code
12, and working internal/microSD filesystems. No firmware has been built or
flashed. Language, runtime, dependencies, and replacement boundaries remain open.

**Current focus:** turn the research and growing equipment inventory into a
reviewed system design. The [first architecture](docs/ARCHITECTURE.md) proposes
local acquisition, a host for UI/records, remote assistance and an articulated
service-monitor body. Its [capability matrix](docs/CAPABILITIES.md) distinguishes
stash candidates from measurement gaps. Board choices and performance targets
remain open; further device experiments and implementation follow detailed design.

## Start here

- [Project brief and exploration sequence](docs/PROJECT.md)
- [First system architecture](docs/ARCHITECTURE.md) and [capability matrix](docs/CAPABILITIES.md)
- [Acquisition/interface engine comparison and behavior](docs/ACQUISITION.md)
- [Device inventory and repeatable collector](docs/DEVICE.md)
- [First reconnaissance: findings and next experiments](docs/RECONNAISSANCE.md)
- [Portable instrument possibilities](docs/POSSIBILITIES.md)
- [Growing hardware inventory](docs/HARDWARE_INVENTORY.md)
- [Aftermarket survey and unusual interface opportunities](papers/2026-10-15-aftermarket-and-interface-synthesis.md)
- [Primary sources and open research questions](papers/README.md)
- [Issue index](ISSUES.md) and [GitHub issues](https://github.com/antimeme-ai/r1337/issues)
- [Project journal](journal/2026-10-15-bootstrap.md)
- [Reconnaissance journal](journal/2026-10-15-reconnaissance.md)
- [Working instructions](AGENTS.md) and [quarantine manifest](QUARANTINE.md)

## Working regime

This project follows Blackbird. `BLACKBIRD.md` is a symlink to
`../BLACKBIRD.md`, the shared workspace doctrine. A standalone checkout needs
the operator's current doctrine beside the checkout; the shared document's
contents are outside this repository.

Research and source study precede architecture and implementation. We own the
required machinery and discuss proposed library adoption before adopting it.
Reference implementations teach us; acquiring them does not select a dependency.

Literature and research reports live in `papers/`. Acquired PDFs are ignored.
Reference implementations and intact source archives live in ignored
`quarantine/`, with sources and restoration commands recorded in `QUARANTINE.md`.
Raw device output, backups, and working logs belong in ignored `context/`.
Actions and decisions go in `journal/`; work is tracked in GitHub issues with a
local index. Empty ignored directories can be recreated with:

```sh
mkdir -p context quarantine
```

There is no project license selection yet.
