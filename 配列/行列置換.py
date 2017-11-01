# -*- coding:utf-8 -*-

# 行と列をひっくり返す
# Numpyを使わずに.
# http://asiagohan.hatenablog.com/entry/2015/05/08/170715


data = [[i+j*10 for i in range(3)] for j in range(2)]

print(data)
# [[0, 1, 2], [10, 11, 12]]

data2 = list(map(list, zip(*data)))

print(data2)
# [[0, 10], [1, 11], [2, 12]]
