# -*- coding: utf-8 -*-

# collections
# 2017/3/21 (c) yo16

from collections import defaultdict


# defaultdict
# 参考:http://d.hatena.ne.jp/itasuke/20080914/p1
d = defaultdict(int)
s = "abrakadabra"

# 文字別にカウント
for i in s:
    d[i] += 1

# 結果表示
for k, v in d.items():
    print(k, v)

# 結果
# a 5
# r 2
# b 2
# k 1
# d 1




# 参考:http://sucrose.hatenablog.com/entry/2014/04/21/000909
d = defaultdict(list)
d['Hello'].append('World')
