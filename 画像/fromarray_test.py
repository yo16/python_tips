#coding: UTF-8

import numpy as np
from PIL import Image


# ary[列][行][0]:R
# ary[列][行][1]:G
# ary[列][行][2]:B
ary = np.array([
	[[255,0,0],[0,255,0]],
	[[0,0,255],[255,255,255]]
])

img = Image.fromarray(np.uint8(ary))

with open("fromarray_test.png", mode="wb") as out:
	img.save(out, format="png")
	
