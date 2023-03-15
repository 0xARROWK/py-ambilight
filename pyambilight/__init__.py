#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .const import *
if OS == 'Linux':
	from .ble_led_linux import *
elif OS == 'Windows':
	from .ble_led_windows import *
from .config import *
from .dependencies import *
from .stream import *
from .utils import *
from .tests import *
from .web import *
