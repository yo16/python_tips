# -*- coding:utf-8 -*-

# 画像ファイルを、単純に端から端までrgbのpixelを比較する
# 2016/12/16 yo16

from PIL import Image


# ファイル1
file1 = './img/nums/1-1.png'

# ファイル2
file2 = './img/nums/2-1.png'


if __name__ == '__main__':
	# ファイル1を開く
	img1 = Image.open(file1)
	img1 = img1.convert('RGB')
	
	# ファイル2を開く
	img2 = Image.open(file2)
	img2 = img2.convert('RGB')
	
	# 1dotずつ比較（ファイル１ベース）
	dotNum = 0		# 比較した数
	sameDotNum = 0	# 同じだったdotの数
	for x in range( img1.size[0] ):
		for y in range( img1.size[1] ):
			isSame = 0
			if ( x < img2.size[0] ) and ( y < img2.size[1] ):
				r1, g1, b1 = img1.getpixel((x, y))
				r2, g2, b2 = img2.getpixel((x, y))
				if (r1==r2) and (g1==g2) and (b1==b2):
					isSame = 1
			
			dotNum += 1
			sameDotNum += isSame
	
	print('same pixel = %d/%d'% (sameDotNum, dotNum))
	