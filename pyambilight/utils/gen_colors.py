#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

def gen_colors(img):
    """Generate a colorscheme using Colorz."""
    # cmd = ["./lib/bin/schemer2", "-format", "img::colors", "-minBright", "0", "-in"]
    cmd = ["./lib/bin/schemer2", "-format", "img::colors", "-in"]
    colors = subprocess.check_output([*cmd, img]).splitlines()
    return colors
