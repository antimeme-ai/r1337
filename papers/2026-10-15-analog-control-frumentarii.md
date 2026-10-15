# Small analog instruments and control-interface lessons

Research date: 2026-10-15. Primary documentation and one pinned firmware
snapshot were read. No device was operated, reference code executed, dependency
adopted or hardware selected. Read the [acquisition record](2026-10-15-analog-control-acquisitions.md)
for exact source restoration.

## Pocket Science Lab: analog capability beside protocol access

[PSLab's hardware repository](https://github.com/fossasia/pslab-hardware)
publishes schematics, a component list, board design and mechanical drawings.
It describes a PIC24EP256GP204-based instrument combining analog acquisition,
programmable gain, voltage/current sources, waveform generation and sensor
buses. Its external DAC, amplifiers and power circuitry are important: breadth
comes from signal-conditioning electronics as well as MCU firmware. Its v6
description adds USB-C, external power, RTC, SD and optional ESP-01 connectivity.
Some limits in the README differ between sections, including PWM frequency;
they are research leads rather than a unified measured specification.

The [oscilloscope UI documentation](https://docs.pslab.io/tutorials/oscilloscope/)
offers channel selection, triggering/timebase, XY display, Fourier analysis and
capture recording. The [multimeter documentation](https://docs.pslab.io/tutorials/multimeter/)
describes different ranges for different inputs, resistance/capacitance
measurements and logged readings. An application called a multimeter is not by
itself evidence for isolated industrial inputs, a handheld meter's input
protection or equal range on every channel. Exact analog bandwidth, calibration
and multi-channel performance would require further revision-specific study.

The locally acquired [firmware revision](https://github.com/fossasia/pslab-firmware/tree/33b0b136b826fe30f59b177bb6f6ddf105cbcce4)
supports hardware v5/v6 and uses a binary command table. Inspected paths:

- `src/commands.c`: grouped ADC, bus, waveform, timing and buffer operations;
  some command numbers explicitly dispatch to removed/unimplemented handlers.
- `src/instruments/oscilloscope.c`: ordinary multi-channel capture configures
  10-bit simultaneous mode; DMA capture selects 10- or 12-bit mode. Capture
  receives requested sample count and time gap locally, and exposes status.
- `src/helpers/buffer.h`: capture data can be fetched by starting index/count.
- `src/instruments/sensors.c`: input-capture peripherals and timers measure
  intervals/counts locally.
- `src/bus/uart/uart.c`: the host-facing UART's configured default is 1 Mbaud.

These mechanisms support a useful architectural lesson: local timed acquisition
and later buffer retrieval are distinct operations. They do not establish
continuous export at the ADC's headline sample rate. Likewise a published
12-bit ADC capability does not mean every capture mode is 12-bit. None of these
paths was built or tested here.

For r1337, a small analog measurement/stimulus block could add capability
beside BP5 and the expected logic analyzer. This is a gap to characterize,
not a PSLab purchase recommendation. Existing unclassified modules may already
provide part of the required conditioning, conversion or excitation.

## HydraBus: protocol breadth needs physical interfaces

[HydraFW's command guide](https://github.com/hydrabus/hydrafw/wiki/HydraFW-console-commands)
documents familiar serial buses alongside JTAG, NAND, smartcard, Wiegand, LIN,
CAN, ADC/DAC and PWM. It also documents local SD logging/scripts, a physical
button to abort blocking operations and a binary automation interface. These
are useful interface/interaction patterns for a field instrument; the command
names alone do not specify every required target adapter.

The [CAN guide](https://github.com/hydrabus/hydrafw/wiki/HydraFW-CAN-guide)
explicitly requires an external CAN transceiver for the actual bus. It describes
initial silent reception, a transition to normal mode on transmit, frame filters
and an SLCAN interface. The [HydraLINCAN shield](https://github.com/smillier/HydraLINCAN)
provides published hardware for CAN/LIN adaptation. This cleanly distinguishes
an MCU protocol peripheral from its electrical line interface. Electrical
adaptation, termination, grounding/isolation and device commands still need
individual attention in the multi-decade control-system collection.

For r1337, study the mode visibility, local cancellation, transcript
recording and automation boundaries. Much of the generic bus role overlaps BP5;
the control-side lesson is to inventory actual device interfaces before adding
another general-purpose protocol board. No HydraBus source archive was acquired
and no complete hardware/firmware audit was performed in this lane.

## Basic sensors need measurement-aware packaging

Sensirion's [design guide](https://sensirion.com/media/documents/FC5BED84/662A065D/Sensirion_Temperature_Sensors_Design_Guide_V1.pdf),
Version 2, March 2024, was acquired and read for sensor/system accuracy,
thermal coupling and enclosure guidance. It explains that housing, PCB heat
sources, air exchange and thermal mass affect the measured environment and
response time. A sensor compartment and thermal decoupling are useful design
patterns. A component's accuracy specification does not establish accuracy of
the assembled instrument.

Consequently, the tertiary temperature objective deserves a defined measurand:
ambient air, a contacted object, internal electronics or an observed surface.
The portable core's processor, charger, radios and the user's hand are candidate
sources of measurement interference to consider. Optical-camera access and
lighting, ambient-sensor exposure and analog probe access should enter the CAD
study together. A compact part's footprint alone is not its integration cost.

This lane supports comparing analog capture/stimulus and physical-interface
coverage with existing digital/radio tools. It does not choose an analog front
end, sensor suite, protocol stack or enclosure architecture.
