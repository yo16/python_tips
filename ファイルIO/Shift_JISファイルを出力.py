# -*- coding: utf-8 -*-

# Shift_JISファイルを出力
# (shift_jisとcp932は同じ)

import codecs


f = codecs.open('shift_jis.txt', mode='w', encoding='shift_jis')

f.write('日本語１２３')

# ↓この文字はできない！（未解決）
#f.write(u'－')
#f.write('－')

# encode時にignoreを指定すると、文字がスキップされる
str = (u'xx－yy').encode('shift_jis', 'ignore')
f.write(str.decode('shift_jis'))
# → xxyy
f.close()


# shift_jisx0213という形式なら・・・という記事
# https://stackoverflow.com/questions/6729016/decoding-shift-jis-illegal-multibyte-sequence
#f = codecs.open('shift_jis.txt', mode='w', encoding='shift_jisx0213')
#str = (u'xx－yy').encode('shift_jisx0213', 'ignore')
#f.write(str.decode('shift_jisx0213'))
# → xx・yy
#f.close()
