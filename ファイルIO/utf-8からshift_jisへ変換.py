# -*- coding:utf-8 -*-

import codecs

# utf-8のファイルからshift_jisのファイルへ変換する。
# Windowsの標準の文字コードは、Shift_JISではなく、
# Microsoftコードページ932 (cp932)であるため、
# cp932を指定する必要がある。
# 2017/12/6

infile = 'utf-8_in.txt'
outfile = 'shift_jis_out.txt'

inf = codecs.open(infile, 'r', encoding='utf-8')
#outf = codecs.open(outfile, 'w', encoding='shift_jis')
outf = codecs.open(outfile, 'w', encoding='cp932')

for line in inf:
	outf.write(line)

inf.close()
outf.close()
