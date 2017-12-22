# coding: utf-8

# 画像をみつけてクリック
# 2017 (c) yo16

import pyautogui
import time

imagePath = './image/calc_button_7.png'



# 非同期で起動したcalcがまだ起動しきってないかもしれないので
# 念のため少し待つ
time.sleep(1)

# calcの7のボタンを探す
location = pyautogui.locateOnScreen(imagePath)
if location != None:
	print('FOUND!!')
	
	# 画像の中心位置を取得
	x, y = pyautogui.center(location)
	
	# クリック
	pyautogui.click(x, y)
	
	print('Clicked at (x:{0}, y:{1})'.format(x,y))
	
else:
	print('not found...')

