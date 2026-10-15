# Closed-enclosure sensing: thermal, acoustic, ultrasonic and RF

Research date: 2026-10-15. The operator asks whether ultrasound, acoustics or
Wi-Fi radar could reveal something behind a difficult enclosure panel, and
reports a thermal dongle somewhere in the stash. No particular panel material,
geometry, internal coupling or operating state has been identified. The dongle
is unlocated/unidentified. No measurement or experiment was performed.

The central distinction is between measuring the panel, detecting internal
activity and resolving internal geometry. Different observations can contribute
to an equipment assessment without generating an image of the interior.

## Acoustic and structural response

Passive contact vibration/acoustic observations are a promising candidate for
detecting operating machinery or changes between equipment states. A contact
sensor and an airborne microphone observe different transfer paths. A surface
signal is affected by panel structure, mounting, sensor coupling and background
activity; identifying an internal component from it is an inference requiring
validation, not a direct image.

Brüel & Kjær's [Structural Testing Part 1](https://www.bksv.com/doc/br0458.pdf)
explains frequency-response measurement using measured excitation force and
structural response, accelerometers, impact excitation and noise/coherence.
This supports investigating controlled mechanical-response comparisons. An
unmeasured tap and a recording may be useful exploratory observations, but do
not by themselves establish a calibrated transfer function or a unique internal
layout. Our microphone/contact-vibration/actuator hardware remains unselected.

## Active ultrasonic inspection

Evident's [thickness-gauging introduction](https://evidentscientific.com/en/applications/introductory-ultrasonics/introduction-thickness-gauging)
describes pulse/echo measurement through solids from one side. This is a strong
lead for panel thickness, material boundaries and selected bonded/layered
structures. It is a separate instrumentation path involving an appropriate
transducer, excitation, receive frontend, timing and material calibration.

The [couplant note](https://ims.evidentscientific.com/en/applications/ultrasonic-couplant)
explains why a thin air gap prevents efficient conventional contact-ultrasonic
transmission. The [gauging factors](https://ims.evidentscientific.com/en/learn/ndt-tutorials/thickness-gauge/factors)
describe air-backed solids, phase changes, geometry, attenuation and velocity
calibration. The acquired Olympus technical notes expand impedance/reflection
and beam limitations. Consequently a pulse can readily characterize a panel's
far surface while transmission onward through an internal air gap is a major
obstacle. An ordinary air-filled electronics enclosure is not equivalent to a
continuously coupled specimen.

Specialized dry-contact/air-coupled and other ultrasonic methods exist; this
pass does not declare them impossible. It establishes no general portable
method for imaging arbitrary circuit boards behind an arbitrary panel. Narrow
questions about the panel or bonded construction are more promising starting
points than an unrestricted interior-imaging claim.

## Wi-Fi sensing and radar

Espressif's [ESP-CSI](https://github.com/espressif/esp-csi) and
[solution documentation](https://docs.espressif.com/projects/esp-techpedia/en/latest/esp-friends/solution-introduction/esp-csi/esp-csi-solution.html)
describe channel-amplitude/phase observations, motion/presence detection and
special synchronized multi-chip arrangements. This is a realistic research
lane for available ESP hardware, with actual chip/firmware/antenna arrangements
to be identified. It does not make every ESP32 snapshot SDR a coherent imaging
radar. Fine motion sensitivity and resolving closely spaced static objects
are different properties.

MIT's [Wi-Vi design](https://people.csail.mit.edu/fadel/wivi/design.html)
specifies non-metallic walls and describes the strong wall reflection and
two-way attenuation. Its method nulls static reflectors and tracks movement;
that is particularly different from mapping stationary components in a metal
electronics box. A conductive panel is a major barrier at Wi-Fi frequencies;
signals leaking around gaps are not an established image through that panel.

For conventional bandwidth-limited ranging, TI's
[range-estimation tutorial](https://www.ti.com/video/5415203482001)
gives nominal range resolution c/(2B). At an illustrative 320 MHz signal
bandwidth this is about 0.47 m. This is a basic range-separation illustration,
not a complete imaging or localization bound; phase-based displacement
sensitivity and specialized aperture/model methods answer different questions.
ADC sample rate alone does not establish usable signal bandwidth or resolution.
Nothing here establishes component-scale enclosure tomography from the stash.

## Thermal dongle and other optical access

FLIR's [material-transmission explanation](https://www.flir.com/en-in/discover/home-outdoor/can-thermal-imaging-see-through-walls/)
states that thermal cameras do not see through metal. Internal heating can
produce a surface-temperature pattern; that is an indirect observation shaped
by thermal coupling and time. Some thin plastics transmit thermal infrared,
but a visibly opaque plastic housing is not automatically an infrared window.
Reflective surfaces also complicate apparent-temperature interpretation.

For r1337, thermal imagery could be valuable for locating warm surface regions
and comparing known operating states, with retained timing and material/context
information. A thermal pattern does not uniquely identify internal geometry.
An existing vent or opening could also permit a small optical probe/borescope
to obtain a direct view; no such probe is assumed owned or selected.

Locate the reported dongle and identify model, connector, supported hosts/apps,
power, optics and whether original radiometric frames can be exported. The
identified iPhones use Lightning, which does not establish compatibility with
an arbitrary thermal accessory. No sensor resolution, temperature accuracy,
frame interface or platform support is assigned without identification.

## Current engineering judgment

Closed-case assessment is a useful r1337 capability family. Thermal and
passive/contact-acoustic observations appear especially promising near-term
research inputs. Optical access through an existing opening is worth comparing
where possible. Active ultrasound deserves targeted study for material/panel
questions. Wi-Fi sensing is an interesting separate motion/channel experiment,
with less current support for the requested enclosure-interior imaging task.

The scope, waveform generator, sensor frontend and capture notebook could serve
several of these paths with appropriate transducers and conditioning. None is
a software-only upgrade to a generic ADC. No architecture or acquisition is
selected; first define the actual observable and compare a known accessible
subject with its closed configuration before trusting an inference.

## Acquired literature and restoration

Two original PDFs are retained unchanged under ignored `papers/enclosure-sensing/`.
Working text extractions are in ignored `context/enclosure-sensing/`. Only the
specified sections were read; no figures were used as measurement evidence.

| Document | Local file | SHA-256 | Read scope |
| --- | --- | --- | --- |
| Olympus Ultrasonic Transducers Technical Notes, 2019 | `olympus-ut-technical-notes-2019.pdf` | `72356806da7435fcfaeedd90e4b1eff19b1283b3b6aad663e09855412be6b3f5` | Impedance, reflection/attenuation and sound-field text |
| Brüel & Kjær Structural Testing Part 1, BR0458 | `bk-structural-testing-br0458.pdf` | `8af229fd1daa3c59af929eff1b4be626df07fa4c2e990684f504856bdecd6478` | FRF definitions/estimation, response sensors and impact-excitation text |

```sh
mkdir -p papers/enclosure-sensing
curl -fsSL https://adobeassets.evidentscientific.com/content/dam/downloads/276824176/UT_Technical_Notes_201907.pdf -o papers/enclosure-sensing/olympus-ut-technical-notes-2019.pdf
curl -fsSL https://www.bksv.com/doc/br0458.pdf -o papers/enclosure-sensing/bk-structural-testing-br0458.pdf
```

Other primary sources above were read live without source-archive acquisition.
No essential blocked acquisition, installation or dependency adoption arose.
