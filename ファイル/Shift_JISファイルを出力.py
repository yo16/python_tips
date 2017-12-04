# -*- coding: utf-8 -*-

# Shift_JISファイルを出力

import codecs


f = codecs.open('shift_jis.txt', mode='w', encoding='shift_jis')

f.write('日本語１２３')

#f.write('－')	# ←この文字はできない！（未解決）

f.close()
