.. FlippyDrive documentation master file, created by
   sphinx-quickstart on Wed May 15 22:51:02 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

FlippyDrive Documentation
=========================

The FlippyDrive is a solderless optical drive emulator for the GameCube, designed so you can keep your OEM drive installed and use both.

.. image:: _static/4X1A7535.jpg
    :width: 100%
   
.. .. admonition:: Having Trouble?
   :class: hint

   Check out the :doc:`troubleshooting` section
   
.. admonition:: Just got your FlippyDrive?
   :class: hint
   
   Check for the latest software info at `https://teamoffbroadway.com/category/updates/fd-software/ <https://teamoffbroadway.com/category/updates/fd-software/>`_

Major Features
==============

- :doc:`No-solder internal install <installation>` into the original Disc Drive slot
- Load games from µSD Card
- Experimental loading over :doc:`Wi-Fi <wifi>` (RPi / PC / NAS)
- No software patching required (games can run stock)
- Preinstalled `cubeboot <https://github.com/OffBroadway/cubeboot>`_ menu patcher
- Keep your original disc drive installed and :ref:`play physical discs <bypassmode>`
- Software updates via :ref:`SD card <sdinstall>` or :ref:`USB drag-and-drop/brick recovery <usbinstall>`
   
.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents:
   
   installation
   usage
   configuration
   compatibility
   troubleshooting
   network
   mods
   developer
