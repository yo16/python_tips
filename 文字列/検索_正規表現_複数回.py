# config: utf-8

import re

# rにしておくとバックスラッシュの文字をエスケープしなくていい
rePattern = r"b+(c+)(.)?"
# コンパイルしておくと、同じパターンで何度も検索するときに速くなる
#reObj = re.compile(rePattern)

str = "aaabbbbcccbbcc"
#matchObj = reObj.search(str)


# コンパイルしない形式
# matchObj = re.match(rePattern, str)


iterator = re.finditer(rePattern, str)
for match in iterator:
	#print(match.groups('x'))  # パターン内のグループのタプル(引数あり)
	print(match.groups())  # パターン内のグループのタプル(引数なし)
	print(match.group(0))  # 検索対象全体
	print(match.group(1))  # 最初の丸括弧
	print(match.group(2))  # ２つ目の丸括弧

	# マッチオブジェクトから情報を取り出す関数
	# group()	正規表現にマッチした文字列を返す。
	# start()	マッチの開始位置を返す。
	# end()	マッチの終了位置を返す。
	# span()	マッチの位置 (start, end) を含むタプルを返す。

# 2つ目の丸括弧の(.)?は、ヒットしないときは
# Noneが入る。
# match.groups()に引数を与えてやるとNoneがその文字になる。
# 例えばmatch.groups()では
# ('ccc', 'b')と('cc', None)だが
# match.groups('x')では
# ('ccc', 'b')と('cc', 'x')になる
