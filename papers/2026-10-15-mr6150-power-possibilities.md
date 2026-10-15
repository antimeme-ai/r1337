# MR6150 and portable power possibilities — 2026-10-15

The operator reports an unlocked Nighthawk M6 MR6150 and a flat battery marked
3.85 V, 19.4 Wh, plus FPV packs with specifications still unknown. This report
uses manufacturer sources and label arithmetic; no hardware was inspected,
connected, discharged, reconfigured or modified.

## Router role

NETGEAR lists MR6150 variants with sub-6 GHz cellular service, dual-band Wi-Fi 6,
1000BASE-T Ethernet and a removable 5040 mAh battery. Regional cellular bands
differ; the suffix is not yet known. Published weights/dimensions vary slightly
between the technical sheet and support table, so final geometry needs actual
measurements. The MR6150 should retain its own model's capabilities when reading
family documentation that also covers M6 Pro.
[Model/SKU table](https://kb.netgear.com/000065402/What-are-the-specifications-of-the-NETGEAR-M6-and-M6-Pro-mobile-hotspot),
[MR6150 technical sheet](https://www.downloads.netgear.com/files/GDC/MR6150/MR6150_TS.pdf).

The acquired family manual's printed page 16 documents USB tethering to a
computer; page 69 lists USB and Ethernet ports. The model sheet also advertises
phone charging through USB-C. These document specific device/power functions,
not general USB-host support for our instruments or a characterized supply for
their loads. The sheet's unlocked-carrier description also does not establish
root access, replacement firmware support, or raw cellular I/Q access.
[Family manual](https://www.downloads.netgear.com/files/GDC/MR6400/MR6400_UM_EN.pdf).

One useful candidate role is independent cellular backhaul for a portable host
or distributed experiment. Keeping it intact would retain its existing modem,
router and managed battery system. Repackaging or reusing its battery is a
different electrical/mechanical project. Neither is selected. Active cellular
and Wi-Fi operation also becomes part of the environment a nearby RF instrument
would observe; placement and intended radio states would matter to a later test.

## What the battery label tells us

The operator's values imply approximately `19.4 Wh / 3.85 V = 5.04 Ah` nominal,
consistent in magnitude with the model's published 5040 mAh. That does not
identify the actual pack, measure its condition, or establish connector/charging
requirements.

For energy budgeting only:

| Assumed total draw from the pack | Ideal duration from 19.4 Wh |
| --- | ---: |
| 2 W | 9.7 h |
| 5 W | 3.88 h |
| 10 W | 1.94 h |

These are calculations, not estimates of any proposed assembly's load or runtime.
Conversion losses, reserve, battery condition, operating temperature and changing
radio/compute loads reduce or alter useful duration. The flat shape is a useful
mechanical possibility; 3.85 V is a nominal battery voltage, not an established
regulated 5 V instrument supply. Part number, full-charge specification,
protection, temperature/identification contacts and power conversion remain
inputs before an electrical design can be made.

The FPV packs create additional options, with cell count, chemistry, voltage,
energy and connector unknown. Their labels and actual intended workloads should
precede any comparison with the Nighthawk pack. No charging, switching or
common-battery topology is proposed by this report.

## Literature acquisition

Both original PDFs were downloaded unchanged on 2026-10-15 and remain ignored:

| Local path | Exact source | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `papers/network-power/mr6150-technical-specifications.pdf` | `https://www.downloads.netgear.com/files/GDC/MR6150/MR6150_TS.pdf` | 162641 | `5c6013cd224323e9a6b2887bc49716cb2b03995ad88840755859f86763f29bf7` |
| `papers/network-power/m6-family-user-manual.pdf` | `https://www.downloads.netgear.com/files/GDC/MR6400/MR6400_UM_EN.pdf` | 2267726 | `d9b0c2b28ca219a68b4b588552b892c6633c107f1033908fe93f40fdd57eb9ea` |

Read the one-page technical sheet and the manual's tethering, power-manager,
battery and port sections. The full family manual was not read end to end.
Existing `pdftotext` extracted relevant text to ignored `context/`.
Restore from the project root:

```sh
mkdir -p papers/network-power
curl -fL 'https://www.downloads.netgear.com/files/GDC/MR6150/MR6150_TS.pdf' -o papers/network-power/mr6150-technical-specifications.pdf
curl -fL 'https://www.downloads.netgear.com/files/GDC/MR6400/MR6400_UM_EN.pdf' -o papers/network-power/m6-family-user-manual.pdf
shasum -a 256 papers/network-power/*.pdf
```

The documents carry NETGEAR's notices; this is literature acquisition, not an
implementation or dependency adoption. No additional source archive was acquired.
