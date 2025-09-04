Headless Server
***************


Install
=======
To use the application, download *flippy_cli* from the `FlippyDrive assets GitHub repo <https://github.com/OffBroadway/flippydrive-assets/releases>`_. Look for the latest stable (non-pre-release) release and download the update file. The zip files are for Windows (AMD64), Linux (AMD64) and Mac OS (Darwin). Extract the exe from the zip file with your zip program of choice.


Usage
=====

.. todo:: Documentation is still work-in-progress


Docker Compose file
===================

If you want to use docker compose, you can use the ``compose.yaml`` file provided below:
(update the version number manually if there's a new version)

.. code-block:: yaml

    services:
      flippydrive-server:
        image: offbroadway/flippydrive-server:v1.4.2
        volumes:
          # Mount the data folder in the current directory to /data inside of the container
          - ./data:/data
        ports:
          - "7031:7031"