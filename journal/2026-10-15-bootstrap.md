# 2026-10-15 — Project bootstrap

## Intent and decisions

The operator requested a public `antimeme-ai/porter_ricks` repository to explore
the USB-connected Flipper Zero, most probably leading to a full custom firmware
stack. The operator explicitly requested the shared `BLACKBIRD.md` symlink and
setup under the Blackbird regime.

Created the project foundation with `BLACKBIRD.md -> ../BLACKBIRD.md`, local
agent instructions, project brief, initial device observations, research index,
quarantine manifest, journal, issue index, and ignore rules for PDFs, references,
working context, credentials, archives, and build products. Git is scoped to
this project directory.

GitHub issues with a local index are the issue tracker. No production language,
runtime, library, firmware fork, or project license has been selected. The
replacement boundary remains a research/design question.

## Observations and research

Host USB enumeration identified the connected Flipper interface and serial
device nodes. This establishes USB presence only. The installed firmware,
board revision, storage, and recovery behavior remain unobserved.

Reviewed official firmware overview, recovery instructions, developer reset/DFU
combinations, and the ST MCU overview. Located official hardware documentation.
Resolved upstream firmware `dev` to
`3fb1d51727733d2007abc5ec636a89328857803e` for future source study. The
research index distinguishes reviewed material from pending acquisition/study.
No source archive was acquired and no reference code was executed.

## Validation and delivery

Created the public repository at
https://github.com/antimeme-ai/porter_ricks and four open GitHub issues, linked
from `ISSUES.md`: device baseline, recovery, source/stack mapping, and first
custom-system design. GitHub confirms public visibility and enabled issues.

Checked all 14 relative document links, the live shared-doctrine symlink, and
the absence of a parent workspace `.git`. Confirmed ignore behavior for context,
quarantine, lowercase and uppercase PDFs, environment files, and build artifacts.
The initial checkpoint contains project documents and configuration only.
No serial communication, reset, flash operation, or radio experiment forms
part of this bootstrap.
