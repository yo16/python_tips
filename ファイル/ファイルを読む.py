# -*- coding: utf-8 -*-

import sys
import codecs

#f = open('intext.txt')
#f = open('intext.txt', 'r')
f = codecs.open('intext.txt', 'r', 'utf_8')


# 出力
# \r\nのそれぞれの文、２度改行される
for line in f:
	print(line)


f.close


print('end')
