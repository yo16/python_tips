# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageGrab
from PIL import ImageOps

# 画面をキャプチャ
img = ImageGrab.grab((0,0,500,500))
# グレースケールに変換
gray_img = ImageOps.grayscale(img)

gray_img.show()
