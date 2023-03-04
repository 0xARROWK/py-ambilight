#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def saturate_colors(colors, amount):
    """Saturate all colors."""
    if amount and float(amount) <= 1.0:
        for i, _ in enumerate(colors):
            if i not in [0, 7, 8, 15]:
                colors[i] = saturate_color(colors[i], float(amount))

    return colors
