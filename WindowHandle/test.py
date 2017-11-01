# -*- coding: utf-8 -*-

import windowhandleenumerator
import windowtext
import ctypes

if __name__ == "__main__":
	f = open(u'test_結果.txt', 'w')
	
	handles = windowhandleenumerator.enum_top_level_windows()
	for handle in handles:
		if ctypes.windll.user32.IsWindowVisible(handle):
			print(" ({handle:0>8X})".format(handle=handle))
			# textのunicode型をstr型へ変換
			text1 = windowtext.get_window_text_w(handle).encode('utf_8')
			
			# print
			print("\"{text}\" ({handle:0>8X})".format(
				handle=handle,
				text=text1))
			
			# ファイル出力
			f.write("\"{text}\" ({handle:0>8X})\n".format(
				handle=handle,
				text=text1))
	
	f.close()
