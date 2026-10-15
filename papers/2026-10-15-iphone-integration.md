# Old iPhones as instrument components

Research date: 2026-10-15. The operator offers existing old iPhones for this
project and subsequently identified an iPhone 11 Pro Max on iOS 17.4.1 and
iPhone 14 Pro Max on iOS 26.6, with one or two more possibly available. These
versions are operator reports; no phone was inspected or modified, and no app
installed. Battery condition, capacity and actual accessory behavior are unknown.

## Identified models and current jailbreak lead

Apple documents [11 Pro Max](https://support.apple.com/en-us/111878) with A13,
Lightning, a 6.5-inch OLED, triple 12 MP rear cameras, GNSS/compass, barometer,
gyro and accelerometer. Apple documents
[14 Pro Max](https://support.apple.com/en-us/111846) with A16, Lightning, a
6.7-inch OLED, 48 MP main camera, macro photography and LiDAR. The 14 Pro Max
is therefore a particularly interesting optical/scene-inspection candidate,
but these are manufacturer features rather than measured accuracy or an
implemented data-export path. Model-family specifications do not identify the
owned phones' storage, battery condition or regional cellular variant.

Both reported OS versions exceed the current Tailscale App Store minimum.
This clears the version threshold, not installation, login, tailnet policy,
network reachability or our future application's behavior.

The operator will look for an older phone to improve jailbreak options. Current
primary documentation provides a useful lead already: the official
[Dopamine site](https://ellekit.space/dopamine/) and
[3.0.11 README](https://github.com/opa334/Dopamine/blob/3.0.11/README.md)
list A12/A13 support across iOS 15.0–18.7.1 (also 26.0–26.0.1).
The identified 11 Pro Max/A13 on 17.4.1 falls within that advertised range.
The 14 Pro Max/A16 on 26.6 does not fall within those documented ranges. No
claim is made about every other possible tool or future support, and the
advertised range has not been tested on either owned phone.

[Palera1n's official site](https://palera.in/) lists A8–A11 devices (and T2),
so neither identified phone belongs to that supported chip range. An older
phone's exact chip and installed OS/build are useful inputs; age alone is not
a compatibility criterion. No exploit, jailbreak or downgrade was attempted.
A rootless jailbreak's advertised support also does not establish a generic
USB instrument driver, baseband I/Q access or a replacement operating system.

## Candidate role

A complete phone could contribute camera, display, touch controls, microphone,
local storage and network-client functions together. Exact optics, focus,
motion/location sensors, cellular service and supported APIs depend on the
identified model, OS and permissions. LiDAR is documented on the identified
14 Pro Max; thermal imaging and ambient temperature measurement are not
established. In particular, using the phone as a camera
does not fulfill the separate environmental-temperature objective.

A candidate arrangement is an instrument controller handling acquisition and
hardware interfaces, with a phone presenting a network UI and submitting images
or observations to remote support. This is an architectural inference, not a
tested integration. Compare a finished internal mount/dock against separate
screen/camera/input electronics. A removable phone would occupy the one
permitted companion role; it must not silently add a second carried module.

## Network software must match the actual OS

Tailscale's [iOS installation guide](https://tailscale.com/docs/install/ios)
still says iOS 15 or later and is marked last validated February 2025. The
[October 7, 2026 changelog](https://tailscale.com/changelog#2026-10-7)
states that v1.104 drops iOS 15. The current
[App Store listing](https://apps.apple.com/us/app/tailscale/id1470499037)
specifies iOS 16.6 or later. Use the listing's more specific current requirement
for the current App Store build; do not assign current-app compatibility to an
unidentified old phone. Earlier build availability/support was not established.
An older phone may still be worth comparing as a local UI/camera if its supported
network/app path works; this has not been tested.

## A connector does not establish general instrument access

Apple's [external storage guide](https://support.apple.com/guide/iphone/external-storage-devices-iph95baac91f/ios)
documents USB storage/SD access with compatible adapters and external power
arrangements. That establishes specific supported classes, not arbitrary access
to a USB serial adapter, logic analyzer or SDR.

Apple's [External Accessory framework](https://developer.apple.com/documentation/externalaccessory/)
describes communication with supported MFi accessories. Its
[DriverKit guide](https://developer.apple.com/documentation/driverkit/creating-drivers-for-ipados)
describes macOS/iPadOS drivers and requires M-series iPads for that iPad path.
An [Apple DTS explanation](https://developer.apple.com/forums/thread/793915)
explicitly distinguishes iPadOS driver access from effectively nonfunctional
IOKit on iOS. Consequently, a USB plug/adapter alone is insufficient evidence
for using an iPhone as our generic instrument host. Standard class-specific
accessories and custom MFi accessory support are separate questions from that
general-driver path; neither has been tested here.

## Design lessons and next discriminating inputs

Retaining the complete phone preserves a working camera/display/power assembly
as a candidate; it also introduces OS/app lifecycle, charging, heat and mechanical
constraints. A network boundary could keep hardware timing and instrument
drivers on a controller while allowing an identified phone to provide a richer
interface. This would need a usable offline/local link, camera upload path,
charging arrangement and comfortable screen/probe orientation.

The two identified models now permit more specific app/network and accessory
research; record exact models/builds of any others found. No platform adoption,
jailbreak, native app, framework,
adapter purchase or physical modification is selected. Primary sources above
were read live; no source archive was acquired for this note.
