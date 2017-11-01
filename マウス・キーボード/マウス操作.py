# -*- coding: utf-8 -*-

import pyautogui

# 現在のマウスの座標位置
currentPos = pyautogui.position()
print currentPos


# マウス移動
# (10,20)の位置に2秒で移動
pyautogui.moveTo(10,20,2)

# 左クリック１回
pyautogui.click(10,20)
# 参考 他のボタン等
#>>> pyautogui.rightClick(x,y)  #右クリック
#>>> pyautogui.middleClick(x,y) #真ん中クリック
#>>> pyautogui.doubleClick(x,y) #ダブルクリック
#>>> pyautogui.tripleClick(x,y) #トリプルクリック


