Configuration Files
===================

The FlippyDrive and cubeboot can be configured using a configuration file. The configuration file is a simple ini file with sections.
    
Configuration File Format
`````````````````````````

The configuration file is a simple ini file with sections. The sections are used to group the configuration options.

Create an text file on the root of your SD card called ``config.ini``. The file should look similar to the example in the following section. Note that the settings file **must** include the ``[<name>]`` section headers for the settings to take effect.


**Example Configuration file:**

.. code-block:: ini

    [flippydrive]
    # Default boot mode, options are "normal" and "bypass"
    # Setting "bypass" will always boot from the disc drive unless X is held down,
    # at which point you can choose cubeboot, swiss, etc.
    boot_mode = normal

    [cubeboot]
    # Cube color - Supports RGB hex colors aka websafe colors
    # comment out/remove the whole line to use the original color
    # Setting "random" shows a random color
    cube_color = 660089

    # Enable booting through Swiss for all games
    force_swiss_default = 0

    # Force progressive scan inside the IPL menu
    force_progressive = 0

    # Disable MemCard PRO GC Support
    disable_mcp_select = 0

    # Used for waiting for GCVideo to initialize
    preboot_delay_ms = 0

    # Delays loading after the boot logo
    # to mimic the load times you would usually experience when booting a disc
    # postboot_delay_ms = 3000

    [network]
    # All network features require a server to be set and running the FlippyDrive app
    # WiFi connections also require a ssid and password

    # Sets the network interface as the default disc device (active is 1)
    # cubeboot can use other network features regardless of setting
    is_default = 0

    # Server IP address, in either IPv4 or IPv6 format. Port is 7031
    server = 198.51.100.1

    # SSID of your network
    ssid = FBIWhiteVan

    # Network key
    password = JEdgarHooverDidNothingWrong
