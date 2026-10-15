# porter_ricks

Explore the Flipper Zero as a complete embedded system, with a likely destination
of an owned, full custom firmware stack.

The starting point is a physical device connected to a Mac over USB-C. The first
job is to understand the hardware, installed software, interfaces, and recovery
paths. That exploration will inform what we build, how far down the stack we
replace existing software, and which experiments give us useful answers first.

**Status:** read-only device inventory and parallel hardware, firmware, and
recovery research. The unit reports dev firmware 0.81.1 from 2023, hardware code
12, and working internal/microSD filesystems. No firmware has been built or
flashed. Language, runtime, dependencies, and replacement boundaries remain open.

**Current focus:** understand the growing equipment collection and discuss
portable instrument possibilities before further device experiments. New
research covers ESP32 raw-I/Q SDR, complementary module roles, and physical forms.

## Start here

- [Project brief and exploration sequence](docs/PROJECT.md)
- [Device inventory and repeatable collector](docs/DEVICE.md)
- [First reconnaissance: findings and next experiments](docs/RECONNAISSANCE.md)
- [Portable instrument possibilities](docs/POSSIBILITIES.md)
- [Growing hardware inventory](docs/HARDWARE_INVENTORY.md)
- [Primary sources and open research questions](papers/README.md)
- [Issue index](ISSUES.md) and [GitHub issues](https://github.com/antimeme-ai/porter_ricks/issues)
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
