# -*- coding: utf-8 -*-

import pyautogui
import time
import ctypes
import windowhandleenumerator
import windowtext
import math


def getPaintWH():
	handles = windowhandleenumerator.enum_top_level_windows()
	for handle in handles:
		if ctypes.windll.user32.IsWindowVisible(handle):
			text1 = windowtext.get_window_text_w(handle)
			if text1 == u'無題 - ペイント':
				return handle
	return 0


# ペイント起動
pyautogui.keyDown('win')
pyautogui.typewrite('r')
pyautogui.keyUp('win')
time.sleep(0.1)
pyautogui.typewrite('mspaint\n')
time.sleep(1)

# ハンドル取得
hwnd = getPaintWH()
if hwnd == 0:
	raise WindowsError()

# ウィンドウサイズを変更
ctypes.windll.user32.SetWindowPos(hwnd, None, 100, 100, 800, 600, 0)

# Ctrl+Wでサイズ変更
pyautogui.keyDown('ctrl')
pyautogui.typewrite('w')
pyautogui.keyUp('ctrl')
time.sleep(0.5)

# ピクセル単位をピクセルへ
pyautogui.keyDown('right')

# 縦横比を維持しない
pyautogui.keyDown('alt')
pyautogui.typewrite('m')
pyautogui.keyUp('alt')

# 水平方向=500
pyautogui.keyDown('alt')
pyautogui.typewrite('h')
pyautogui.keyUp('alt')
pyautogui.typewrite('500')

# 垂直方向=400
pyautogui.keyDown('alt')
pyautogui.typewrite('v')
pyautogui.keyUp('alt')
pyautogui.typewrite('400\n')


# スピログラフを描く
center = [350,480]
pyautogui.click(center[0], center[1])

# 設定
r1 = 160
r2 = 97
delta1_do = 5	# r1の回転角速度(度)
# 外の回転数(周)
rot = 5

# 描画
# r1の角速度(radian)
delta1 = (delta1_do / 180.0)*math.pi
# r2の角速度(radian)
delta2 = delta1 * r1 / r2

# 初期位置 r1=[1,0]方向
curTheta1 = 0
curTheta2 = 0
pyautogui.moveTo(center[0]+r1, center[1])

rotend = int(math.floor(360*rot))
for t1 in range(0, rotend, delta1_do):
	curTheta1 += delta1
	curTheta2 += delta2
	nextpos = [
		center[0]+(r1-r2)*math.cos(curTheta1)+r2*math.cos(curTheta2),
		center[1]+(r1-r2)*math.sin(curTheta1)+r2*math.sin(curTheta2)
		]
	pyautogui.dragTo(nextpos[0], nextpos[1],0)
	
