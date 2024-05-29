Other Mod Compatibility
=======================

Picoboot and other IPL replacements
```````````````````````````````````

Because Picoboot and other IPL replacements feed the GameCube a non-stock boot program, Cubeboot is not compatible with these mods. It is not necessary to remove them, but they must be disabled according to their respective project's documentation.

Pico based mods like the Picoboot can be disabled simply by erasing the flash using the first-party ``picotool``.

GCVideo
```````

In general, GCVideo output mods work just fine, although some are very poorly designed electrically. We have received reports that when coupled with questionable displays, a few backpower the GameCube's 5V rail even when the GameCube is off in violation of the HDMI specification's reverse current protection requirement.

In addition to the damage this may be doing to the GameCube, it keeps the FlippyDrive powered up while the cube is off, usually resulting in the previously selected game immediately launching or region errors depending on the game and cube in question. We are gathering more information on how prevalent this is.

Power
`````

The FlippyDrive consumes very little power in SD card mode, and much more in Wi-Fi mode, but still less than the drive. It also enters a lower power state during drive bypass. 

While all GameCubes tested had sufficient power margins to run the FlippyDrive and disc drive simultaneously for disc ripping purposes, many mods consume large amounts of power without considering how it may affect other mods.

As the FlippyDrive is a net negative power consumer vs operating the disc drive, we have not noticed any power-related compatibility issues. If you are building a heavily modded GameCube, keep in mind that the GameCube has a very limited power budget and many mods are designed with little regard to how they may interfere electrically.

We will update this with more information as we receive reports.
