# coding: utf-8

# 前回のキャプチャとの違いを検出
# 2017 (c) yo16

# このプログラムは、あるタイミングから画面が変わったことを
# 認識することを目的にして作ってみました。

import pyautogui
import time


def main():
	# コマンドプロンプトが立ち上がりきるまで待つ
	time.sleep(0.5)
	
	img1 = pyautogui.screenshot()
	#print(img1.width)
	#print(img1.height)
	
	# 採取する距離(pixel)
	distance = 100
	
	# 一定距離、離れたドット色を格納する配列
	# RGBの2次元配列（3次元配列）
	dots1 = [[ img1.getpixel((w*distance,h*distance)) for h in range(int(img1.height/distance)) ] for w in range(int(img1.width/distance))]
	#print(dots1)
	
	
	
	# 違いが出るまでループ
	changed = False
	while not changed:
		time.sleep(1)
		
		img2 = pyautogui.screenshot()
		dots2 = [[ img2.getpixel((w*distance,h*distance)) for h in range(int(img1.height/distance)) ] for w in range(int(img1.width/distance))]
		
		for h in range(int(img1.height/distance)):
			for w in range(int(img1.width/distance)):
				if dots1[w][h] != dots2[w][h]:
					changed = True
		
		# 本当は、この文字も検出してしまうかもしれないので
		# 出力はあまりよくない
		if changed:
			print('changed!')
		else:
			print('no change.')


if __name__ == '__main__':
	main()


