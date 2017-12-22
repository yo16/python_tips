# coding: utf-8

# 画面のキャプチャを撮る
# 2017 (c) yo16

import pyautogui

# どちらでもいい
# 戻り値は
# Image object (see the Pillow or PIL module documentation for details)

# 方法１
#image_object = pyautogui.screenshot('screenshot.png')

# 方法２
image_object = pyautogui.screenshot()
image_object.save('screenshot.png')
