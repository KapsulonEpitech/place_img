from email.mime import base
from PIL import Image
import numpy as np
base = Image.open("wip.png")
base_pixels = base.load()

img = Image.open("base.png")
img_pixels = img.load()


start = [140, 4396]

def to_extended(x, y):
    return [start[0] + x * 3, start[1] + y * 3]

for x in range(116):
    for y in range(256):
        if base_pixels[x, y] == (0, 0, 0, 0):
            continue
        else:
            one = to_extended(x, y)[0]
            two = to_extended(x, y)[1]
            val = np.asarray(base_pixels[x, y])
            val[-1] = 255
            img_pixels[one, two] = tuple(val)

img.save("out.png")