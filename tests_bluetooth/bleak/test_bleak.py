import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())

# https://www.youtube.com/watch?v=MQugcNLFI9k
# https://www.youtube.com/watch?v=NaWIBRvSWE8
# https://www.youtube.com/watch?v=sDCb6Sus3T8
# https://www.youtube.com/watch?v=Puw6A3d0wbE
# https://www.youtube.com/watch?v=aHUrAvKNF8s
# https://www.youtube.com/watch?v=bV7VJikaTQs
# https://www.youtube.com/watch?v=KD_XesvG7AM