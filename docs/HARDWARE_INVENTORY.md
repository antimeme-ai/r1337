# Hardware inventory for the discussion

Inventory is incomplete. Except for the Flipper's recorded USB/CLI observations,
these entries come from the operator's descriptions and have not been inspected
or connected by this project. Exact variants remain open where indicated.

| Equipment | What is known | Identification still needed |
| --- | --- | --- |
| Flipper Zero | USB/CLI inventory in `DEVICE.md`; reported hardware code 12 and 2023 firmware | Physical board identification and accessory connections |
| Flipper Zero Wi-Fi module v1 | Operator found the module | Physical revision/module markings and installed firmware |
| Raspberry Pis | Several available | Models, RAM, accessories, displays and power arrangements |
| TI LAUNCHXL-CC1312R1 | Operator supplied exact LaunchPad model | Physical board revision, antenna and accessories |
| Freenove ESP32-WROVER | Operator found board and ESP32 GPIO extension board | Freenove product/PCB revision, module markings, attached peripherals |
| Xilo flight controller | Operator found board | Exact model, MCU, sensors, connectors and documentation |
| Bus Pirate | Operator owns one and is locating it | Generation, board revision, firmware and probe accessories |
| Assorted modules | Additional parts available | Continue inventory as the operator introduces them |

## Questions for the eventual capability map

For each identified board, distinguish processor, physical interfaces, RF front
end, measurement capability, local timing, host/control transport, storage,
power, and mechanical dimensions. A GPIO extension board alone does not establish
new radio, measurement, or electrical-interface capabilities.

Map complementarity and overlap before deciding what belongs in a portable
assembly. Candidate roles include a handheld interface, a local computing host,
detachable wired/RF instruments, and separately powered remote nodes. These are
discussion options, not assignments of particular boards to a selected design.

The operator is interested in a new portable form factor and in recent ESP32
SDR developments. Assess those against the actual chip generations and data
paths. Internal sample rate, sustained exported I/Q rate, capture duty cycle,
tuning range and phase coherence are separate properties.
