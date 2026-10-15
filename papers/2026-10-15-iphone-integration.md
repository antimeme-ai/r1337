# Old iPhones as instrument components

Research date: 2026-10-15. The operator offers existing old iPhones for this
project. Exact models, iOS versions, connector types and battery condition are
unknown. No phone was inspected or modified and no app installed.

## Candidate role

A complete phone could contribute camera, display, touch controls, microphone,
local storage and network-client functions together. Exact optics, focus,
motion/location sensors, cellular service and supported APIs depend on the
identified model, OS and permissions. No LiDAR, thermal imaging or ambient
temperature measurement is assumed. In particular, using the phone as a camera
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

Identify models and OS versions first, then inspect the supported app/network
and accessory paths. No platform adoption, jailbreak, native app, framework,
adapter purchase or physical modification is selected. Primary sources above
were read live; no source archive was acquired for this note.
