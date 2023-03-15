import logging
import time
import numpy as np

from mss import mss
from mss.models import Size
from PIL import Image

swidth = 1920
sheight = 1080
resize_base = 540
force_resize = False
current_screen = True
dimension_screen = {'top': 150, 'left': 100, 'width': 1820, 'height': 930}

def test_image_resize():
    """Test image processing performance."""
    fps = []
    taken_time = []

    with mss() as sct:

        ratio = swidth / sheight
        resize_ratio = int(resize_base // ratio)

        monitor = dimension_screen

        if current_screen:
            monitor = sct.monitors[0]

        for i in range(100):

            print("test " + str(i + 1) + "/100", end="\r" if i < 99 else "\n")

            # grab image, resize it and save it
            img = sct.grab(monitor)
            # update last_time at right place
            last_time = time.time()

            if force_resize:
                img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
                img = img.resize((resize_base, resize_ratio))
            else:
                img = Image.frombytes("RGB", Size(width=resize_base, height=resize_ratio), img.bgra, "raw",
                                      "BGRX")

            img.save("../tests/tmp_tests.jpeg", "JPEG")

            taken_time.append(time.time() - last_time)
            # fps calculation
            # fps.append(1 / (time.time() - last_time))

    # fps = np.array(fps)
    #print(np.median(fps))
    taken_time = np.array(taken_time)
    taken_time = np.median(taken_time)*1000
    logging.info("Median time : {:.2f}".format(np.median(a=taken_time))) # 15ms
    time.sleep(5)


def test_image_magick_resize():
    """Test image processing performance."""
    fps = []
    taken_time = []

    with mss() as sct:

        ratio = swidth / sheight
        resize_ratio = int(resize_base // ratio)

        monitor = dimension_screen

        if current_screen:
            monitor = sct.monitors[0]

        for i in range(100):

            print("test " + str(i + 1) + "/100", end="\r" if i < 99 else "\n")

            # grab image, resize it and save it
            last_time = time.time()
            img = sct.grab(monitor)

            if force_resize:
                img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
                img = img.resize((resize_base, resize_ratio))
            else:
                img = Image.frombytes("RGB", Size(width=resize_base, height=resize_ratio), img.bgra, "raw",
                                      "BGRX")

            img.save("tests/tmp_tests.jpeg", "JPEG")

            taken_time.append(time.time() - last_time)
            # fps calculation
            fps.append(1 / (time.time() - last_time))

    fps = np.array(fps)
    median_fps = np.median(a=fps)
    logging.info("Median fps : {:.2f}".format(np.median(a=fps)))
    taken_time = np.array(taken_time)
    logging.info("Median time : {:.2f}".format(np.median(a=taken_time)))

test_image_resize()