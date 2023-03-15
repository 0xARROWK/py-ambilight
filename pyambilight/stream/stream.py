#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# v0.5.0

# run with : nice -n 19 python3 stream.py

# TODO :  bluetooth connection module, arduino support, led synchronization with wallpaper, multiscreen support ?
import logging
import time
import cv2
import numpy as np
import pygatt
import colorsys
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
#from apscheduler.schedulers.blocking import BlockingScheduler
from mss import mss
from mss.models import Size
from PIL import Image
from PIL import ImageColor
from ..config import *
from ..const import *
from ..utils import palette, get_colorscheme, get_brightest_color, rgb_to_hex


#try:
#led = Led("BE:FF:20:00:FE:37", "fff0", "0000fff3-0000-1000-8000-00805f9b34fb")
#except:
#    pass
# adapter = pygatt.GATTToolBackend()
# adapter.start()

led = None

# device = adapter.connect("BE:FF:20:00:FE:37", 15)
seconds_interval = 0.1
minutes_interval = 0
hours_interval = 0


async def start():
    """Stream desktop screen and process with image."""
    fps = []

    # adapter = pygatt.GATTToolBackend()
    # adapter.start()

    # device = adapter.connect(mac, 15)

    with mss() as sct:

        ratio = swidth / sheight
        resize_ratio = int(resize_base // ratio)

        monitor = dimension_screen
        if current_screen:
            monitor = sct.monitors[0]

        while True:

            # grab image, resize it and save it
            last_time = time.time()
            img = sct.grab(monitor)

            if force_resize:
                img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
                img = img.resize((resize_base, resize_ratio))
            else:
                img = Image.frombytes("RGB", Size(width=resize_base, height=resize_ratio), img.bgra, "raw", "BGRX")

            img.save("tmp.jpeg", "JPEG")

            # get three current dominant color and convert them from hex to rgb
            rgb = get_colorscheme("tmp.jpeg")
            for i in range(len(rgb)):
                rgb[i] = ImageColor.getcolor(rgb[i], "RGB")

            # get color from lightest and send it to leds
            rgb, hexa = get_brightest_color(rgb)
            #hexa = rgb_to_hex(rgb[0])
            print(rgb)
            palette([rgb], background=True)

            # h, l, s = colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2])
            # led.set_brightness(s)
            await led.set_color(hexa)
            # hexa = hexa[1:]
            # out = [(hexa[i:i + 2]) for i in range(0, len(hexa), 2)]

            # device.char_write("0000fff3-0000-1000-8000-00805f9b34fb",
            #                   [0x7e, 0x00, 0x05, 0x03, int("0x" + out[0], 16), int("0x" + out[1], 16),
            #                    int("0x" + out[2], 16), 0x00, 0xef], wait_for_response=False)

            # fps calculation and exit
            taken_time = time.time() - last_time
            print("{:.2f}".format(1 / taken_time) + " fps", end='\r')
            fps.append(1 / taken_time)

            # if taken_time < seconds_interval:
            #    time.sleep(seconds_interval - taken_time)
            time.sleep(seconds_interval)


async def stream():
    global led
    if OS == 'Linux':
        from ..ble_led_linux import LinuxLed
        led = LinuxLed("BE:FF:20:00:FE:37", "fff0", "0000fff3-0000-1000-8000-00805f9b34fb")
    elif OS == 'Windows':
        from ..ble_led_windows import WindowsLED
        led = WindowsLED("BE:FF:20:00:FE:37", "fff0", "0000fff3-0000-1000-8000-00805f9b34fb")
        await led.connect()
    
    await start()
    #scheduler = AsyncIOScheduler()
    #scheduler.add_job(start, 'interval', seconds=seconds_interval, minutes=minutes_interval, hours=hours_interval)
    #scheduler.start()
    #asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    stream()
