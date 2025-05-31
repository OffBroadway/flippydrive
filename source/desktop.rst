GUI Application
***************

Install
=======
To use the application, download *flippy_app* from the `FlippyDrive assets GitHub repo <https://github.com/OffBroadway/flippydrive-assets/releases>`_. Look for the latest stable (non-pre-release) release and download the update file. The zip files are for Windows (AMD64), Linux (AMD64) and Mac OS (Darwin). Extract the exe from the zip file with your zip program of choice.

Usage
=====
Server tab
----------

.. image:: /_static/gui_tab_server.png

.. _gui_tab_server:

Game Server
^^^^^^^^^^^

- **Status**: This field displays the status of the server and the IP address and port the server is reachable on. This is the IP address (without the ``:7031`` part) you should enter in the configuration file. If you haven't selected a folder below yet, you should do so first.

Configuration
^^^^^^^^^^^^^

* **Games Path**: This field shows the current directory where the server is looking for files, blank if not (yet) set.

* **Select Folder**: Clicking this button to select a different folder. If you already set one, you will have to power cycle the GameCube before the new folder is detected.


.. _gui_tab_compression:

Compression tab
---------------


.. image:: /_static/gui_tab_compression.png

File Selection
^^^^^^^^^^^^^^

* **Select File**: Click this button to select one file to be compressed.
* **Select Folder**: Click this button to select a folder. All compatible files within that folder will be compressed.

* **Select Output**: Click this button to select a folder where the compressed files will be saved.

* **Start Conversion**: Once you have selected either a file or a folder and configured the desired output folder and compression settings, clicking this button will compress the file(s) to FDI.

Compression Level
^^^^^^^^^^^^^^^^^

This slider controls the level of compression applied to the files.

Having the slider to the left (1) results in faster compression, but size reduction might be reduced.
Having the slider to the right (9) results in the compression process taking longer, but it results in smaller file sizes.


Compression Progress
^^^^^^^^^^^^^^^^^^^^

This section shows the compression progress once it has been started.
After finishing. it will show the compression result.

Advanced Options
^^^^^^^^^^^^^^^^

* **Number of Workers**

  This slider controls the number of CPU cores or threads that compression will utilize during the compression process.
  Increasing the number of workers can potentially significantly speed up the compression time, especially when processing multiple files, as the workload is distributed across multiple CPUs. However, increasing the number of workers will consume more CPU cyles.

* **Enable Dictionary Generation (30 seconds per-file)**

  Checking this box will enable a dictionary generation step for each input file before compression. This process may take an additional 30 seconds per file. Dictionary generation can sometimes lead to better compression ratios, especially for files with repetitive data patterns.

* **Enable High Compression Levels (not recommended)**

  .. caution:: While this may result in even smaller file sizes, it is **not recommended** as, depending on the file you compress, will **likely** cause compatibility issues, causing files to fail to boot on the GameCube. Use this option with caution and at your own risk.
  Checking this box will enable the use of potentially higher compression levels.

* **Save Intermediate NKit Files**

  Checking this box will cause any intermediate NKit files (``.nkit.iso``) that are generated during the compression process to be kept, otherwise they will be deleted.
