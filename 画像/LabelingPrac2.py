# -*- coding:utf-8 -*-

# LabelingPrac.pyを見ながら
# 思い出すためのコーディング


# ラベリング
# （塊のグループ分け）
# 参考 http://imagingsolution.blog107.fc2.com/blog-entry-193.html

from PIL import Image
import sys
import pdb
import datetime

COLARRAY = [ \
			(255,255,255,0), (255,0,0,0), (0,255,0,0), (0,0,255,0), \
			(255,255,0,0), (0,255,255,0), (255,0,255,0), \
			(128,0,0,0), (0,128,0,0), (0,0,128,0), \
			(128,128,0,0), (0,128,128,0), (128,0,128,0), \
			(255,128,0,0), (0,255,128,0), (128,0,255,0), \
			(128,255,0,0), (0,128,255,0), (255,0,128,0) \
]

# 【デバッグ用】rsltの数値をcsv出力する
def putCsv(ary2d):
	d = datetime.datetime.today()
	
	outFile = ".\\csv\\LabelingPrac2out_{0:02d}{1:02d}{2:02d}_{3:06d}.csv".format(d.hour, d.minute, d.second, d.microsecond)
	f = open(outFile, "w")
	
	# 縦横置換
	ary2d_t = list(map(list, zip(*ary2d)))
	
	for i in range(len(ary2d_t)):
		for j in range(len(ary2d_t[i])):
			elm = ary2d_t[i][j]
			
			f.write(str(elm)+",")
		f.write("\n")
	f.close()

def main():
	# img = Image.open(".\\img\\CreateImageFile.png")
	# img = Image.open(".\\img\\test1.png")
	# img = Image.open(".\\img\\test2.png")
	# img = Image.open(".\\img\\test3.png")
	# img = Image.open(".\\img\\test4.png")
	# img = Image.open(".\\img\\test4-2.png")
	# img = Image.open(".\\img\\test5.png")
	#img = Image.open(".\\img\\test6-1.png")
	#img = Image.open(".\\img\\test6-2.png")
	#img = Image.open(".\\img\\test6-3.png")
	#img = Image.open(".\\img\\test6-4.png")
	#img = Image.open(".\\img\\test7.png")
	#img = Image.open(".\\img\\test8.png")
	#img = Image.open(".\\img\\test9.png")
	#img = Image.open(".\\img\\test10.png")
	#img = Image.open(".\\img\\test11.png")
	#img = Image.open(".\\img\\Labeling_lv1.png")
	#img = Image.open(".\\img\\Labeling_lv1_1.png")
	#img = Image.open(".\\img\\Labeling_lv2.png")
	#img = Image.open(".\\img\\Labeling_lv3.png")
	img = Image.open(".\\img\\mscapture.png")
	if img.mode != "RGB":
		img = img.convert("RGB")
	#	pix = img.load()
	
	w = img.size[0]
	h = img.size[1]
	
	# 結果の配列
	rslt = [[ 0 for i in range(h) ] for j in range(w) ]
	
	# ルックアップテーブル
	lstLookupTable = [0]
	# 最後に割り振った番号
	lastAssignedNum = 0
	
	# ★breakpoint
	# http://racchai.hatenablog.com/entry/2016/05/30/070000
	# s(tep)		ステップイン
	# n(ext)		ステップオーバー
	# r(eturn)		ステップアウト
	# l(ist)		現在行の前後のソースコードを表示
	# a(rgs)		現在いる関数の引数を表示
	# p				プリント
	# c(ont(inue))	次のブレイクポイントまで実行
	# 横→縦方向に走査する
	for y in range(0,h):	# 縦
		for x in range(0,w):	# 横
			#if sys.flags.debug : print('point(x:{0:2d},y:{1:2d})'.format(x,y))
			#if (sys.flags.debug and (x==1) and (y==2)) : pdb.set_trace()
			
			r,g,b = img.getpixel((x,y))
			# 色を適当に取得
			col = (r+g+b)
			
			# 色がゼロの場合は、ラベリングでゼロ番と決める
			# 以下では、色がゼロでない場合のラベリングをする
			labelNo = 0
			if ( 0 < col ):
				# 上の段と左を見て、最小の値を探す
				minVal = 9999
				lstFoundLabels = []	# 見つけたラベルのリスト
									# 最後にすべてまとめて、ルックアップテーブルにminValを設定する
				# 左上
				if ( 0 < x ) and ( 0 < y ):
					surroundLabel = rslt[x-1][y-1]
					if ( 0 < surroundLabel ):			# ラベル設定済み
						if ( lstLookupTable[surroundLabel] < minVal ):		# 周囲のラベルの中で最小
							# minValが更新された
							# rslt[x][y]の候補値を設定
							minVal = lstLookupTable[surroundLabel]
						
						# 見つけたラベルのリストへ追加
						lstFoundLabels.append(surroundLabel)
				
				# 上
				if ( 0 < y ):
					surroundLabel = rslt[x][y-1]
					if ( 0 < surroundLabel ):			# ラベル設定済み
						if ( lstLookupTable[surroundLabel] < minVal ):		# 周囲のラベルの中で最小
							# minValが更新された
							# rslt[x][y]の候補値を設定
							minVal = lstLookupTable[surroundLabel]
						
						# 見つけたラベルのリストへ追加
						lstFoundLabels.append(surroundLabel)
				
				# 右上
				if ( x < w-1 ) and ( 0 < y ):
					surroundLabel = rslt[x+1][y-1]
					if ( 0 < surroundLabel ):			# ラベル設定済み
						if ( lstLookupTable[surroundLabel] < minVal ):		# 周囲のラベルの中で最小
							# minValが更新された
							# rslt[x][y]の候補値を設定
							minVal = lstLookupTable[surroundLabel]
						
						# 見つけたラベルのリストへ追加
						lstFoundLabels.append(surroundLabel)
				
				# 左
				if ( 0 < x ):
					surroundLabel = rslt[x-1][y]
					if ( 0 < surroundLabel ):			# ラベリング済み
						if ( lstLookupTable[surroundLabel] < minVal ):		# 周囲のラベルの中で最小
							# minValが更新された
							# rslt[x][y]の候補値を設定
							minVal = lstLookupTable[surroundLabel]
						
						# 見つけたラベルのリストへ追加
						lstFoundLabels.append(surroundLabel)
				
				# minValが更新されたか否かで、
				# カレントの[x][y]に設定するlabelNoを決める
				if( minVal < 9999 ):
					# minValがsys.maxintから更新されている場合は、
					# 周囲にラベリング済みのマスがあったということ。
					# カレントの[x][y]は、minValに決定
					labelNo = minVal
					
					# 見つけたラベルに対するルックアップテーブルの値は、
					# 最小値に書き換える
					for foundLabel in lstFoundLabels:
						if ( minVal < lstLookupTable[ foundLabel ] ):
							# 既に入っている値より小さいときだけ、書き換える
							lstLookupTable[ foundLabel ] = minVal
				
				else:
					# 更新されていないので、周囲にラベリング済みのマスはなかったということ。
					# カレントの[x][y]は、最後のラベリング番号＋１番に決定
					lastAssignedNum += 1;
					labelNo = lastAssignedNum;
					
					# ルックアップテーブルへ要素を追加
					# index＝値＝lastAssignedNum
					lstLookupTable.append(lastAssignedNum)
			
			# ラベリング番号を設定
			rslt[x][y] = labelNo
	
	# すべて割り当てられた！
	#showLookupTable(lstLookupTable)
	
	# ルックアップテーブルは各々のセルの最小値に書き換わっているが
	# 遡ってはいないので、すべて遡って同じ値にする
	for i in range(lastAssignedNum):
		for j in range(i, lastAssignedNum):
			if ( i == lstLookupTable[j] ):
				lstLookupTable[j] = lstLookupTable[i]
	#showLookupTable(lstLookupTable)
	
	#putCsv(rslt)
	
	# ルックアップテーブル値で、データを書き戻す
	for x in range(w):
		for y in range(h):
			rslt[x][y] = lstLookupTable[ rslt[x][y] ]
	#showLookupTable(lstLookupTable)
	
	#putCsv(rslt)
	
	# なるべく小さな数に直す
	maxKey = 0
	for i in range(len(lstLookupTable)):
		if( maxKey < lstLookupTable[i] ):
			maxKey += 1
			# lstLookupTable[i]と同じ値をすべて、maxKeyに書き換える
			tmp = lstLookupTable[i]
			for j in range(len(lstLookupTable)):
				if( tmp == lstLookupTable[j] ):
					lstLookupTable[j] = maxKey
	
	# [確認用]使った色の数を数える
	lstUsedColor = {}
	for x in range(w):
		for y in range(h):
			if ( lstLookupTable[rslt[x][y]] not in lstUsedColor ):
				lstUsedColor[ lstLookupTable[rslt[x][y]] ] = 1
			else:
				lstUsedColor[ lstLookupTable[rslt[x][y]] ] += 1
	for k in lstUsedColor.keys():
		print("section("+str(k)+"):count="+str(lstUsedColor[k]))
	
	
	# rsltから画像を作る
	imgout = Image.new("RGB", (w, h), (255,255,255,0))
	for x in range(w):
		for y in range(h):
			col = COLARRAY[ lstLookupTable[rslt[x][y]] % len(COLARRAY) ]
			
			imgout.putpixel((x,y), col)
	imgout.save(".\\img\\LabelingPrac2Out.bmp")
	imgout.show()


def showLookupTable(tbl):
	print("--- show LookupTable ---")
	for i in range(len(tbl)):
		print('[{0:3d}]:{1:3d}'.format(i, tbl[i]))



if __name__ == "__main__":
	main()

