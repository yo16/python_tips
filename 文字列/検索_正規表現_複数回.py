# config: utf-8

import re

# rにしておくとバックスラッシュの文字をエスケープしなくていい
rePattern = r"b+(c+)"
# コンパイルしておくと、同じパターンで何度も検索するときに速くなる
#reObj = re.compile(rePattern)

str = "aaabbbbcccbbccaa"
#matchObj = reObj.search(str)


# コンパイルしない形式
# matchObj = re.match(rePattern, str)


iterator = re.finditer(rePattern, str)
for match in iterator:
	print(match.group(0))
	print(match.group(1))

	# マッチオブジェクトから情報を取り出す関数
	# group()	正規表現にマッチした文字列を返す。
	# start()	マッチの開始位置を返す。
	# end()	マッチの終了位置を返す。
	# span()	マッチの位置 (start, end) を含むタプルを返す。
