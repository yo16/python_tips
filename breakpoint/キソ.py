# -*- coding: utf-8 -*-

# breakpointの練習
# http://racchai.hatenablog.com/entry/2016/05/30/070000
# s(tep)		ステップイン
# n(ext)		ステップオーバー
# r(eturn)		ステップアウト
# l(ist)		現在行の前後のソースコードを表示
# a(rgs)		現在いる関数の引数を表示
# p				プリント
# c(ont(inue))	次のブレイクポイントまで実行

import pdb



def test1( num ):
	print("test1")
	print( str(num) )

def test2( num ):
	print("test2")
	print( str(num) )


if __name__ == "__main__":
	pdb.set_trace()		# ブレイクポイントの設定
	for i in range(5):
		test1(i)
	
	pdb.set_trace()		# ブレイクポイントの設定
	for i in range(5,10):
		test2(i)

