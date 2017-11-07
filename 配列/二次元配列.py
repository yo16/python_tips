# -*- coding: utf-8 -*-

# ２次元配列の操作

ary2d = [[ i+j*10 for i in range(3) ] for j in range(4) ]

# 概要
print(ary2d)
#[[0, 1, 2], [10, 11, 12], [20, 21, 22], [30, 31, 32]]


for i in range(len(ary2d)):
	for j in range(len(ary2d[i])):
		print( ary2d[i][j] )
#0
#1
#2
#10
#11
#12
#20
#21
#22
#30
#31
#32
