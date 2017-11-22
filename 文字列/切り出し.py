# coding:utf-8

str = 'abcde'

# 開始index:終了index
print(str[2:3])
# → c

# 前２文字
print(str[:2])
# → ab

# 後ろから２文字
print(str[-2:])
# → de

# 後ろから２文字を除く
print(str[:-2])
# → abc



# 日本語
str2 = 'あいうえお'
print(str[2:4])
# →出ない！
