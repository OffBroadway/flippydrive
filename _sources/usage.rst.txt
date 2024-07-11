Using the FlippyDrive
=====================

.. _sdcard:

SD Card
````````````````

You can use any SDHC/SDXC card with FlippyDrive. We do not suggest using SD Cards with a capacity less than 4GB as those may have compatibility issues.

.. _sdcardsetup:

SD Card Setup
------------------

In order to use the FlippyDrive you must first format the SD card or configure Wi-Fi to target a desktop machine.

.. todo
    Wi-Fi configuration is in internal testing and will be available shortly

Make sure your SD card is formatted with exFAT or FAT32. We suggest using exFAT as it is a more modern standard.

.. _sdcardfiles:

SD Card Files
------------------

Once your SD card is formatted you can place ``.ISO``, ``.GCM``, or ``.FDI`` files in the root of the SD card.

.. note::
    Currently only files ending in ``.ISO`` are detected by cubeboot. If you have a GCM or NKIT file, simply rename it to ISO.
    Folders are not currently supported. This will change in the future.

.. _usage:

Usage
````````````````

Now that you have your SD card setup you can insert it into the FlippyDrive and power on your GameCube.

.. _startup:

Startup
------------------

When booting the GameCube using FlippyDrive you have three options:


.. _updatemode:

Update Mode
-----------

If you hold down the ``X`` button on the P1 controller it will start a software update.

.. _bypassmode:

Passthrough Mode
------------------

Two passthrough modes are provided by the FlippyDrive to launch games in the physical disc drive.

Enhanced Passthrough
********************

Hold the ``R`` trigger on P1 when powering up the console to enter enhanced passthrough mode.

This process uses your physical disc loaded via cubeboot with the ``config.ini`` file with read with appropriate video and region-free settings applied.

Pure Passthrough
****************

Hold the ``L`` trigger on P1 when powering up the console to enter pure passthrough mode.

Control is handed completely to the physical disc drive and the disc will load as if no FlippyDrive is installed.  That means your disc and console must match regions and no additional features are available as this is stock gamecube behavior.

Once control is handed off to the drive in pure mode, it is not possible to exit unless you power off the GameCube.

.. _cubeboot:

Normal Mode
-----------

If you do not hold down any buttons while the GameCube is turning on, it will boot directly into Cubeboot. However if you have placed a ``boot.dol`` file in the root of your SD card it will boot that program instead.

Cubeboot will play the GameCube startup animation and then jump directly into the Cubeboot Loader which allows you to select a game to play.

You can navigate the loader with the analog stick and press a to select a game. If you do not want to start that game simply press ``B`` to get back to the list of games.

Once you are ready to play press start on the game select screen and it will immediately boot the game.

.. seealso::
    If you experience any issues during gameplay please reference the compatibility page and submit a bug report using the form.
    
    For FlippyDrive bugs go to :doc:`troubleshooting`
    For Game related issues while using FlippyDrive check :doc:`compatibility` and submit a bug report.

    For more information on configuring the FlippyDrive check the :doc:`configuration` page.

.. toctree::
    :hidden:

    updates
    backup

