# coding: utf-8

# マウス位置を取得
# 2017 (c) yo16

import pyautogui as pg

x,y = pg.position()
print('x,y={0},{1}'.format(x,y))



# 連続的に取得

import time
# 実行する時間(s)
checkTime = 5
# 頻度(s)
frequency = 0.1

for i in range(int(checkTime/frequency)):
	time.sleep(frequency)
	x,y = pg.position()
	print('x,y={0},{1}'.format(x,y))

