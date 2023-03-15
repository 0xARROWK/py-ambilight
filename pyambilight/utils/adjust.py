#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .generic_adjust import generic_adjust
from .color_tools import rgb_to_yiq


def adjust(cols, light):
    """Create palette."""
    # TODO: fix alt + tab bug
    res = ['#000000'] * 16

    if 'Could not get colors from image with settings specified. Aborting.' in cols[0]:
        res = ['#ffffff'] * 16
    else:
        try:
            cols.sort(key=rgb_to_yiq)
            raw_colors = [*cols[8:], *cols[8:]]
            res = generic_adjust(raw_colors, light)
        except:
            pass

    return res
