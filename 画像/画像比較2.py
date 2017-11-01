# -*- coding:utf-8 -*-

# 画像ファイルの中で
# 真っ白でない部分を比較する
# 2016/12/16 y.ikeda

from PIL import Image


# ファイル1
file1 = './img/nums/1-1.png'

# ファイル2
file2 = './img/nums/1-2.png'


def main():
	# RECTを取得
	rect1 = getRect(file1)
	rect2 = getRect(file2)
	
	img1 = Image.open(file1)
	img1 = img1.convert('RGB')
	img2 = Image.open(file2)
	img2 = img2.convert('RGB')
	
	# 1dotずつ比較（ファイル１ベース）
	dotNum = 0		# 比較した数
	sameDotNum = 0	# 同じだったdotの数
	for x in range( rect1['width'] ):
		for y in range( rect1['height'] ):
			isSame = 0
			
			if ( rect2['x']+x < img2.size[0] ) and ( rect2['y']+y < img2.size[1] ):
				r1, g1, b1 = img1.getpixel((rect1['x']+x, rect1['y']+y))
				r2, g2, b2 = img2.getpixel((rect2['x']+x, rect2['y']+y))
				if (r1==r2) and (g1==g2) and (b1==b2):
					isSame = 1
			
			dotNum += 1
			sameDotNum += isSame
	
	img1.close()
	img2.close()
	
	print('same pixel = %d/%d'% (sameDotNum, dotNum))


# ファイルの真っ白でない部分のRECTを取得する
def getRect(fileName):
	img = Image.open(fileName)
	img = img.convert('RGB')
	
	minx = img.size[0]
	miny = img.size[1]
	maxx = 0
	maxy = 0
	
	for x in range( img.size[0] ):
		for y in range( img.size[1] ):
			r,g,b = img.getpixel((x,y))
			if( r+g+b < 255*3 ):
				if(x < minx):
					minx = x
				if(y < miny):
					miny = y
				if(maxx < x):
					maxx = x
				if(maxy < y):
					maxy = y
	
	img.close()
	
	return {'x':minx, 'y':miny, 'width':(maxx-minx), 'height':(maxy-miny)}


if __name__ == '__main__':
	main()
	