Configuration File
*******************

The FlippyDrive and cubeboot can be configured using a configuration file. The configuration file is a simple ini file with sections.

The sections are used to group the configuration options.

Create an text file on the root of your microSD card called ``config.ini``. The file should look similar to the example in the following section. Note that the settings file **must** include the ``[<name>]`` section headers for the settings to take effect.

Some options are optional. If so, they are marked with a ``#`` in front of them, remove ``#`` and one space to enable them.

This document explains the various configuration options available in the ``config.ini`` file.

Example Configuration file
==========================

:download:`Download <_static/config.ini>`

.. literalinclude:: _static/config.ini
   :language: ini


Configuration File Format
=========================

[flippydrive]
-------------

Settings under this section control the general boot behavior of the FlippyDrive.

.. confval:: boot_mode
   :type: string
   :default: normal

   Sets the default boot mode.

   Values:

   * ``normal``: Boots according to the standard FlippyDrive sequence.
   * ``bypass``: Always boots directly from the disc drive. Boot to the bootloader (:kbd:`X`) if you want to use cubeboot, swiss, etc.

[cubeboot]
----------

This section contains settings specific to cubeboot functionality.

.. confval:: cube_color
   :type: string (RGB hex)
   :default: (commented out)

   Customizes the color of the GameCube logo displayed during boot.

   Values:

   * **Commented out**: If this line is commented out (or not present), the original logo color will be used.
   * ``random``: Displays a random color for the GameCube logo each time you boot.
   * **RGB hex color**: Enter a 6-digit hexadecimal color code (similar to websafe colors) to set a specific color. For example, ``660089`` would set a particular shade of purple.

.. confval:: force_swiss_default
   :type: integer
   :default: 0

   When set to ``1``, all games will automatically boot through Swiss.
   Values:

   * ``0`` Off
   * ``1`` On

.. confval:: force_progressive
   :type: integer
   :default: 0

   When set to ``1``, forces progressive scan mode within the IPL (GameCube menu).
   .. attention:: Doesn't work in IPL NTSC-U 1.0. Also causes graphical issues in games when running PAL IPL 1.0 if not forcing games to boot through Swiss (``force_swiss_default = 1``)

   Values:

   * ``0`` Off
   * ``1`` On

.. confval:: disable_mcp_select
   :type: integer
   :default: 0

   When set to ``1``, disables support for MemCard PRO GC.

   Values:

   * ``0`` Off (MemCard Pro GC enabled)
   * ``1`` On (MemCard Pro GC disabled)

.. confval:: preboot_delay_ms
   :type: integer
   :default: 0 (milliseconds)

   .. versionchanged:: 1.5.0

   .. warning::
     ``preboot_delay_ms`` existed before version 1.5.0 but did not function at all. It is advised not to use it on lower versions as it could cause other issues such as being unable to boot certain titles.


   Sets a delay, in milliseconds, used for waiting for GCVideo to initialize before proceeding with the boot process.

.. confval:: postboot_delay_ms
   :type: integer
   :default: (commented out)

   Sets a delay, in milliseconds, after the boot logo appears. This can be used
   to mimic the typical disc loading times you would experience with a physical
   game disc. This line is commented out by default.

---

[network]
---------

This section configures network features. Please note that all network
features require a server running the FlippyDrive application to be set and
active, however, if a cable is plugged in, it will connect to your local network regardless of network setting.
Wi-Fi connections also necessitate providing both an SSID and password.

.. confval:: is_default
   :type: integer
   :default: 0

   When set to ``1``, the network interface is set as the default disc device.
   CubeBoot can utilize other network features regardless of this setting.

   Values:

   * ``0`` - Off - Games will be read from SD
   * ``1`` - On - Games will be read from network first

.. confval:: server
   :type: string (IPv4 or IPv6 address)
   :default: 198.51.100.1

   The IP address of your FlippyDrive server. This can be either an IPv4 or
   IPv6 address. The default port for the server is ``7031``.

.. confval:: ssid
   :type: string

   The SSID (network name) of your 2.4 GHz Wi-Fi network.

.. confval:: password
   :type: string

   The network key (password) for your Wi-Fi network.

Experimental Options
--------------------

The following options are still under development. Use them at your own discretion.

[cubeboot]
^^^^^^^^^^
.. confval:: enable_experimental_png
   :type: integer
   :default: 0 (commented out)

   .. versionadded:: 1.4.3

   When set to ``1``, this enables folder icons and game icons in the interface.
   Be aware that this feature is still experimental and might have bugs.

   Place PNG files with the same filename as the folder or game file, e.g. ``tux.png`` for ``tux.iso`` or ``misc.png`` for a folder called 'misc'

   Values:

   - ``0``: Disabled
   - ``1``: Enabled

.. confval:: cube_logo
   :type: string (filename)
   :default: (commented out)

   .. versionadded:: 1.4.5

   This enables the custom Cube logo feature, which replaces the word 'GAMECUBE' on
   the boot animation with a custom image. Specify the filename of your desired logo image.
   PNG dimensions must be 352x40 and can be generated `here <https://trevor.la/logo>`_.

   Values:

   - A valid PNG filename


