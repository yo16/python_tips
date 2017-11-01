# -*- coding: utf-8 -*-

# いろいろやってみたけど
# よくわからない・・・
# 2015/11/6

import sys
import codecs


# sys.stdin  = codecs.getreader('shift_jis')(sys.stdin)
# sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

#for line in open('test_sjis.txt', 'r'):
#	print(line)



fin = codecs.open('test_UTF8.txt', 'r', 'utf-8')
for line in fin:
	print(line)

#fin = codecs.open('test_sjis.txt', 'r', 'shift_jis')
#for line in fin:
#	print(line)

