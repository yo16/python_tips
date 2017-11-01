# -*- coding: utf-8 -*-

# ２次元配列のループ

ary2d = [[ i+j*10 for i in range(3) ] for j in range(4) ]

# 概要
print(ary2d)
#[[0, 1, 2], [10, 11, 12], [20, 21, 22], [30, 31, 32]]


for elm1 in ary2d:
	for elm2 in elm1:		# elm1は配列[0,1,2]
		print( str(elm2)+"," )
"""
0,
1,
2,
10,
11,
12,
20,
21,
22,
30,
31,
32,
"""

