#!/usr/bin/env python

"""Tests for `papi_iot` package."""

import pytest
import sys
import fake_rpi
from os import path

sys.modules['picamera'] = fake_rpi.picamera
from papi_iot.papi_iot import PAPIIOT

