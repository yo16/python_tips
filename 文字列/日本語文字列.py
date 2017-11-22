# -*- using : utf-8 -*-


str = '日本語no文字列'


# 表示
print(str)
# → 日本語no文字列
# コマンドプロンプトにちゃんと出る

# 長さ
print(len(str))
# → 8

# 切り出し
# 日本語no文字列
print(str[2:4])
# → 語n
# ２バイト文字と混じっても、１文字ずつ分ける！
print(str[1:7])
# → 本語no文字


# 比較
if str == '日本語文字列':
	print('icchi')
	# 正常に動作
