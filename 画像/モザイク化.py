# -*- coding:utf-8 -*-

# 画像ファイルをモザイク化する
# 2016/12/14 y.ikeda

from PIL import Image
from PIL import ImageDraw




# 入力ファイル
#inFile = 'tmp1.png'
inFile = './img/1_1_pil_01.jpg'

# 出力ファイル
#outFile = 'tmp1_moz.png'
outFile = './img/1_1_pil_01_moz.png'

# 分割数
devNum = 20



if __name__ == '__main__':
	# 入力ファイルの情報を収集
	imgIn = Image.open(inFile)
	imgIn = imgIn.convert('RGB')
	# 画像サイズは、inImg.size（[0]幅、[1]高さ）
	# モザイクサイズ
	mozSize = [int(imgIn.size[0]/devNum),
			   int(imgIn.size[1]/devNum)]
	
	# 出力ファイルを作成
	imgOut = Image.new("RGB", (imgIn.size[0], imgIn.size[1]), (255,255,255,0))
	
	for x in range(0,devNum):
		for y in range(0,devNum):
			pixcelCount = 0
			colorSum = [0,0,0]
			
			# モザイクの１マス分の平均の色を計算する
			for xMoz in range(mozSize[0]):
				for yMoz in range(mozSize[1]):
					r,g,b = imgIn.getpixel( ( x * mozSize[0] + xMoz, y * mozSize[1] + yMoz ) )
					pixcelCount += 1
					colorSum[0] += r
					colorSum[1] += g
					colorSum[2] += b
			# 色が決まる
			mozColor = [colorSum[0]/pixcelCount,
						colorSum[1]/pixcelCount,
						colorSum[2]/pixcelCount]
			
			for xMoz in range(0,mozSize[0]):
				for yMoz in range(0,mozSize[1]):
					imgOut.putpixel((x*mozSize[0]+xMoz, y*mozSize[1]+yMoz), tuple(mozColor))
	
	# 保存
	imgOut.save(outFile)
