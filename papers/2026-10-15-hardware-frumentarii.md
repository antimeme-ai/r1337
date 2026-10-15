# Hardware frumentarii — 2026-10-15

## Scope and result

This lane studied official Flipper hardware documentation, ST's CPU and radio
boundaries, boot ROM recovery, and research qualifying those boundaries. It did
not communicate with the device, reset it, or write any flash or option bytes.
Acquisitions and unresolved download failures are recorded in
[the acquisition report](2026-10-15-hardware-acquisitions.md).

An owned CPU1 system is a concrete design direction. The documented radio update
path accepts ST images, while published research demonstrates CPU2 execution
outside that path. Those are different engineering options with different
unresolved work; neither establishes a working replacement on our unit. Full
CPU2 ownership remains a research question, not an impossibility inferred from
vendor documentation.

## Reading inventory

| Primary source | Read in this pass | Status |
| --- | --- | --- |
| [Flipper hardware specifications](https://docs.flipper.net/zero/development/hardware/tech-specs) | MCU, display, storage and peripheral specifications | Read live page; component function documented, physical board uninspected |
| [Flipper schematic index](https://docs.flipper.net/zero/development/hardware/schematic) | Main board, MCU, power, display, buttons, CC1101, iButton, NFC/RFID entries | Index read; linked PDFs return HTTP 403; schematics not read |
| [DS11929](https://www.st.com/resource/en/datasheet/stm32wb55rg.pdf), Rev 18 | Architecture; memory, MPU and protection descriptions, especially §§3.3–3.4 | Relevant sections read through web PDF; local download failed |
| [RM0434](https://www.st.com/resource/en/reference_manual/rm0434-multiprotocol-wireless-32bit-mcu-armbased-cortexm4-with-fpu-bluetooth-lowenergy-and-802154-radio-solution-stmicroelectronics.pdf) | Located only | Web PDF exceeds fetch size; local download failed; full register study remains open |
| [AN5185](https://www.st.com/resource/en/application_note/an5185-how-to-use-stmicroelectronics-firmware-upgrade-services-for-stm32wb-mcus-stmicroelectronics.pdf), Rev 15, April 2026 | §§1.1–1.4: FUS capabilities, versions, activation, memory | Read through web PDF; local download failed |
| [AN5289](https://www.st.com/resource/en/application_note/an5289-building-wireless-applications-with-stm32wb-series-microcontrollers-stmicroelectronics.pdf), served Rev 18, August 2024 | §§4.1–4.3, 4.7, 5.1–5.2 | Read relevant architecture, clock and flash coordination sections; local download failed |
| [AN2606](https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf), Rev 70, February 2026 | §81, printed pp.441–445 | Read WB30/35/50/55 bootloader section; local download failed |
| [ES0394](https://www.st.com/resource/en/errata_sheet/es0394-stm32wb55xxstm32wb35cx-device-errata-stmicroelectronics.pdf), Rev 18, April 2026 | Applicability, selected SRAM2, flash, clock and USB errata | Read selected sections, not exhaustive errata closure; local download failed |
| [SA0024](https://www.st.com/resource/en/security_advisory/sa0024-potential-isolation-issue-between-cpu1-and-cpu2-on-stm32wb5x-stm32wb3x-stm32wb1x-and-stm32wl5x-stmicroelectronics.pdf), Rev 1, December 2024 | Complete advisory, especially p.1 | Read through web PDF; no local PDF acquisition |
| [TI CC1101 SWRS061I](https://www.ti.com/lit/ds/symlink/cc1101.pdf) | Overview, interfaces, operating conditions and section map | PDF acquired; bounded reading, not a complete radio-driver study |
| [Thomas Cougnard, SSTIC 2025 paper](https://www.sstic.org/media/SSTIC2025/SSTIC-actes/recupration_de_la_cle_des_firmwares_radio_du_stm32/SSTIC2025-Article-recupration_de_la_cle_des_firmwares_radio_du_stm32wb55-cougnard_61Kne8u.pdf) | CPU2 execution and conclusions, §§5–7; preceding mechanisms inspected for context | Paper acquired; no experimental reproduction |
| [Cougnard slides](https://www.sstic.org/media/SSTIC2025/SSTIC-actes/recupration_de_la_cle_des_firmwares_radio_du_stm32/SSTIC2025-Slides-recupration_de_la_cle_des_firmwares_radio_du_stm32wb55-cougnard.pdf) and [FUS 2.0 follow-up](https://blog.xilokar.info/stm32wb55-fus-20.html) | Follow-up read; slides acquired as companion, not independently reviewed end to end | Research conclusions only; no operational procedure selected |

Document revision labels above come from the served documents, not assumptions
about the catalog's latest version. In particular the ST catalog lists AN5289
with a newer update date than the Rev 18 PDF served at the cited URL.

## Hardware capability and replacement surfaces

Flipper documents STM32WB55RG, a 64 MHz Cortex-M4 application core and 32 MHz
Cortex-M0+ radio core, sharing 1024 KB flash and 256 KB SRAM. It documents an
ST7567-controlled 128×64 monochrome SPI display, SPI microSD, USB full speed,
CC1101 Sub-GHz, ST25R3916 NFC, LF RFID, infrared, iButton and GPIO. These names
identify driver research surfaces; they do not establish component revisions or
the pin routing of the connected board. The current specifications include BLE
5.4, which must not be projected onto an older installed radio image.
[Source: official hardware specifications](https://docs.flipper.net/zero/development/hardware/tech-specs).

The CC1101 is a separate SPI-controlled transceiver with 64-byte transmit and
receive FIFOs, configurable packet processing and synchronous/asynchronous serial
modes. Owning that driver is a different problem from replacing the STM32's
integrated 2.4 GHz CPU2 stack. This is an architectural inference from its
documented interface and Flipper's component list. The TI document's chip-level
capabilities do not establish the assembled board's analog front-end behavior.
[Source: CC1101 datasheet, overview and §§10–11, 20, 27](https://www.ti.com/lit/ds/symlink/cc1101.pdf).

DS11929 describes an optional eight-region CPU1 MPU. Flash protection and CPU2
security are separate mechanisms: readout protection, write protection, PCROP,
and a CPU2-secured flash portion have different effects. RDP Level 2 disables
debug and alternative boot selections irreversibly. CPU1 task isolation is thus
a possible owned-runtime design feature, while the present option-byte state
remains unmeasured. A generic memory-capacity figure is not an application linker
budget. [Source: DS11929 §§3.3.2–3.3.4](https://www.st.com/resource/en/datasheet/stm32wb55rg.pdf).

## CPU2 and memory boundaries

AN5185's documented FUS path installs, upgrades and deletes CPU2 wireless images
only when encrypted and signed by ST; optional customer signing is additional.
FUS and the wireless stack run alternately on CPU2 and occupy protected flash
and SRAM. Option bytes define the allocations. Its WB5x map shows SRAM1 at
`0x20000000` (192 KiB), SRAM2a at `0x20030000` (32 KiB) and SRAM2b at
`0x20038000` (32 KiB), with protected boundaries inside SRAM2. The FUS version
is available via the SRAM2a shared device-information table. Current FUSv2 and
older FUS versions have different update constraints; the manual's defaults must
not be treated as this unit's actual allocation.
[Source: AN5185 §§1.1–1.4](https://www.st.com/resource/en/application_note/an5185-how-to-use-stmicroelectronics-firmware-upgrade-services-for-stm32wb-mcus-stmicroelectronics.pdf).

AN5289 documents CPU2 binaries and mailbox communication with CPU1. The readable
SFSA, SBRSA and SNBRSA option bytes define secured flash/SRAM2 boundaries, with
4 KiB flash and 1 KiB SRAM boundary granularity. Available application memory
changes with CPU2 image version. Shared clocks and peripherals require the
documented hardware-semaphore protocol: USB and RNG share CLK48, flash operations
need coordination, and CPU2 timing can stall CPU1. CPU2 expects a 32 MHz clock;
startup emits a system-ready mailbox event before system commands. An owned
clock/power/flash layer therefore needs an explicit retained-CPU2 contract if we
keep ST radio firmware. [Source: AN5289 §§4.1–4.3, 4.7, 5](https://www.st.com/resource/en/application_note/an5289-building-wireless-applications-with-stm32wb-series-microcontrollers-stmicroelectronics.pdf).

## Research qualifies the supported path

Cougnard's 2025 paper reports decrypted firmware/FUS recovery and arbitrary CPU2
execution; its conclusion is experimental research, not merely speculation about
the register interface. The follow-up identifies FUS 1.2.0, describes fixes in
FUS 2.0 and reports a further failure in that release. The author is **Thomas
Cougnard (Xilokar)**. This creates a substantive lead for full ownership, but it
does not provide an owned radio implementation, a stable recovery procedure, or
compatibility evidence for our hardware. We did not reproduce its methods or
extract any keys. [Paper §§5–7](https://www.sstic.org/media/SSTIC2025/SSTIC-actes/recupration_de_la_cle_des_firmwares_radio_du_stm32/SSTIC2025-Article-recupration_de_la_cle_des_firmwares_radio_du_stm32wb55-cougnard_61Kne8u.pdf),
[author's FUS 2.0 follow-up](https://blog.xilokar.info/stm32wb55-fus-20.html).

ST independently acknowledges that CPU1 software can interfere with and take
control of CPU2 execution even when ESE is enabled. SA0024 lists any silicon
version of STM32WB5x among affected products and advises against relying on CPU2
for assets requiring isolation from CPU1. Therefore neither an enclave-valid
status nor the documented secure memory map establishes an adversarial security
boundary against arbitrary CPU1 code. [Source: SA0024 p.1](https://www.st.com/resource/en/security_advisory/sa0024-potential-isolation-issue-between-cpu1-and-cpu2-on-stm32wb5x-stm32wb3x-stm32wb1x-and-stm32wl5x-stmicroelectronics.pdf).

## Recovery and errata constraints

AN2606 §81 documents WB55 boot ROM in 28 KiB at `0x1FFF0000`, using 20 KiB RAM
at `0x20000000`; USB DFU uses PA11/PA12, HSI48 and CRS. Boot selection uses
Pattern 16, involving boot configuration; boot ROM presence alone does not
establish a reachable recovery route. §81.3 also documents bootloader command
limitations. [Source: AN2606 §81](https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf).

Flipper distinguishes firmware DFU selected by LEFT during boot from ST ROM DFU
selected by OK. Hardware reset goes through button logic to the MCU reset line;
power reset involves the charger. Documented failure conditions include an
active debug block holding reset, damaged or absent Flipper bootloader, and
option bytes that ignore OK. These are documentation facts, not observed recovery
tests. [Source: Flipper key combinations](https://developer.flipper.net/flipperzero/doxygen/key_combos.html).

ES0394 makes silicon revision identification necessary. Relevant examples include
SRAM2 parity initialization before CPU2 startup (§2.2.22), flash/ECC effects under
reset (§2.2.13), and a minimum 10 MHz APB clock for USB (§2.17.1). Other clock,
power and debug limitations need screening against the actual REV_ID and planned
execution modes before an owned startup sequence. This was a triage reading,
not a claim that all errata have been handled. [Source: ES0394](https://www.st.com/resource/en/errata_sheet/es0394-stm32wb55xxstm32wb35cx-device-errata-stmicroelectronics.pdf).

## Connected-unit information supplied by the inventory lane

The root inventory lane reports that the running firmware identifies hardware
version 12, target 7, body 9, connection 6 and display 1, with OTP version 2.
It reports CPU2 alive in Stack mode, FUS 1.2.0 and stack type 3 version 1.13.3;
reported stack allocations are 120 KiB flash, 19 KiB SRAM2b and 14 KiB SRAM2a,
with FUS reporting 24 KiB flash and 16 KiB SRAM2b. These values are firmware
self-reports communicated by that lane. This lane has not inspected raw captures
or independently measured them. They are not sufficient to infer SFSA or a final
linker map by subtracting sizes from nominal capacity.

Inventory also reports a valid enclave and ten provisioned keys, without reading
key material. Treat preservation of that state as a design input. Neither the
read-only report nor this literature pass establishes recoverability after FUS,
security-option or provisioned-state changes.

## Next work this pass enables

1. Obtain readable revision-matched schematics and RM0434 locally. Trace reset,
   BOOT0/OK, SWD, power rails, buses and pin multiplexing against upstream target
   definitions; retain explicit unresolved routing until drawings are read.
2. Correlate the installed CPU2 image and reported allocation with its exact
   release notes, actual option bytes and pinned Flipper linker definitions.
3. Make a recovery design covering CPU1 firmware, bootloader, option bytes,
   storage and provisioned CPU2 state separately before an experiment changes any
   of them. Then exercise the selected route on this unit.
4. Keep two architectural candidates visible: owned CPU1 with a retained CPU2
   contract; and deeper CPU2/radio ownership as a separate research program.
   Published execution control does not supply the undocumented radio machinery.

No dependency was adopted. This report selects neither a runtime nor an update
mechanism and does not authorize a particular flash operation.
