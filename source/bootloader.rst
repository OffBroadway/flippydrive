Bootloader menu
***************

If you hold :kbd:`X` while powering on the GameCube, the GameCube boots to the FlippyDrive bootloader menu.

.. image:: /_static/bootloader.png
  :width: 50%


Update/Reinstall Firmware
=========================
This option updates the FlippyDrive firmware from any ``update.fpkg`` file placed on the inserted microSD card. Otherwise, it will reinstall the current firmware from the backup copy.

.. _Boot DOL:

Boot Onboard DOL
================
.. image:: /_static/bootloader_boot.png
  :width: 50%

It is possible to launch onboard DOL files from the FlippyDrive flash storage directly.

.. note:: Any other files copied to the FlippyDrive flash storage through Swiss will also show up here. Please note that any custom DOL files will be erased during the firmware update process.

- backup
    This launches the :doc:`backup`.

- cubeboot
    This launches cubeboot, basically the same thing that happens when powering up the GameCube without opening the bootloader.

- remote-access
    This launches remote access so that you can transfer files from/to the microSD card through FTP and/or SMB. Check out the :doc:`remote-access` for more information.
- swiss-gc
    This launches the homebrew software `Swiss <https://github.com/emukidid/swiss-gc>`_.

Boot Disc Mode
==============

.. hint:: Formerly known as Pure Bypass mode. You can also hold down :kbd:`L` while turning on the GameCube to boot directly to Disc Mode.

This starts Disc Mode. For more information, check out the :doc`usage`
This allows you to boot physical media from the DVD drive, your GameCube will function the same as if it's a original GameCube, with the same restrictions.

Control is handed completely to the physical disc drive and the disc will load as if no FlippyDrive is installed.  That means your disc and console must match regions and no additional features are available as this is stock GameCube behavior.

Boot Enhanced Disc Mode
=======================
.. versionadded:: 1.3.0

.. hint:: Formerly known as Enhanced Bypass mode. You can also hold down :kbd:`R` while turning on the GameCube to boot directly to Enhanced Disc Mode.

This allows you to boot physical media from the DVD drive via cubeboot, in Enhanced Disc Mode. Enhanced Bypass mode allows you to bypass region restrictions. Please note that this mode is currently a bit unstable.


Exit
====
Exits the bootloader.