# -*- coding:utf-8 -*-

# ラベリング
# （塊のグループ分け）
# 参考 http://imagingsolution.blog107.fc2.com/blog-entry-193.html

from PIL import Image

COLARRAY = [ \
			(255,0,0,0), (0,255,0,0), (0,0,255,0), \
			(255,255,0,0), (0,255,255,0), (255,0,255,0), \
			(128,0,0,0), (0,128,0,0), (0,0,128,0)]

def main():
	#img = Image.open(".\img\CreateImageFile.png")
	# img = Image.open(".\img\Labeling_lv1.png")
	# img = Image.open(".\img\Labeling_lv2.png")
	img = Image.open(".\img\Labeling_lv3.png")
	# img = Image.open(".\img\mscapture.png")
	if img.mode != "RGB":
		img = img.convert("RGB")
	#	pix = img.load()
	
	w = img.size[0]
	h = img.size[1]
	
	# 結果の配列
	rslt = [[ 0 for i in range(h) ] for j in range(w) ]
	
	# ルックアップテーブル
	lstColor = [0]
	# 最後に割り振った番号
	lastAssignedNum = 0
	
	# 横→縦方向に走査する
	for y in range(0,h):	# 縦
		for x in range(0,w):	# 横
			r,g,b = img.getpixel((x,y))
			# 色を適当に取得
			col = (r+g+b)
			# 色がある場合のみ、結果の配列を更新する
			if ( col == 0 ):	# なんとなく閾値７５(10%*3色くらいの色の違いはわからない)
				
				# これまでに設定した値を参照しながら、０以外の最小値を探す
				minVal = 0
				lstFoundKey = []
				# 左上
				if ( x > 0 ) and ( y > 0 ):
					tmp = rslt[x-1][y-1]
					if ( 0 < tmp ):
						if ( minVal == 0 ) or ( tmp < minVal ):
							minVal = tmp
						lstFoundKey.append( tmp )
				# 上
				if ( y > 0 ):
					tmp = rslt[x][y-1]
					if ( 0 < tmp ):
						if ( minVal == 0 ) or ( tmp < minVal ):
							minVal = tmp
						lstFoundKey.append( tmp )
				# 右上
				if ( x < w-2 ) and ( y > 0 ):
					tmp = rslt[x+1][y-1]
					if ( 0 < tmp ):
						if ( minVal == 0 ) or ( tmp < minVal ):
							minVal = tmp
						lstFoundKey.append( tmp )
				# 左
				if ( x > 0 ):
					tmp = rslt[x-1][y]
					if ( 0 < tmp ):
						if ( minVal == 0 ) or ( tmp < minVal ):
							minVal = tmp
						lstFoundKey.append( tmp )
				
				pixVal = 0
				if ( minVal == 0 ):
					# 周囲がすべて0の場合は、新しく割り当てる
					# print("new region("+str(x)+","+str(y)+")")
					lastAssignedNum += 1
					lstColor.append( lastAssignedNum )
					pixVal = lastAssignedNum
				else:
					# 周囲に割り当て済みの番号がある場合は、
					# その番号のルックアップテーブル値(更新後の値)を使用する
					pixVal = lstColor[ minVal ]
					
					# 見つけたルックアップテーブル値はすべて、
					# ルックアップテーブル値(更新後の値)で書き換える
					for key in lstFoundKey:
						lstColor[ key ] = pixVal
					
				# 計算した値を設定
				rslt[x][y] = pixVal
	
	# すべて割り当てられた！
	
	# ルックアップテーブル値で書き戻す
	for x in range(w):
		for y in range(h):
			rslt[x][y] = lstColor[ rslt[x][y] ]
	
	# なるべく小さな数に直す
	maxKey = 0
	for i in range(len(lstColor)):
		if( maxKey < lstColor[i] ):
			maxKey += 1
			# lstColor[i]と同じ値をすべて、maxKeyに書き換える
			tmp = lstColor[i]
			for j in range(len(lstColor)):
				if( tmp == lstColor[j] ):
					lstColor[j] = maxKey
	
	# [確認用]使った色の数を数える
	lstUsedColor = {}
	for x in range(w):
		for y in range(h):
			if ( lstColor[rslt[x][y]] not in lstUsedColor ):
				lstUsedColor[ lstColor[rslt[x][y]] ] = 1
			else:
				lstUsedColor[ lstColor[rslt[x][y]] ] += 1
	for k in lstUsedColor.keys():
		print("section("+str(k)+"):count="+str(lstUsedColor[k]))
	
	
	# rsltから画像を作る
	imgout = Image.new("RGB", (w, h), (255,255,255,0))
	for x in range(w):
		for y in range(h):
			if( lstColor[rslt[x][y]] == 0 ):
				col = (255, 255, 255, 0)
			else:
				col = COLARRAY[ lstColor[rslt[x][y]] % len(COLARRAY) ]
			
			imgout.putpixel((x,y), col)
	imgout.save(".\img\LabelingPracOut.bmp")
	imgout.show()

if __name__ == "__main__":
	main()

