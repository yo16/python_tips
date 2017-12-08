# coding: utf-8

# assert
# 変数が期待する値でないときに、例外を投げる

#assert 条件式,Falseのときに出すメッセージ


a = 1
assert a==1, 'a is not 1 !'
# 何も起こらない


list = []
#assert list, 'list is empty !'
# → 例外発生

list.append('x')
assert list, 'list is empty !'
# → 何も起こらない
