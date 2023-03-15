import asyncio
import argparse

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from ble_led_windows import WindowsLED

led = None

# device = adapter.connect("BE:FF:20:00:FE:37", 15)
seconds_interval = 0.1
minutes_interval = 0
hours_interval = 0


async def start():
    """Stream desktop screen and process with image."""
    # ...
    await led.set_color("#FF00FF")
    # ...
    # print("send data...")


async def stream():
    global led
    led = WindowsLED("BE:FF:20:00:FE:37", "fff0", "0000fff3-0000-1000-8000-00805f9b34fb")
    await led.connect()
    
    await start()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(start, 'interval', seconds=seconds_interval, minutes=minutes_interval, hours=hours_interval)
    scheduler.start()
    asyncio.get_event_loop().run_forever()
