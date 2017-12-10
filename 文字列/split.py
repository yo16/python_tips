# -*- coding: utf-8 -*-

str = "abc,def,g"
ary = str.split(",")
print(ary)
# ['abc', 'def', 'g']


# セパレータがないときは、全要素＝１要素となる
str2 = "abcdef"
ary2 = str2.split(",")
print(ary2)
# ['abcdef']

