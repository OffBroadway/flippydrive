Remote Access
**************
.. versionadded:: 1.4.5

Make sure the FlippyDrive application is open on your computer before turning on your GameCube.

#. Hold :kbd:`X` to get to the FlippyDrive bootloader
#. Select ``Boot Onboard DOL``
#. Select ``remote``.

This app will start the FTP/SMB connection. You can then use your favorite client to connect to the IP address of the computer running the FlippyDrive application and port `7021`.

Make sure that you recognize the IP address and that the FlippyDrive application isn't binding to a different network adapter on your computer.

You can use any FTP client of choice. For ease of use, we recommend FileZilla or any other well-known client.

1. Download an install FileZilla and open it
2. Go to File > Site Manager
3. Click 'New site' and name it 'FlippyDrive' or something else.
4. In the panel to the right, set the following options:

**General tab**:

- Protocol: "FTP - File Transfer Protocol"
- Host: "127.0.0.1"
- Port: "7021"
- Encryption: "Only use plain FTP (insecure) ⚠"
- Logon Type: "Normal"
- User: "anonymous"
- Password: leave empty

**Advanced tab:**  Leave as-is

**"Transfer Settings" tab:**

- Transfer mode: Default
- "Limit number of simultaneous connections": ✅
- "Maximum number of connections": 1

**"Charset" tab:** Leave as-is (Autodetect)


.. todo:: Add screenshots

.. warning:: In beta versions 1.4.5 and 1.4.6, creating folder on the microSD is broken.