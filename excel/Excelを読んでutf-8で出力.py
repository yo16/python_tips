# -*- coding:utf-8 -*-

# Excelはshift_jisだから、うまくできないのかなと思ったら
# あっさりできた

import xlrd
import codecs

book = xlrd.open_workbook('TestFile.xlsx')


sheet1 = book.sheet_by_index(0)

# セルの値を取得
str = sheet1.cell(5,3).value
# でぃーろく



# そのまま出力
f1 = open('file1.txt', mode='w', encoding='utf-8')
f1.write(str)
# → 正しくutf-8で出力される

f1.write('\n')


# unicode文字列と組み合わせる
str2 = u'日本語大丈夫ですか:{0}'.format(str)
f1.write(str2)


f1.write('\n')

f1.close()



# クローズ
book.release_resources()
del book
