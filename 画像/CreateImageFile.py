# -*- coding:utf-8 -*-

# 画像ファイルを作成する
# 2016/3/16 yo16

from PIL import Image
from PIL import ImageDraw

def make_image(screen, bgcolor, filename):
	img = Image.new('RGB', screen, bgcolor)
	
	# マークを描く
	#dr = ImageDraw.Draw( img )
	#dr.rectangle(((100,100), (200,200)), fill=(0,0,255))
	px = [[0,0,0,0,0,0,0,0,0,0], \
	      [0,0,0,0,0,0,0,0,1,0], \
	      [0,0,0,0,0,0,1,1,1,0], \
	      [0,0,0,0,1,1,1,1,1,0], \
	      [0,0,1,1,1,1,1,1,1,0], \
	      [0,1,1,1,1,1,1,1,1,0], \
	      [0,1,1,1,1,1,1,1,1,0], \
	      [0,1,1,1,1,1,1,1,1,0], \
	      [0,0,0,0,0,0,0,0,0,0], \
	      [0,0,0,0,0,0,0,0,0,0]]
	for i in range(len(px)):
		for j in range(len(px[i])):
			col = (0,0,0,0)
			if (px[i][j] == 1):
				col = (255,255,255,0)
			img.putpixel((j,i), col)
	
	img.save(filename)
	return


if __name__ == '__main__':
	# 画像のサイズ
	screen = (10, 10)
	
	# 背景色
	bgcolor = (0xdd, 0xdd, 0xdd)
	
	# ファイル名
	filename = ".\img\CreateImageFile.png"
	
	make_image(screen, bgcolor, filename)

