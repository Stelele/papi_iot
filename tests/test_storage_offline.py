#!/usr/bin/env python

"""Tests for `papi_iot` package."""

import pytest
import sys
import fake_rpi
from os import path

sys.modules['picamera'] = fake_rpi.picamera
from papi_iot.papi_storage_offline import OfflineStorage


def photo_dir_creation():
    offline = OfflineStorage()

    offline.setOfflinePhotoStorageLocation()

    assert path.isdir(offline.getOfflinePhotoStorageLocation('knownFaces')) == True
    assert path.isdir(offline.getOfflinePhotoStorageLocation('unkownFaces')) == True

def video_dir_creation():
    offline = OfflineStorage()

    offline.setOfflineVideoStorageLocation()

    assert path.isdir(offline.getOfflineVideoStorageLocation())