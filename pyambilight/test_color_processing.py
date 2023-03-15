import logging
import time
import numpy as np

from mss import mss
from mss.models import Size
from PIL import Image, ImageColor

import scipy.cluster
import sklearn.cluster
import os

from utils import get_colorscheme, palette, get_brightest_color
from colorthief import ColorThief

swidth = 1920
sheight = 1080
resize_base = 200
force_resize = False
current_screen = True
dimension_screen = {'top': 150, 'left': 100, 'width': 1820, 'height': 930}


# WARNING : average color vs dominant color is not the same. Dominant color will be far accurate than average
# which just do a mean of all rgb colors contained in the image.


# most opttimized with resize enabled + resize base set to 200
def use_colorthief():
    ct_image = ColorThief("tests/tmp_tests.jpeg")
    color = ct_image.get_color(quality=100)
    return [color]


# most optimized with resize enabled + resize base set to 50
def schemer2():
    dominant_colors = get_colorscheme("tests/tmp_tests.jpeg")
    for i in range(len(dominant_colors)):
        dominant_colors[i] = ImageColor.getcolor(dominant_colors[i], "RGB")
    return get_brightest_color(dominant_colors)
    #return [dominant_colors[0]]


def pillow_getcolors(image):
    #Get colors from image object
    width, height = image.size
    pixels = image.getcolors(width * height)
    #Sort them by count number(first element of tuple)
    sorted_pixels = sorted(pixels, key=lambda t: t[0])
    #Get the most frequent color
    dominant_color = sorted_pixels[-1][1]
    return [dominant_color]


def compute_average_pixel_by_pixel(img):
    width, height = img.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    return [r_total/count, g_total/count, b_total/count]


def mini_batch_kmeans(image):
    ar = np.asarray(image)
    shape = ar.shape
    ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

    kmeans = sklearn.cluster.MiniBatchKMeans(
        n_clusters=10,
        init="k-means++",
        n_init="auto",
        max_iter=20,
        random_state=1000
    ).fit(ar)
    codes = kmeans.cluster_centers_

    vecs, _dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, _bins = np.histogram(vecs, len(codes))    # count occurrences

    colors = []
    for index in np.argsort(counts)[::-1]:
        colors.append(tuple([int(code) for code in codes[index]]))
    return colors                    # returns colors in order of dominance


def test_color_detection():
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

            # update last_time at right place
            # grab image, resize it and save it
            img = sct.grab(monitor)

            if force_resize:
                img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
                img = img.resize((resize_base, resize_ratio))
            else:
                img = Image.frombytes("RGB", Size(width=resize_base, height=resize_ratio), img.bgra, "raw",
                                      "BGRX")

            img.save("tests/tmp_tests.jpeg", "JPEG")

            last_time = time.time()
            rgb = schemer2()
            # palette(rgb, background=True)
            taken_time.append(time.time() - last_time)
            # fps calculation
            #fps.append(1 / (time.time() - last_time))

    #fps = np.array(fps)
    #print(np.median(fps))
    taken_time = np.array(taken_time)
    taken_time = np.median(a=taken_time)*1000
    print("Median time : {:.2f}".format(np.median(a=taken_time))) # 25-40ms
    time.sleep(5)


if __name__ == "__main__":
    test_color_detection()
    time.sleep(5)