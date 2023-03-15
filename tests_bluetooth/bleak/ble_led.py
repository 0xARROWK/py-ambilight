#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : ble_led
# Author             : Noewen
# Date created       : 20/02/2021
# Date last modified : 10/09/2021
# Python Version     : 3.*

import asyncio
import time
from bleak import BleakClient


# Brightness in percent (0-100)
def brightness(percent):
    return [0x7e, 0x00, 0x01, percent, 0x00, 0x00, 0x00, 0x00, 0xef]


# Color in hexadecimal format (ex: #FF00FF)
def color(hexa):
    hexa = hexa[1:]
    return [0x7e, 0x07, 0x05, 0x03, int(hexa[0:2], 16), int(hexa[2:4], 16), int(hexa[4:6], 16), 0x00, 0xef]


class WindowsLED:
    currentColor = '#FF00FF'
    currentBrightness = 100

    def __init__(self, address, uuid, characteristic):
        self.uuid = uuid
        self.address = address
        self.characteristic = characteristic
        self.device = None


    async def connect(self):
        print("waiting for connection...")
        client = BleakClient(self.address)
        await client.connect()
        print(f"Connected : {client.is_connected}")
        #paired = await client.pair(protection_level=3)
        #print(f"Paired : {paired}")
        self.device = client
        await self.set_brightness(self.currentBrightness)
        await self.set_color(self.currentColor)


    # Set brightness intensity in percent
    async def set_brightness(self, b):
        self.currentBrightness = b
        await self.device.write_gatt_char(self.characteristic, bytearray(brightness(b)))


    # Set color in hexadecimal format (ex: #FF00FF)
    async def set_color(self, c):
        self.currentColor = c
        await self.device.write_gatt_char(self.characteristic, bytearray(color(c)))


    def stop(self):
        self.device.disconnect()


async def main():
    led = WindowsLED("BE:FF:20:00:FE:37", "fff0", "0000fff3-0000-1000-8000-00805f9b34fb")
    await led.connect()
    last_time = time.time()
    for i in range(10):
        await led.set_color("#FF0000" if i%2 == 0 else "#00FF00")
        time.sleep(0.1)
    print((time.time() - last_time) * 1000)


asyncio.run(main())