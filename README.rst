========
PAPI IOT
========


.. image:: https://img.shields.io/pypi/v/papi_iot.svg
        :target: https://pypi.python.org/pypi/papi_iot

.. image:: https://img.shields.io/travis/Stelele/papi_iot.svg
        :target: https://travis-ci.com/Stelele/papi_iot

.. image:: https://readthedocs.org/projects/papi-iot/badge/?version=latest
        :target: https://papi-iot.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/Stelele/papi_iot/shield.svg
     :target: https://pyup.io/repos/github/Stelele/papi_iot/
     :alt: Updates

An API for home security system using raspberry Pi with Pi IR camera and facial recognition.

* Github repo: PAPI IOT
* Free software: MIT license
* Documentation: https://papi-iot.readthedocs.io.


Features
--------

* Surveillance Security
* Pi camera live stream 
* Facial recognition 
* Storage Management: SD card memory and Google cloud storage
* Email notifications

Build Status
------------

## Step 1 – Install dLib Library & Face recognition Library

## Step 2 - Clone the papi_iot
Open up terminal and clone the papi_iot repo:

```
bash cd /home/pi
git clone https://github.com/Stelele/papi_iot
```

Quick Start
-----------

## Pre-requisite

* Minimum Raspberry Pi 0 w, 2GB is recommended for optimal Face recognition performance
* [OpenCV face-recognition](https://github.com/ageitgey/face_recognition)
* Raspberry Pi V2 Camera Module 
* Python 3 recommended.

## Start

```bash cd papi_iot
sudo python3 /papi_iot/papi_iot/papi_livestream.py
```

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
