# -*- coding: utf-8 -*-

import pyautogui
import time

# キーリスト表示
print pyautogui.KEYBOARD_KEYS


# --- notepad ---

pyautogui.keyDown('win')
pyautogui.typewrite('r')
pyautogui.keyUp('win')
pyautogui.typewrite('notepad\n')
time.sleep(1)	# 1秒スリープ
pyautogui.typewrite('123')



# --- alt+tab ---

# altをキーダウン
pyautogui.keyDown('alt', 0.1)
# tab
pyautogui.typewrite(['tab'], 0.1)	# ファンクションキーは、配列渡し
# altをキーアップ
pyautogui.keyUp('alt', 0.1)



# 
