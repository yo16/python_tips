# -*- coding: utf-8 -*-

import sys
import codecs

#f = open('intext.txt')
#f = open('intext.txt', 'r')
f = codecs.open('intext.txt', 'r', 'utf_8')


# 出力
for line in f:
	# 変数「line」には、行末に「\r\n」が入っている。
	# \r\nのそれぞれで改行されるため２度改行される。
	print(line)
	# もし行末の\r\nを除外したければ、replaceする必要あり。


f.close


print('end')
