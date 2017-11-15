# -*- coding: utf-8 -*-


print('{0}と{1}'.format(100,200))
# 100と200


print('{hen1}と{hen2}'.format(hen1=10,hen2=20))
# 10と20


# listを使う
lst1 = [11,21]
lst2 = [12,22]
print('{0[0]}と{0[1]}、{1[0]}と{1[1]}'.format(lst1, lst2))
# 11と21、12と22


# dictionaryを使う
dict = {'name1':'aa', 'name2':'bb', 'val':123}
print('{name1}と{name2}と{val}'.format(**dict))
# aaとbbと123



# 書式
#型名	説明
#b		2進数で出力
#d		10進数で出力
#o		8進数で出力
#x		16進数で出力
#X		16進数で出力
print('{0}は2進数だと{0:b}'.format(8))
# 8は2進数だと1000

#型名	説明
#<任意の幅	任意の幅を取り、左詰め
#>任意の幅	任意の幅を取り、右詰め
#^任意の幅	任意の幅を取り、中央寄せ
print('{0:>5}円'.format(10))
print('{0:>5}円'.format(200))
print('{0:>5}円'.format(3000))
#   10円
#  200円
# 3000円

