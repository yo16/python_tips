#  -*- using : utf-8 -*-

# 全角/半角変換
# jaconv
# https://qiita.com/yukinoi/items/42f8b5461dc1b62db7f9

import jaconv

# デフォルト
# ascii(アルファベット) : False
# kana(カタカナ) : True
# digit(数字) : False

str = u'アイウａｂｃ０１２'

print( jaconv.z2h(str) )
# ｱｲｳａｂｃ０１２

print( jaconv.z2h(str, ascii=True) )
# ｱｲｳabc０１２

print( jaconv.z2h(str, ascii=True, kana=False) )
# アイウabc０１２

print( jaconv.z2h(str, ascii=True, kana=False, digit=True) )
# アイウabc012
