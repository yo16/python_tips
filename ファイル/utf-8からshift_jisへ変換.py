# -*- coding:utf-8 -*-

import codecs

# utf-8のファイルからshift_jisのファイルへ変換する。
# 少なくとも、－（全角ハイフン）が変換できない。（解決できていない）
# 2017/12/6

infile = 'utf-8_in.txt'
outfile = 'shift_jis_out.txt'

inf = codecs.open(infile, 'r', encoding='utf-8')
outf = codecs.open(outfile, 'w', encoding='shift_jis')

for line in inf:
	outf.write(line)

inf.close()
outf.close()
