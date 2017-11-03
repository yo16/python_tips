# -*- coding: utf-8 -*-

#dict型の連結

dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}

dict1.update( dict2 )

print(dict1["c"])
# 3


dict2["c"] = 999
print(dict1["c"])
# 3
# リンクがついているわけではなく、
# コピーされているので、
# 元が変わっても反映されない。


dict3 = {"a":100}
dict1.update(dict3)
print(dict1["a"])
# 100
同じキーがある場合は後勝ち
