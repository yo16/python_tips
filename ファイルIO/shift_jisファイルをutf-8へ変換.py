# -*- encode:utf-8 -*-

import codecs

inFilePath = 'shift_jis-file.txt'
outFilePath = 'utf-8-file.txt'

inf = codecs.open(inFilePath, mode='r', encoding='shift_jis')
outf = codecs.open(outFilePath, mode='w', encoding='utf-8')

for line in inf:
	outf.write(line)

inf.close()
outf.close()
