# coding:utf-8

str = 'abcabcabcd'


print( str.replace('a', 'A') )
# → AbcAbcAbcd


# 回数指定（こんなの使うかな？？１回の指定で使うかな）
print( str.replace('a', 'A', 2) )
# → AbcAbcabcd


# aまたはcをxへ置換するには、
# 正規表現で置換する必要あり。
#print( str.replace('[ac]', 'x') )	# NG!
import re
print( re.sub(r'[ac]', 'x', str) )
# → xbxxbxxbxd

