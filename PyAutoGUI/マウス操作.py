# -*- coding: utf-8 -*-

import sys
import pyautogui

print u'マウス位置'.encode('shift-jis')
print pyautogui.position()

print u'解像度'.encode('shift-jis')
print pyautogui.size()



print u'マウスカーソルを移動'.encode('shift-jis')
# pyautogui.moveTo(x, y, time)  # マウスカーソルを (x,y)の座標までtime秒で移動する．もしtime=0であればすぐに移動する．
# pyautogui.moveRel(xOffset, yOffset, time)  #現在のマウスカーソルの座標から(xOffset,yOffset)だけtime秒で移動する．
pyautogui.moveTo(150,1050,2)

# ダブルクリック
# pyautogui.click(x, y, clicks, interval, button)
#pyautogui.click(10,10,2, 0.1, 'left')

# 下記でも同様
# pyautogui.doubleClick(10,10)



print u'Shiftキーを押す'.encode('shift-jis')
pyautogui.keyDown('shift')

# 左クリック
pyautogui.click(150,1050)

print u'Shiftキーを離す'.encode('shift-jis')
pyautogui.keyUp('shift')

