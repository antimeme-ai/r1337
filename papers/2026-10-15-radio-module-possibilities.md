# Radio module possibilities — 2026-10-15

The collection could support both a portable instrument and a small distributed sensing system. The most useful additions are independent roles: the Flipper supplies a handheld interface and several physical interfaces; the TI board supplies an autonomous sub-GHz endpoint; the classic ESP32-WROVER supplies Wi-Fi, Bluetooth, memory, and general peripheral processing; the official Wi-Fi board supplies an especially relevant debug path for developing custom Flipper firmware. These are possible combinations, not a selected architecture or instructions to connect or flash anything.

This report uses manufacturer documentation. No boards were connected, interrogated, reprogrammed, or powered by this research lane; no SDK, library, or reference implementation was adopted. The operator's labels establish candidate models, not verified silicon, board revision, wiring, fitted accessories, or installed firmware.

## Identity matters

| Operator description | Working interpretation | Still unknown |
| --- | --- | --- |
| TI LAUNCHXL-CC1312R1 | CC1312R LaunchPad for 868/915 MHz; specifically R1 | PCB revision, fitted RF routing/antenna, current image and jumpers |
| Freenove ESP32-WROVER with extension | Classic ESP32-WROVER development board plus breakout/extension | Exact Freenove SKU/revision, WROVER suffix, flash/PSRAM, extension model, camera/card presence |
| Flipper Wi-Fi module v1 | Candidate official Wi-Fi Developer Board whose published assembly is Module_V1 | Confirm silkscreen and module marking; determine its present firmware separately |
| Flipper Zero | Existing handheld exploration subject | See device baseline for observations; chip specifications alone do not describe its installed software |
| Raspberry Pis and Xilo flight controller | Additional possible processing/sensing platforms | Models unreported; no specific interfaces, CPU, sensor complement, or power requirements assigned |

The [TI kit page](https://www.ti.com/tool/LAUNCHXL-CC1312R1) explicitly identifies the LaunchPad and its 868/915 MHz antenna. It must not inherit CC1312R7 capacity, CC1352 dual-band features, or a higher-power variant's specifications. Freenove separately lists [FNK0060 as its ESP32-WROVER board](https://freenove.com/tutorial); newer product naming and breakout compatibility do not identify the operator's exact unit.

## What the TI board adds

The [CC1312R datasheet, SWRS210H](https://www.ti.com/lit/ds/symlink/cc1312r.pdf), describes a 48 MHz Cortex-M4F with 352 KiB flash, 80 KiB SRAM, and an autonomous sensor controller. It exposes UART, SPI/SSI, I2C, I2S, ADC, GPIO, and JTAG/cJTAG. Its RF core handles packet work through vendor commands; §9.3 explicitly says its radio Cortex-M0 is not customer-programmable. Thus an owned application still has a vendor radio boundary.

The silicon supports multiple sub-GHz bands and GFSK/FSK families, with mode-dependent rates and coding; OOK is also documented. This does not make the fitted LaunchPad antenna/matching appropriate for every silicon frequency. Its specified chip-level examples include 5.8 mA RX, 24.9 mA TX at +14 dBm, and 0.85 µA standby under stated conditions. Those are not whole-board battery estimates. [Datasheet §§1, 8–9](https://www.ti.com/lit/ds/symlink/cc1312r.pdf).

For the actual board, TI's [SWRA588B hardware report, §§4.1–4.7](https://www.ti.com/lit/an/swra588b/swra588b.pdf) describes USB power, a 3.3 V LDO, an XDS110 debugger, USB-to-UART up to 1 Mbps, BoosterPack headers, and jumpers that separate debugger and target sections. External target power requires the documented jumper arrangement. The debugger is useful on the bench and adds size/power overhead in a portable deployment; that overhead must be measured separately from radio-chip figures. The [kit page](https://www.ti.com/tool/LAUNCHXL-CC1312R1) also identifies EnergyTrace support.

TI's [RF examples guide](https://software-dl.ti.com/simplelink/esd/simplelink_cc13x2_26x2_sdk/3.10.00.53/exports/docs/proprietary-rf/proprietary-rf-users-guide/proprietary-rf-guide/examples-cc13x2_26x2.html) documents low-level RF commands and raw packets, plus an optional EasyLink layer. This is evidence of ways to study the chip, not a decision to adopt those components. Its [operation-mode guide](https://dev.ti.com/tirex/explore/content/simplelink_cc13xx_cc26xx_sdk_8_32_00_07/docs/proprietary-rf/proprietary-rf-users-guide/proprietary-rf/operation_modes.html) warns that device support differs; family-wide BLE/high-speed listings do not confer those modes on CC1312R1.

Relative to Flipper's existing radio, the largest addition is **another independently programmable computer and receiver/transmitter**, capable of remaining at a remote location while the handheld moves. A compatible PHY could permit a controlled link between them. Matching center frequency alone is insufficient: modulation, deviation, bandwidth, symbol rate, preamble/sync, whitening, coding, packet structure, and timing have to agree.

## Packet and timing access are different from raw I/Q

Flipper's [Sub-GHz documentation](https://docs.flipper.net/zero/sub-ghz) identifies its CC1101 and the 300–348, 387–464, and 779–928 MHz bands. The [CC1101 datasheet](https://www.ti.com/lit/ds/symlink/cc1101.pdf) documents a configurable modem, packet FIFOs, RSSI, and serial modes for demodulated data. Such access supports packet and pulse/timing work. It does not by itself expose a general complex-sample RF capture stream.

Similarly, TI's phrase “raw packets” for CC1312R means packet data below a higher-level protocol. It must not be translated into unfiltered, arbitrary-rate I/Q samples. An [older TI support answer specifically about CC1312R](https://e2e.ti.com/support/wireless-connectivity/sub-1-ghz-group/sub-1-ghz/f/sub-1-ghz-forum/677814/cc1312r-looking-for-low-power-sub-1ghz-transceiver-that-can-output-input-i-q-samples) stated that an IQ patch was not then released for 13x2, while distinguishing older 13x0 support; it also described direct-modulation TX as unsuitable for I/Q input. This historical answer is not proof of all present firmware options. This pass found no demonstrated general I/Q capture pipeline for the operator's R1 board, so none is assumed. The separate ESP32 SDR investigation addresses that different possibility.

## The official Flipper Wi-Fi board has a development role

Flipper's [developer-board documentation](https://developer.flipper.net/flipperzero/doxygen/dev_board.html) identifies ESP32-S2-WROVER, USB-C, and Wi-Fi/USB debugging firmware using Black Magic Debug and CMSIS-DAP. It supports breakpoints, stepping, memory/variable inspection, and flashing supported targets. These are documented capabilities of the platform; the operator's installed board firmware has not been checked.

The [official schematic index](https://docs.flipper.net/zero/development/hardware/devboard-schematics?stub=1) labels an assembly `Wi-Fi Module_V1_Assembly.pdf` and its module sheet `ESP32-S2-WROVER-N4R2`. That supports the candidate identification but does not establish that every board called “v1” is identical. Espressif's [chip comparison](https://docs.espressif.com/projects/esp-idf/en/v4.3.4/esp32s2/hw-reference/chip-series-comparison.html) distinguishes the S2's single-core LX7, 2.4 GHz Wi-Fi and native USB OTG from classic ESP32; S2 has no Bluetooth.

For porter_ricks, a verified debug board could become valuable even if no networking feature is ever added to the handheld. Keeping it available as a debugger is one possible role; using it as an owned Wi-Fi peripheral is another. Those roles could require different firmware and compete for pins and availability. Wi-Fi hardware alone does not make the stock Flipper applications network-enabled.

## The Freenove WROVER is a different sort of sidecar

Classic ESP32 supports Wi-Fi plus Bluetooth Classic and BLE, with UART, SPI, I2C, I2S and SD-related interfaces; unlike S2 it has no native USB OTG. Board USB can instead be a programming/UART bridge. Exact usable pins depend on the module and board wiring. [Espressif comparison](https://docs.espressif.com/projects/esp-idf/en/v4.3.4/esp32s2/hw-reference/chip-series-comparison.html), [WROVER-E/IE module datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wrover-e_esp32-wrover-ie_datasheet_en.pdf).

Freenove's [current FNK0060 product page](https://store.freenove.com/products/fnk0060) describes a dual-core 240 MHz camera board with 4 MB flash, 8 MB PSRAM, and a memory-card slot. Treat those as one documented candidate configuration, not measured facts for this unit. If present, camera and storage make a useful event recorder or peripheral-processing companion. They also consume pins and bandwidth that cannot be assigned again merely because the ESP32 chip supports another peripheral.

The extension board may mainly make pins and power easier to reach. Freenove's [FNK0091 breakout documentation](https://docs.freenove.com/projects/fnk0091/en/latest/fnk0091/codes/tutorial/Preface.html) describes directly connected 0–3.3 V signal terminals and several supported board pinouts; it also describes its own external-power circuitry. Another Freenove extension may differ. We should not assign that jack voltage, current rating, or pin map to an unidentified extension. A supply rail marked 5 V does not make the MCU signals 5 V tolerant.

## Possible combinations to discuss

All rows below are proposals. They describe possible roles and the uncertainty each would need resolved; they are not an implementation queue.

| Proposal | Roles and useful result | Main question before design |
| --- | --- | --- |
| Handheld plus remote sub-GHz node | CC1312R stays with a sensor or controlled radio source; Flipper provides local interaction and a compatible radio endpoint | Which shared PHY and application protocol, and what should happen during link loss? |
| Instrument with a network sidecar | Flipper handles buttons/display and local interfaces; WROVER receives measurements over a wired link and serves a browser view or stores a log | Required event rate, buffering, available pins, and ownership of each record |
| Two-location packet observer | TI and Flipper observe selected compatible traffic at different locations and preserve packet/status observations for later comparison | Clock alignment and observation bias; this does not imply phase-coherent reception or direction finding |
| Event camera or sensor node | WROVER collects a sensor event, image if fitted, or local log; handheld controls the session | Actual camera/card hardware and whether radio/storage latency meets the use |
| Custom-firmware development station | Official Wi-Fi board provides debug access; TI XDS110 provides its own target's debug/log path; Flipper remains the system under development | Verified firmware, target wiring, and recovery access before any debug session |
| Small distributed network | A second ESP-family node can exchange application messages with WROVER through Wi-Fi or an appropriate peer protocol; TI can form the sub-GHz branch through a gateway | Which nodes are actually present, and why distribute this particular job? |

Espressif's [ESP-NOW documentation](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/network/esp_now.html) supplies one possible connectionless Wi-Fi transport for ESP nodes. It has channel, version, peer, and application-delivery constraints. It is not sub-GHz and does not make CC1312R or Flipper's CC1101 a direct ESP-NOW peer. Its inclusion here selects no protocol or SDK dependency.

## Portability is a system property

A development-board collection can first be understood as connected instruments without assuming that every board belongs in one enclosure. Separate nodes could sometimes make the handheld smaller and preserve antenna placement. Combining boards could reduce cabling in another use. Neither form is selected.

Before judging a portable package, the relevant unknowns are exact dimensions and connectors, available GPIO after fitted peripherals, compatible signal voltages, regulator paths and possible back-powering, peak/average load, battery/charging arrangements, antenna separation and enclosure effects, and event timing across independent clocks. These are design inputs, not a request to perform wiring or power experiments now. ESP32 and CC1312R low-power chip figures do not include the assembled board's regulator, bridge/debugger, LEDs, camera, storage, and radio duty cycle.

The strongest current distinction is between **more interfaces on a handheld** and **independent computers placed where the observation happens**. The inventory supports exploring both. Exact Pi and flight-controller models, and the operator's preferred kind of instrument, could expand the useful possibilities without committing us to a stack today.

## Source handling and scope

Reviewed linked manufacturer pages and datasheets on 2026-10-15. No additional local source corpus was acquired in this lane, so no quarantine files or archive hashes were created. TI's large SWRA588B PDF exceeded the browser's direct PDF limit; its manufacturer-hosted indexed text and TI-hosted document excerpts supplied the cited board details. No design files or source code from these platforms were run. This report complements the firmware and ESP32 SDR investigations and does not supersede device observations.
