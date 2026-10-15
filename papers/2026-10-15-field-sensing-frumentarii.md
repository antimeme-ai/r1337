# Field sensing and coherent physical instruments — 2026-10-15

Peter Jansen's **2026 Open Source Science Tricorder Cyberdeck** is the closest reference found in this lane: a finished-looking handheld console, internally integrated sensors, local graphs/images, and an explicit account of the mechanical and software compromises. Its strongest lesson is that broad capability becomes useful through the enclosure, controls and data paths acting together. The other projects below expose complementary questions: what temperature actually means, what makes a camera useful at equipment-inspection distances, how local acquisition survives beyond a preview window, and how controls remain usable.

This research follows the current brief: RF/electromagnetic, debugging and firmware access first; control-system work second; camera/basic sensing as useful supporting capability. A polished folding/tablet/cyberdeck core and at most one pocket companion remain the physical direction. These references do not select parts, dependencies, an enclosure, or a build. No device operation, installation or acquired-code execution occurred.

## Six projects, each with a concrete lesson

### 1. Arducorder Mini → Science Tricorder Cyberdeck: integrate breadth deliberately

Primary sources: Jansen's [2014 Arducorder project](https://hackaday.io/project/1395-open-source-science-tricorder), [2014 source](https://github.com/tricorderproject/arducordermini/tree/e6ff23335c06cd4f6410152471ade1856c504c26), and [2026 cyberdeck source](https://github.com/tricorderproject/cyberdeck/tree/b2b8410a905fe13b079b8bc42ec15af540e23f07). Both source snapshots were acquired; see [the acquisition record](2026-10-15-field-sensing-acquisitions.md).

The lineage moves from a custom handheld with internal sensor boards and a tile interface to a uConsole sensor backpack. The newer design combines visible/thermal imaging, spectroscopy, magnetic observations and environmental sensing. Its author calls it a prototype and documents failed phone/tablet/small-console iterations. CAD replaces the console's back, mounts sensors, routes a particulate-sensor exhaust and exposes sensing apertures. Its integrated appearance is relevant; its exact shape need not be ours. [Author's design account](https://github.com/tricorderproject/cyberdeck/blob/b2b8410a905fe13b079b8bc42ec15af540e23f07/README.md).

Read the limits alongside the pictures: unresolved cooling, short reported runtime, antenna placement, and ambiguous low-profile connectors. The advertised magnetic tile's fast theoretical operation is not the assembled instrument's demonstrated capture rate. README errata reports roughly one frame/second. Source adds nuance: focus modes exist, but the ESP32 loop still ends in `delay(1000)`; the host's page-dependent polling does not remove that delay. [Firmware loop](https://github.com/tricorderproject/cyberdeck/blob/b2b8410a905fe13b079b8bc42ec15af540e23f07/esp32/uconsole_sensor_backpack_1b/uconsole_sensor_backpack_1b.ino), [host UI](https://github.com/tricorderproject/cyberdeck/blob/b2b8410a905fe13b079b8bc42ec15af540e23f07/src/UserInterfacePygame.py).

The old [TileGUI](https://github.com/tricorderproject/arducordermini/blob/e6ff23335c06cd4f6410152471ade1856c504c26/firmware/test2k/TileGUI.h) gives heterogeneous quantities a common navigation scheme. The new host separates drivers, screen selection, histories, baselines and errors; its sensor bridge retains boot-relative timestamps. Yet thermal and visible drivers are polled independently, not established as synchronized exposures. The thermal driver enables filtering/smoothing, so displayed imagery also depends on processing choices. [Sensor bridge](https://github.com/tricorderproject/cyberdeck/blob/b2b8410a905fe13b079b8bc42ec15af540e23f07/src/DriverESP32Sensors.py), [thermal driver](https://github.com/tricorderproject/cyberdeck/blob/b2b8410a905fe13b079b8bc42ec15af540e23f07/src/DriverThermalCamera.py).

**Transfer:** coherent navigation and internal integration can accommodate breadth. Distinguish the sensor's capability, acquisition mode, transport rate and displayed refresh; retain measurement timing and processing state. Study this implementation without importing its JSONL internal machinery or software dependencies into r1337.

### 2. tCam/tCam-Mini: keep temperature-bearing data, not just false-color pictures

Dan Julio's [original project source](https://github.com/danjulio/tCam) describes standalone tCam with screen/storage and smaller networked tCam-Mini. The [author's hardware/firmware documentation](https://danjuliodesigns.com/products/tcam_mini.html) identifies radiometric Lepton variants and separates Wi-Fi streaming from the USB power/update/diagnostic path. A camera's USB connector therefore does not automatically establish the image transport we would want.

This is useful for observing equipment warming, locating a suspect area, retaining a temperature field, and sending selected frames for remote interpretation. It is not evidence that our ESP32 boards alone can provide thermal imaging, that every Lepton variant is radiometric, or that the author's desktop application meets our local-host performance needs. Its [quick-start guide](https://danjuliodesigns.com/resources/Products/tcam_mini/tcam_mini_quick_instructions.pdf) and source are reference inputs; no unit was tested and present manufacturing/availability was not established.

**Transfer:** retain radiometric frame values and relevant settings alongside a viewable rendering. Local preview/capture should not require a remote support station; analysis can happen later. A palette screenshot alone is a poor substitute for the original measurements.

### 3. Sensor Watch: small, legible interactions and physically honest sensing

The [temperature face](https://www.sensorwatch.net/docs/using/temperature/) samples periodically and selects among fitted sensors. Its documentation explicitly notes wrist heat corrupts an ambient reading, and lower-resolution accelerometer temperature is a fallback rather than the same sensor. No temperature sensor means the face skips itself.

The [Watch Interface Guidelines](https://www.sensorwatch.net/docs/wig/) organize interaction around questions a small display and a few buttons can answer quickly, with power behavior part of the UI contract. They also explain that default Sensor Watch is not a continuously synchronized companion. This is not a proposal to carry a watch as a second instrument.

**Transfer:** readings need location/context and sensor identity, not just a unit suffix. A sensor beside our CPU, charger or hand may be reporting that local environment. Preserve a coherent global meaning for capture/back/mode controls even as instruments change; expose unavailable sensing instead of displaying an unexplained old number.

### 4. OpenMV: acquisition, optics and camera controls are a single capability

OpenMV's [programmable-camera tutorial](https://docs.openmv.io/v5.0.1/openmvcam/tutorial/index.html), [lens/focus guide](https://docs.openmv.io/v5.0.1/openmvcam/tutorial/vision/optics/lenses-and-focus.html), and [CSI reference](https://docs.openmv.io/v5.0.1/library/omv.csi.html) make the hardware/software boundary explicit. Focus distance, field of view and exposure/gain matter as much as nominal pixel count. Autofocus and triggered modes are sensor-specific: the documented autofocus commands apply to an OV5640 FPC module, while triggered mode is identified for MT9V034. These are not universal board capabilities.

For r1337, a useful visible-camera experience is inspecting connector labels, board markings, component placement and an equipment front panel, then retaining a sharp local still for library/manual lookup. A room-focused camera may fail at close markings; inadequate or reflective illumination can defeat a nominally high-resolution sensor. A proposed optical layout therefore needs focus access, usable working distance, controlled light and a stable way to aim the instrument. No lens or sensor is selected here.

**Transfer:** distinguish preview from a retained capture; keep exposure/focus/illumination choices attached where relevant. Hardware acquisition and local storage should proceed independently of remote interpretation. Software snapshot/preview timing alone establishes no precision correlation with an RF or digital trace.

### 5. Beepy: an embedded controller can make a Linux handheld feel like one object

SQFMI's [hardware pinouts](https://beepy.sqfmi.com/docs/hardware/pinouts) separate Pi display lines from an RP2040-backed keyboard, battery measurement and power signals. Its [operating guide](https://beepy.sqfmi.com/docs/getting-started) describes a physical-key shutdown interaction, status indication, and a later power-on gesture; the same object combines keyboard, display, power and OS behavior.

This is useful field-integration evidence even though its small monochrome interface is not a template for our camera/graph-rich core. Its firmware/driver compatibility requirements and shutdown procedure also show the integration work hidden by a neat exterior. The documentation is a historical implementation reference; current supply/support was not established.

**Transfer:** local capture controls and power/status feedback can remain available through a dedicated embedded controller while the host does networking/research. A finished keyboard/display shell still needs a deliberate suspend/shutdown/recovery story, particularly when captures or firmware jobs are active. It does not follow that another carried pocket keyboard is needed.

### 6. OpenFlexure: mechanical stability and illumination produce useful close inspection

The [open microscope project](https://openflexure.org/projects/microscope/) treats stage motion, camera/lens geometry and illumination as an instrument. Its [reflection-illumination Delta Stage](https://build.openflexure.org/openflexure-delta-stage/v1.2.3/pages/index_reflection.html) is a distinct configuration from transmission imaging; its [local/network control guide](https://openflexure.org/projects/microscope/control) shows how acquisition hardware can serve either an attached interface or another computer.

This is a mechanical/UI reference, not a recommendation to fit a laboratory microscope into the core. Equipment inspection might benefit from a folding support, fixed working-distance spacer or small target fixture rather than more pixels. A camera that cannot be held steady at its required distance is not a useful inspection feature. Transmitted-light sample imaging does not automatically transfer to opaque circuit-board inspection.

**Transfer:** make support, illumination and optical access part of CAD. The core/one-companion rule could accommodate one deliberately designed inspection head, but this report does not assign that companion role or add more external modules.

## “Temperature” denotes three different observations

| Observation | What it concerns | What integration must preserve |
| --- | --- | --- |
| Environmental temperature | Air near the sensor after its thermal response; placement and local heat sources matter | Ventilation/placement context, sampling time and sensor identity; case temperature is not automatically ambient |
| Target/contact temperature | A probe thermally coupled to an equipment surface or another identified point | Probe/contact method, settling, location and electrical-interface constraints; it is not a thermal image |
| Radiometric thermal image | A field of infrared-derived apparent temperatures under an instrument model | Original values, optics/processing state, and relevant emissivity/reflection/measurement settings; it is not a contact measurement |

FLIR's [thermographic measurement guide](https://support.flir.com/docdownload/assets/web/2p5q/en-us/T505000.xml.html) explains emissivity, reflected apparent temperature and distance compensation. Accordingly, an equipment thermal image is useful context without implying that every shiny component's displayed number is its true surface temperature. The table is a proposed distinction for our design vocabulary; this pass selects no ambient or contact probe, calibration procedure, or numerical accuracy claim.

## Useful combinations within the actual brief

The strongest camera/basic-sensing addition is an **equipment observation attached to an electrical/RF session**: save an overview, a readable marking/connector close-up, selected sensor observations, relevant instrument settings and the capture time relationship. On the core, the user can inspect the local original and annotate the subject. Through the proposed tailnet support path, a selected still/crop and bounded trace can support manual lookup, candidate part identification or analysis. Network loss should leave the originals and local instrument usable; reconnect should resume analysis/upload rather than replay a device-changing operation. This is our proposed integration lesson, not a feature demonstrated by every reference.

The operator also has old iPhones. Conditional roles include the inspection camera, touch/display surface, available onboard sensing, and a tailnet-connected terminal; exact model, iOS version, connector, app/API support and power behavior remain unknown. An iPhone could be integrated into the core or occupy the single permitted companion role. Jansen abandoned one bulky phone-backed iteration; that documents his integration outcome rather than a universal obstacle. A phone role would still need local capture/export behavior, usable focus/lighting and a coherent dock or enclosure. Apple/Tailscale compatibility research is outside this lane.

A later UI could distinguish live preview, fresh measurement, baseline-relative view, frozen capture and remote interpretation explicitly. Measurement age and independent clocks matter when images, slow environmental readings and fast traces share one screen. Remote confidence should not disguise blurred labels, unknown probe placement or missing calibration context.

For physical research, reserve sight lines, working distances, lighting paths, antenna regions, air inlet/exhaust separation and access to power/recovery controls before filling the enclosure volume. Jansen's sensor backpack and OpenFlexure's optics show how CAD can define what the instrument can actually observe. Production finish, thermal behavior and RF coexistence still require our own design and measurements; photographs of an attractive prototype do not establish them.

## What this pass establishes

Six original projects/documentation sets were read, with the Arducorder/cyberdeck lineage receiving direct source/CAD/photo inspection. The two acquired snapshots are research material, not an adopted implementation. No original source needed operator acquisition; no product, purchase or new device experiment is selected. Further reading should follow the promising boundaries above rather than expanding the carried-module count or displacing the primary RF/debugging/firmware scope.
