Headless Server
***************

.. todo:: These documentations are still work-in-progress

Install
=======

Usage
=====

Docker Compose file
======

If you want to use docker compose, you can use the ``compose.yaml`` file provided below:
(update the version number manually if there's a new version)

.. code-block:: yaml

    services:
      flippydrive-server:
        image: offbroadway/flippydrive-server:v1.5.0
        volumes:
          # Mount the data folder in the current directory to /data inside of the container
          - ./data:/data
        ports:
          - "7031:7031"