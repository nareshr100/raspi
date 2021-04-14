#!/usr/bin/env python3

import board
import busio
import adafruit_ahtx0

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)