# -*- coding: utf-8 -*-


# .find(検索する文字列, 開始位置, 終了位置)
# .rfind(検索する文字列, 開始位置, 終了位置)	# 後ろから
# .index(検索する文字列, 開始位置, 終了位置)
# .rindex(検索する文字列, 開始位置, 終了位置)	# 後ろから
# findとindexの違いは、
# 見つからない場合、findは-1を返し、indexは実行時エラーになる


str = 'abcdefgd'
#      01234567

print(str.find('cde',0))
# → 2

print(str.find('cdd',0))
# → -1


#print(str.index('cdd',0))
# Traceback (most recent call last):
#   File "検索.py", line 21, in <module>
#     print(str.index('cdd',0))
# ValueError: substring not found


print(str.rfind('d'))
# → 7


