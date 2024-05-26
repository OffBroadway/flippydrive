Software Updates
================

.. _sdinstall:

Install from µSD
````````````````

In order to install software updates from the micro SD card, you must download the `update.fpkg` file from the latest `FlippyDrive assets GitHub repo <https://github.com/OffBroadway/flippydrive-assets/releases>`_. Look for the latest release and download the update file.

You can then place the file on the root of your SD card. It must be named ``update.fpkg`` in order for the FlippyDrive to detect the update properly.

In order to start the update, you must hold down ``X`` on the P1 controller while turning on the GameCube.

There is an alternative to doing this where you can create an empty file called forceupdate on the root of the SD card as well. This will do the same thing as holding down ``X`` and force the FlippyDrive to do a software update when it starts.

.. _usbinstall:

Install via USB
```````````````

.. hint::
    This process is only necessary if the firmware has somehow become corrupt and unbootable. You should always use the SD install process first, and attempt a software reinstall of the current version by holding ``X`` at boot.

In order to install a software update from USB you have to perform a full recovery. 
This method must be performed while the GameCube is turned off. It is suggested that you remove the power cable from the back of the GameCube.


.. _disassembly:

Disassembly
------------------
First you must open your GameCube to get access to the FlippyDrive. Depending on the size of your micro USB cable you may need to unscrew the two retaining screws that hold the FlippyDrive in place.

Be very careful when doing so as to not put undue stress on the flex cable. The flex cable is quite delicate and may tear. If you need to unscrew the posts it is suggested that you unclip the flex cable from the FlippyDrive first so that it is not dangling.

.. _connecting:

Connecting to PC
------------------
Before plugging in the USB cable hold down the button on the front of the FlippyDrive while inserting the USB. You will know that it worked if a USB drive called "RPI-RP2" is mounted on your computer.


You can download the latest recovery.uf2 firmware file from the `FlippyDrive assets GitHub repo <https://github.com/OffBroadway/flippydrive-assets/releases>`_. Look for the latest release and download the recovery file.

.. _installing:

Installing
------------------

In order to install the firmware simply copy the recovery.uf2 file into the USB drive labeled "RPI-RP2" and wait for the copy to complete. You will know that it is done when the drive Auto ejects and disappears.

.. note::
    Installing via this method will wipe out the internal flash on the FlippyDrive. This means any Homebrew dol files you have copied over will be removed.
    
    This method does not affect the SD card at all and it is safe to use while the SD card is inserted.


.. _reassembly:

Reassembly
------------------

Next you can unplug the USB cable and mount the FlippyDrive back to the mounting post with the two screws.

If you have unplugged the flex cable insert it as directed in the install guide with the matching square symbol facing out.
