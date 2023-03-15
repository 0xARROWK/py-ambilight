import asyncio
import argparse
import nest_asyncio

from test_asyncio import stream

async def parse_args(parser):
    """Process args."""
    args = parser.parse_args()
    if args.run:
        await stream()


def get_args():
    """Get the script arguments."""
    description = "pyambi - synchronises rgb leds with your screen"
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("-r", "--run", action="store_true",
                     help="Run pyambi in default mode (bluetooth). Only bluetooth mode is supported at this moment.")

    return arg


async def main():
    """Main script function."""
    parser = get_args()
    await parse_args(parser)


if __name__ == "__main__":
	nest_asyncio.apply()
	asyncio.run(main())
