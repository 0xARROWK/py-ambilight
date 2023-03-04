#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The mac address of the leds is required to connect to them by bluetooth. To find the mac address, turn on your leds
# and a computer, then open the bluetooth settings. In the list of available devices you can see your leds and get
# their mac address.
led_mac_address = ""


# screen width in pixel
swidth = 1920
# screen height in pixel
sheight = 1080


# Possible values :
# any number as long as resize_base <= screen height in pixel (for FHD screen, recommended between 50 and 540)
#
# High value = lower performance but more accurate colour detection
# Low value = better performance but slightly less accurate colour detection
# After changing this variable, don't forget to test performance by running pyambi with '-t' parameter.
resize_base = 50


# Possible values :
# True, False
#
# If force_resize = True, the image processing time will be doubled, but colours detected will be closer to reality.
# You can always lower 'resize_base' to improve performance and stability of detection
# After changing this variable, don't forget to test performance by running pyambi with '-t' parameter.
force_resize = True


# Possible values :
# False, True
#
# If current_screen = True, the colour detection will be done on the whole screen.
current_screen = True


# Possible values :
# any number as long as top + height <= screen height in pixel and as long as left + width <= screen width in pixel
#
# If current screen = False, the colour detection will be done on the captured image between these coordinates.
dimension_screen = {'top': 150, 'left': 100, 'width': 1820, 'height': 930}
