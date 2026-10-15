# Hardware acquisitions — 2026-10-15

## Acquired literature

Original PDFs are retained unmodified in ignored `papers/hardware/`. The
reconnaissance report is
[2026-10-15-hardware-frumentarii.md](2026-10-15-hardware-frumentarii.md).
No executable reference implementation or source archive was acquired by this
lane, and there is no extracted reference tree requiring quarantine cleanup.

| Local PDF | Primary source | Bytes | Pages | SHA-256 |
| --- | --- | ---: | ---: | --- |
| `papers/hardware/swrs061i-cc1101.pdf` | [TI CC1101 datasheet, SWRS061I](https://www.ti.com/lit/ds/symlink/cc1101.pdf) | 2,758,709 | 112 | `daa14cd9b83adf92545ab072939f85f6a8fef9ce654e3f37366087db714ea639` |
| `papers/hardware/sstic2025-cougnard-stm32wb55.pdf` | [Thomas Cougnard, SSTIC 2025 paper](https://www.sstic.org/media/SSTIC2025/SSTIC-actes/recupration_de_la_cle_des_firmwares_radio_du_stm32/SSTIC2025-Article-recupration_de_la_cle_des_firmwares_radio_du_stm32wb55-cougnard_61Kne8u.pdf) | 863,833 | 16 | `052566b133efa8d53a841e2ac6effbb472be8b5910c2d51b9622f0ca78636c89` |
| `papers/hardware/sstic2025-cougnard-stm32wb55-slides.pdf` | [Thomas Cougnard, SSTIC 2025 slides](https://www.sstic.org/media/SSTIC2025/SSTIC-actes/recupration_de_la_cle_des_firmwares_radio_du_stm32/SSTIC2025-Slides-recupration_de_la_cle_des_firmwares_radio_du_stm32wb55-cougnard.pdf) | 16,218,828 | 135 | `422d7fb8d13b90a4c2235b29a948a60381e5c0d7e18a7aade8ef8f5000b60929` |

The paper's author is Thomas Cougnard (Xilokar). The printed CC1101 document
comprises the 98-page datasheet plus appended package and ordering material;
`pdfinfo` reports 112 physical pages. Page counts are reported for locating
content, not as evidence of complete reading.

Restore from the project root:

```sh
mkdir -p papers/hardware
curl -fL --connect-timeout 10 --max-time 120 \
  -o papers/hardware/swrs061i-cc1101.pdf \
  'https://www.ti.com/lit/ds/symlink/cc1101.pdf'
curl -fL --connect-timeout 10 --max-time 120 \
  -o papers/hardware/sstic2025-cougnard-stm32wb55.pdf \
  'https://www.sstic.org/media/SSTIC2025/SSTIC-actes/recupration_de_la_cle_des_firmwares_radio_du_stm32/SSTIC2025-Article-recupration_de_la_cle_des_firmwares_radio_du_stm32wb55-cougnard_61Kne8u.pdf'
curl -fL --connect-timeout 10 --max-time 120 \
  -o papers/hardware/sstic2025-cougnard-stm32wb55-slides.pdf \
  'https://www.sstic.org/media/SSTIC2025/SSTIC-actes/recupration_de_la_cle_des_firmwares_radio_du_stm32/SSTIC2025-Slides-recupration_de_la_cle_des_firmwares_radio_du_stm32wb55-cougnard.pdf'
```

The TI symlink can change; compare the resulting document code and revision
with SWRS061I and the table's digest before treating it as the same edition.
The PDFs' own notices and the SSTIC publication pages are the source locations
for publication and reuse terms. No project licensing conclusion is drawn.

## Needed sources with acquisition failures

These belong in the root's shopping list unless another lane obtains them.
Reachable web-rendered text is not a local PDF acquisition.

| Needed item | Primary source | Failure and remaining work |
| --- | --- | --- |
| Flipper main board assembly and schematics, especially MCU, power, buttons, peripheral buses | [Official schematic index](https://docs.flipper.net/zero/development/hardware/schematic) | Linked S3 PDF URLs carry February 2024 signatures and return 403. Thirteen main/peripheral schematic links were checked; removing the query from the MCU object URL also returns 403. Obtain fresh official links or exports. |
| DS11929 STM32WB55 datasheet | [ST PDF](https://www.st.com/resource/en/datasheet/stm32wb55rg.pdf) | Web can read served Rev 18; local Python HTTPS read times out, curl HTTP/2 returns stream error, HTTP/1.1 stalls. Obtain original PDF locally. |
| RM0434 STM32WB reference manual | [ST PDF](https://www.st.com/resource/en/reference_manual/rm0434-multiprotocol-wireless-32bit-mcu-armbased-cortexm4-with-fpu-bluetooth-lowenergy-and-802154-radio-solution-stmicroelectronics.pdf) | Web exceeds 10 MiB content limit; local transfer fails as above. ST catalog locates Rev 16 (9 March 2026), not verified from PDF bytes. Most important outstanding register reference. |
| AN5185 FUS | [ST PDF](https://www.st.com/resource/en/application_note/an5185-how-to-use-stmicroelectronics-firmware-upgrade-services-for-stm32wb-mcus-stmicroelectronics.pdf) | Relevant Rev 15 sections read through web; local transfer fails. Need the original plus version-specific release notes matching this unit's reported FUS 1.2.0. |
| AN5289 wireless application integration | [ST PDF](https://www.st.com/resource/en/application_note/an5289-building-wireless-applications-with-stm32wb-series-microcontrollers-stmicroelectronics.pdf) | Relevant Rev 18 sections read through web; local transfer fails. Earlier guessed alternate title failed; use this actual linked title. |
| AN2606 boot ROM | [ST PDF](https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf) | Rev 70 §81 read through web; local transfer fails. Earlier guessed title failed; use this actual linked title. |
| ES0394 errata | [ST PDF](https://www.st.com/resource/en/errata_sheet/es0394-stm32wb55xxstm32wb35cx-device-errata-stmicroelectronics.pdf) | Selected Rev 18 sections read through web; local transfer fails. Note there is no hyphen between `stm32wb55xx` and `stm32wb35cx` in the working URL. |
| SA0024 CPU isolation advisory | [ST PDF](https://www.st.com/resource/en/security_advisory/sa0024-potential-isolation-issue-between-cpu1-and-cpu2-on-stm32wb5x-stm32wb3x-stm32wb1x-and-stm32wl5x-stmicroelectronics.pdf) | Full Rev 1 advisory read through web. Local acquisition not attempted after repeated common-host transfer failures; still obtain original. |

The official historical documentation source at
[`flipperdevices/docs`, commit `498bcb8e49a1ef07fc72683d935ede147dbb96b8`](https://github.com/flipperdevices/docs/tree/498bcb8e49a1ef07fc72683d935ede147dbb96b8)
was inspected remotely at `en/content/development/hardware/schematic.md`.
It points to old Altium identifiers rather than hosting PDFs. It describes
stripped component values. This is historical reference, not current workspace
instructions or confirmation of present board routing. No archive was retained.

No purchased material is required yet. The items above are access/download gaps,
not recommendations to adopt a vendor SDK or acquire a particular debug board.
