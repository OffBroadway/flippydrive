.. flippydrive documentation master file, created by
   sphinx-quickstart on Wed May 15 22:51:02 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

FlippyDrive Documentation
=========================

The FlippyDrive is an optical drive emulator for the GameCube, designed so you can keep your OEM drive installed and use both.

.. todo::
   Photo of FlippyDrive
   
.. admonition:: Having Trouble?
   :class: hint

   Check out the :doc:`troubleshooting` section
   
Major Features
==============

- :doc:`No-solder internal install <installation>` into the original Disc Drive slot
- Load games from :doc:`µSD Card <sd>`
- Experimental loading over :doc:`Wi-Fi <wifi>` (RPi / PC / NAS)
- No software patching required (games can run stock)
- Preinstalled `Cubeboot <https://github.com/OffBroadway/cubeboot>`_ menu patcher
- Keep your original disc drive installed and :ref:`play physical discs <bypassmode>`
- Software updates via :ref:`SD card <sdintall>` or :ref:`USB drag-and-drop/brick recovery <usbintall>`


   
.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents:
   
   installation
   usage
   troubleshooting
   sd
   network
   developer
