# Network and USB instrument possibilities — 2026-10-15

The additional devices add three useful kinds of machinery: a Linux Wi-Fi appliance, a dual-band USB radio, and programmable USB peripherals. They could complement the Flipper, ESP32s, and TI board as observers or controlled test counterparts. Their useful role depends on which side of each connection they occupy; connector shape alone does not determine that role.

This is an understanding pass using primary Hak5/O.MG documentation. No device was connected, powered, interrogated, configured, or activated by this lane. No payload, network experiment, installation, or architecture selection follows from these possibilities. Existing device firmware and configuration remain unknown.

## Inventory interpretation

| Reported item | Manufacturer-documented platform role | Identification still needed |
| --- | --- | --- |
| WiFi Pineapple Mark VII | Network appliance with internal Wi-Fi radios, USB-facing Ethernet and USB host expansion | Hardware revision, firmware, enabled services, present configuration |
| MK7AC auditing adapter | MediaTek MT7612U dual-band USB Wi-Fi adapter | Confirm label and fitted antennas; firmware/driver compatibility on eventual host |
| Bash Bunny | Linux computer presenting programmable USB peripheral functions | Mark I or II, firmware, stored automation and current switch-selected behavior |
| “om.g plug” | Candidate O.MG Plug: Wi-Fi-managed USB HID peripheral | Exact product, Basic/Elite tier, firmware, activation state, accessories |

Hak5's [Mark VII specifications](https://shop.hak5.org/products/wifi-pineapple?variant=11303845317) distinguish it from Enterprise and Pager: three role-oriented 2.4 GHz radios, a single-core MIPS network SoC, 256 MB RAM, 2 GB eMMC, USB-C power/Ethernet, and a USB 2.0 host port. Newer Pineapple products' 6 GHz, CPU, storage, or radio specifications should not be assigned to this unit.

## The Pineapple is an active computer with two different USB roles

The USB-C connection supplies power and presents an Ethernet interface to a computer. Hak5 identifies its host-facing USB Ethernet hardware as ASIX AX88772. The separate host port accepts supported peripherals; documentation explicitly covers USB storage and an added USB Ethernet adapter. It is therefore possible to have the Pineapple act as a USB host on one port while a computer accesses its networking through the other. [Connection/power guide](https://documentation.hak5.org/wifi-pineapple/setup/connecting-the-wifi-pineapple), [USB Ethernet hardware](https://documentation.hak5.org/wifi-pineapple/faq/macos-support), [host-side network adapter support](https://documentation.hak5.org/wifi-pineapple/faq/establishing-an-internet-connection/configuring-a-usb-ethernet-adapter).

The management interface is available through its USB Ethernet connection or configured management Wi-Fi. This gives a possible control plane for a portable instrument, but does not make it an ordinary Ethernet dongle or passive USB hub. Nor does the USB-C connection imply an arbitrary USB gadget interface under our control. [Manufacturer UI overview](https://documentation.hak5.org/wifi-pineapple/ui-overview/introduction).

Hak5's macOS page reports compatibility limitations for the AX88772 connection on macOS 11 and later. That is a documented integration uncertainty, not an observation about the current Mac or a reason to install anything during inventory. Wireless management is a distinct connection path. [MacOS support page](https://documentation.hak5.org/wifi-pineapple/faq/macos-support).

For power, Hak5 specifies a source delivering basic 5 V and at least 2 A continuously, and describes compatibility issues with some USB-C power sources. This is source-sizing guidance, not measured continuous consumption. Extra radios, storage, and the selected workload affect the eventual budget; neither a connector nor a battery's energy label establishes suitable output or runtime. [Manufacturer power guidance](https://documentation.hak5.org/wifi-pineapple/setup/connecting-the-wifi-pineapple).

## MK7AC adds another Wi-Fi receiver/transmitter

Hak5 identifies [MK7AC](https://shop.hak5.org/collections/in-byofk/products/mk7ac-wifi-adapter) as an MT7612U adapter supporting 802.11a/b/g/n/ac at 2.4 and 5 GHz, with two RP-SMA antennas and a USB 3.0 interface. Its [compatibility document](https://documentation.hak5.org/wifi-pineapple/faq/compatible-802.11ac-adapters) specifically lists MT7612U support on Mark VII. The adapter is a USB peripheral requiring a host and driver, not a standalone network computer.

The practical addition is 5 GHz and an independently assignable observation interface beyond the Pineapple's built-in 2.4 GHz radios. The advertised 866 Mbit/s link figure is not capture throughput, storage throughput, or the speed available through Mark VII's USB 2.0 host. Monitor capability also does not mean simultaneous observation of every channel or raw wideband I/Q capture. Actual observation coverage depends on channel selection, radio allocation, driver behavior and dropped-frame handling.

## Bash Bunny supplies programmable USB counterparts

Hak5 describes [Bash Bunny](https://shop.hak5.org/products/bash-bunny) as a Linux/Debian computer with serial access and selectable automation. Its USB functions can include serial console, mass storage, HID keyboard and Ethernet emulation, in supported combinations. That provides a potential controlled counterpart for testing USB host behavior or a laboratory computer's handling of device classes. It is more capable than a thumb drive, and its stored behavior matters before attachment. [Manufacturer USB function documentation](https://docs.hak5.org/bash-bunny/writing-payloads/attackmode).

Generation remains important: Hak5 lists Bluetooth LE and microSD expansion for Mark II. Those should not be assumed for a unit merely called Bash Bunny. Nor does its Linux CPU make its exposed USB plug a general USB host receptacle. The relevant documented connection role here is a programmable device attached to a host. [Mark I/II comparison](https://shop.hak5.org/products/bash-bunny).

## O.MG Plug is a narrow candidate identification

The spelling “om.g plug” plausibly refers to Hak5's [O.MG Plug](https://hak5.org/collections/mischief-gadgets/products/omg-plug), but this remains unconfirmed. The product page documents Wi-Fi browser management, keyboard/mouse functions, onboard stored automation, and different Basic/Elite tiers. It is an active programmable USB endpoint. It should not be assigned the role of power adapter, passive connector, host controller, or hub from the word “plug.”

The [official product comparison](https://shop.hak5.org/pages/o-mg-compare) separates Plug, Cable and Adapter products. Features of an O.MG Cable or Adapter cannot be transferred to an unidentified Plug. A controlled HID counterpart is a plausible instrument role; a general Linux sidecar, inline USB protocol analyzer, or arbitrary USB-class emulator is not established by these sources.

## Possibilities to discuss

These are proposals, not selected experiments:

- **Independent packet observer:** Pineapple plus MK7AC could observe a chosen channel while an owned ESP32 node runs the application being studied. A second device's observations can help distinguish missing transmissions from application logging failures, while still requiring clock alignment and explicit capture-loss accounting.
- **Separate management network:** the appliance could supply a management path for a collection of nodes. Management and observation roles would need deliberate allocation; extra radios do not remove channel and interference constraints.
- **Controlled USB endpoints:** Bash Bunny could represent selected supported USB classes, with candidate O.MG Plug representing a narrower HID case, when examining a known laboratory host. Two USB peripherals do not communicate merely by joining their plugs: a compatible host controller and suitable power/data arrangement are required.
- **A portable kit of instruments:** the network appliance, USB counterparts, handheld and remote sensor nodes could remain separate tools. Understanding them does not require putting all their electronics into one battery-powered enclosure.

The next useful discussion inputs are exact variants, present state and the behavior the operator wants to understand. No current evidence requires activating these devices, changing their stored behavior, or selecting an implementation architecture. This lane acquired no archives; its sources remain linked manufacturer documents reviewed on 2026-10-15.
