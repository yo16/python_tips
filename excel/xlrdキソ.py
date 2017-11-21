# -*- coding:utf-8 -*-

import xlrd

book = xlrd.open_workbook('TestFile.xlsx')
print('シート数:'+str(book.nsheets))

i = 0
for name in book.sheet_names():
	i += 1
	print('シート名:No.'+str(i)+':'+name)

# シート名 別解
print('シート名:'+book.sheet_by_index(0).name)



sheet1 = book.sheet_by_index(0)
# 最終の行数、列数
# 数なので、１行だったら１
print('行数/列数:'+str(sheet1.ncols)+'/'+str(sheet1.nrows))

# セルの値を取得
# はじめは０
print('値(D6):'+sheet1.cell(5,3).value)


