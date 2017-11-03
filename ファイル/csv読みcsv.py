# -*- coding : utf-8 -*-

# csvモジュールを使ったサンプル
#http://docs.python.jp/2/library/csv.html

import csv

f = open('csvsample.csv' ,'r')

reader = csv.reader(f)
header = next(reader)
for row in reader:
	print(row)

f.close()
