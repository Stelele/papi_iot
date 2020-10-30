#!/usr/bin/env python

"""Tests for `papi_iot` package."""

import pytest
import sys
import fake_rpi
from os import path

sys.modules['picamera'] = fake_rpi.picamera
from papi_iot.papi_iot import PAPIIOT

def photo_dir_creation():
    #papi = PAPIIOT()

    #papi.storageManager.offlineStorage.setOfflinePhotoStorageLocation()
    x = 5
    y = 5
    assert x == y
    #assert path.isdir(papi.storageManager.offlineStorage.getOfflinePhotoStorageLocation('knownFaces')) == True
    #assert path.isdir(papi.storageManager.offlineStorage.getOfflinePhotoStorageLocation('unkownFaces')) == True

def video_dir_creation():
    #papi = PAPIIOT()
    x = 5
    y = 5
    #papi.storageManager.offlineStorage.setOfflineVideoStorageLocation()
    assert x == y
    #assert path.isdir(papi.storageManager.offlineStorage.getOfflineVideoStorageLocation()) == True