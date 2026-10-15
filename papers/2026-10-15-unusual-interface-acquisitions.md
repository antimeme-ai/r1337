# Unusual-interface literature acquisition manifest

Acquired 2026-10-15 for the [research report](2026-10-15-unusual-interface-avenues.md).
Original PDFs are retained unchanged under ignored `papers/unusual-interfaces/`.
Derived text is under ignored `quarantine/unusual-interfaces/text/`. No executable
reference code, dependency, installation or hardware operation was involved.

These are original PDF documents, not source-code archives; no extracted tree
contains nested Git metadata or filesystem detritus. No PDF was rewritten or
sanitized. The text extraction is a reading aid, not a replacement original.
Publisher URLs can change; the SHA-256 values identify the exact acquired bytes.
There is no upstream Git revision for these PDF artifacts.

| Local original basename | Primary source / revision | SHA-256 |
| --- | --- | --- |
| `retrofab-chi2016.pdf` | [Autodesk author-hosted paper](https://www.research.autodesk.com/app/uploads/2023/03/retrofab-a-design-tool.pdf_recq46gvQ9Haa6erl.pdf), Ramakers, Anderson, Grossman & Fitzmaurice, CHI 2016, *RetroFab: A Design Tool for Retrofitting Physical Interfaces using Actuators, Sensors and 3D Printing* | `aa1932ed37e7156bb373d5cbad37ff45d2739e85629fd8886e4e0a802cdab96a` |
| `srs-lock-in-basics-2020.pdf` | [Stanford Research Systems technical note](https://www.thinksrs.com/downloads/pdfs/applicationnotes/Lock-In%20Basics.pdf), *Lock-In Amplifier Basics*, dated 07-Apr-20 | `af2d31f91ac5d381ffab6945fe98d6ef36aa3fa525d8d4db5c29d2cba688aed8` |
| `sweepsense-iui2016.pdf` | [Author-hosted paper](https://chrisharrison.net/projects/sweepsense/SweepSense.pdf), Laput, Chen & Harrison, IUI 2016, DOI 10.1145/2856767.2856812 | `88a5a66f4a59cf0be800c7aae02715c935e8ff017eeaea0b5309185d5e6da3c5` |
| `synthetic-sensors-chi2017.pdf` | [Author-hosted paper](https://chrisharrison.net/projects/syntheticsensors/syntheticsensors.pdf), Laput, Zhang & Harrison, CHI 2017, DOI 10.1145/3025453.3025773 | `ba6026ea9c1a68e0930b21625cf6374ea9cbaa5cda3e03d2eca22e69c30a8e8c` |
| `ti-tiducf0-optical-port-2016.pdf` | [TI TIDUCF0](https://www.ti.com/lit/ug/tiducf0/tiducf0.pdf), November 2016, TIDA-01212, *Single Bidirectional Infrared LED Communication Port Reference Design* | `5975527e614b223f43fbd7cbf24c011fad0f54ff4350d9676a7e9d825fb35bf3` |
| `ti-tidueg0-hart-input-2018.pdf` | [TI TIDUEG0](https://www.ti.com/lit/ug/tidueg0/tidueg0.pdf), October 2018, TIDA-060020, *HART Enabled PLC Analog Input Module Reference Design* | `7da6e3bf0a0ea804beb1b3c4498fb46f25de98e79abd3a3b9975c0f7f3f407dc` |

## Rights and source notices

Read the notices in the retained originals before reuse. Acquiring a readable
reference does not adopt code or grant republication rights.

- RetroFab, SweepSense and Synthetic Sensors retain ACM copyright and their
  first-page copying/permission notices. No open-source license is inferred.
  Originals/text remain ignored; the public report contains our analysis and
  primary links rather than redistributed papers. RetroFab's primary
  [publication landing page](https://www.research.autodesk.com/publications/retrofab-a-design-tool-for-retrofitting-physical-interfaces-using-actuators-sensors-and-3d-printing/)
  supplies publication context.
- SRS supplies the note as vendor educational literature. No explicit open
  content/source license was found in the note; no redistribution right is
  inferred from public download availability.
- TI's originals retain their copyright and end-of-document important notices.
  TIDUEG0's notice limits use of its resources to development involving the
  described TI products and prohibits other reproduction/display. These are
  reference literature, not permissively licensed assets for the project. No
  design/code reuse or publication of the PDFs is selected.

## What was read

- RetroFab: introduction/workflow, physical component/fixture descriptions,
  preliminary evaluation and limitations. Particularly the difference between
  demonstrated basic controls/light sensing and proposed future camera/display
  support; no general robotic HMI claim is carried forward.
- SRS: phase-sensitive detection, reference coherence, dual-phase results,
  narrow-band detection and interpretation of a waveform's selected component.
- SweepSense: signal generation/analysis, two example implementations, evaluation
  and limitations; classifiers require training and may be device/model specific.
- Synthetic Sensors: multimodal acquisition and evaluation, ground-truth labels,
  null instances, later-session evaluation, false triggers and limits of automatic
  event discovery.
- TI optical: system overview, optical implementation, spectral/alignment and
  receive-method details, demonstrated signaling limitations. CC1350/CC1310
  reference behavior is not assigned to the stash's CC1312R1.
- TI HART: block diagram, analog input/DC and AC modem coupling, loop/load roles
  and relevant physical-layer test discussion. No conformance claim on r1337.

Other primary sources were read in the browser and cited directly in the report:
PGA300 Rev. D configuration/OWI sections, ST UM0470 Rev. 4 activation sections,
Microchip UPDI physical interface, TI resolver SBAA144, ADI LVDT CN0288,
transducer excitation/RTD/thermocouple notes, Microchip magnetic-card-reader
encoding/frontend, TI SBOA200 encoder principles, Disney Touché publication
description, R&S near-field measurement limits, Microchip historical AN236 and
NI's historical GPIB signal/serial-poll documentation. These were not acquired
as local originals in this bounded pass.

An attempted Synthetic Sensors copy at
`https://www.gierad.com/assets/supersensor/supersensor.pdf` returned 404; the
author-hosted original above succeeded. Some vendor/browser URL variants failed;
accessible canonical primary URLs are cited in the report. No acquisition is
currently blocked on operator intervention. Full licensed standards may be
needed for a later identified interface/conformance task; no such task was
selected here.

## Restoration

Run from repository root. These commands download literature only. Compare the
resulting hashes with the table; a changed upstream PDF must be recorded as a
new acquisition rather than silently treated as the same revision.

```sh
mkdir -p papers/unusual-interfaces quarantine/unusual-interfaces/text
curl --fail --location 'https://www.research.autodesk.com/app/uploads/2023/03/retrofab-a-design-tool.pdf_recq46gvQ9Haa6erl.pdf' --output papers/unusual-interfaces/retrofab-chi2016.pdf
curl --fail --location 'https://www.thinksrs.com/downloads/pdfs/applicationnotes/Lock-In%20Basics.pdf' --output papers/unusual-interfaces/srs-lock-in-basics-2020.pdf
curl --fail --location 'https://chrisharrison.net/projects/sweepsense/SweepSense.pdf' --output papers/unusual-interfaces/sweepsense-iui2016.pdf
curl --fail --location 'https://chrisharrison.net/projects/syntheticsensors/syntheticsensors.pdf' --output papers/unusual-interfaces/synthetic-sensors-chi2017.pdf
curl --fail --location 'https://www.ti.com/lit/ug/tiducf0/tiducf0.pdf' --output papers/unusual-interfaces/ti-tiducf0-optical-port-2016.pdf
curl --fail --location 'https://www.ti.com/lit/ug/tidueg0/tidueg0.pdf' --output papers/unusual-interfaces/ti-tidueg0-hart-input-2018.pdf
shasum -a 256 papers/unusual-interfaces/*.pdf
```

Reading text was derived using the existing `pdftotext -layout` utility, one
document at a time. For example:

```sh
pdftotext -layout papers/unusual-interfaces/retrofab-chi2016.pdf quarantine/unusual-interfaces/text/retrofab-chi2016.txt
```

Apply the same basename mapping to the other five PDFs. No software installation
is part of restoration. Text layout/tool versions can affect derived text;
original-PDF identity is established by the hashes above. Original figures were
not used as dimensional or electrical design drawings in this report.
