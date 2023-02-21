#! /usr/bin/env python3

import sys, colorsys, random, string

def rgb(r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m"

i = random.randint(0, 360)

try:
    for line in sys.stdin:
        for char in line:
            if char not in "!@#$%^&*()_+-=\"':;[]{}\\|,./<>?~` "+string.ascii_letters:
                print(char, end='')
                continue
            if char == "[":
                print("\x1b[0;0H", end='')
            colour = colorsys.hsv_to_rgb(i/360, 1, 1)
            colour = [int(x * 255) for x in colour]
            print(rgb(colour[0], colour[1], colour[2])+char, end='')
            i += 0.5
            i = i % 360
except KeyboardInterrupt:
    print("\x1b[0m")

print("\x1b[0m")
