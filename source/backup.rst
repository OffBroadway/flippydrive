Disc Backup Utility
*******************

.. image:: /_static/bootloader_backup.png
  :width: 50%

The FlippyDrive provides an integrated disc backup utility and can be launched through the :doc:`bootloader`.
This program will read and checksum the current disc loaded in the drive while saving it to the current storage device.  Usually this storage destination is the microSD card, although you can backup to your computer over the network in Wi-Fi and Ethernet mode if they are set as default as described in :doc:`the configuration file<configuration>`.

Stored disc images are immediately usable in cubeboot.

The backup utility provides two modes, both of which store disc images accurately although using different mechanisms.

Fallback Mode
-------------
Fallback mode uses a two step transfer, where data is loaded from disc into GameCube memory then sent to the FlippyDrive for storage.  This allows the FlippyDrive backing storage arbitrary time to write the data although the transfer rates will be reduced significantly.
The backup process can take anywhere from 25 minutes to over an hour.

Fast Mode
---------
.. warning:: This mode is currently not available yet
.. versionadded: 1.5.0

The FlippyDrive will snoop on drive traffic in fast mode and attempt to store data as it is streaming by.  This will likely succeed in SD mode and will likely fail in Network modes.  The program will inform you if the FlippyDrive storage medium cannot keep up and the transfer will abort.
