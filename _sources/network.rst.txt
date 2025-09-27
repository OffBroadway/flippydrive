Networking
**********

General Parameters
``````````````````

By default, the FlippyDrive uses the following network parameters:

- Addressing: Dynamic, DHCP4 (SLAAC in test)
- Protocol: TCP
- Port: 7031, 7021 (Remote Access, v1.4.5 and newer)

.. toctree::
    :hidden:

    wifi
    ethernet
    server
    desktop
    remote-access

The FlippyDrive has onboard Wi-Fi for management, updates, and experimental support for loading games live. All of this is accomplished with the FlippyDrive application.

Take a look at the :doc:`configuration file<configuration>` entries, :doc:`server<server>`, and/or :doc:`desktop app<desktop>` required to use network features.

Gameplay Network Requirements
`````````````````````````````

Playing games live over the network is very network intensive and desktop/server dependent. As such, live loading of disc images is experimental and will likely remain that way forever as results cannot be guaranteed under many conditions.

The GameCube disc interface is a simple command/response style, so any network delays in responding to requests can cause significant performance problems. In general, your network must meet the following requirements:

- <5ms ping between desktop/server and FlippyDrive
- Ability to maintain MCS4 data rates (39 Mbit/s) with FlippyDrive
- No significant interference/SNR drops
- For multi-AP WI-Fi setups: Ability to bond FlippyDrive to the nearest AP as it may select a sub-optimal distant AP BSSID

.. note::
    The upcoming on-cube Wi-Fi configuration app will include a speed and latency test to indicate if your network likely supports these performance requirements.
