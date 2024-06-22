Configuration Files
===================

The FlippyDrive and cubeboot can be configured using a configuration file. The configuration file is a simple ini file with sections.
    
Configuration File Format
`````````````````````````

The configuration file is a simple ini file with sections. The sections are used to group the configuration options. The configuration file is divided into two sections, the FlippyDrive section and the cubeboot section. The FlippyDrive section is used to configure the FlippyDrive and the cubeboot section is used to configure the cubeboot.


**Example Configuration file:**

.. code-block:: ini

    [cubeboot]

    # Support rgb hex colors aka websafe colors
    cube_color = 660089

    # Enable booting through Swiss for all games
    force_swiss_default = 1

    # Force progressive scan inside the IPL menu
    force_progressive = 1

    # Used for waiting for GCVideo to initialize
    preboot_delay_ms = 0
