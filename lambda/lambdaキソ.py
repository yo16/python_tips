# -*- coding: utf-8 -*-
# 参考:http://www.lifewithpython.com/2013/01/python-anonymous-function-lambda.html


# 基本
myfunc = lambda x: x*2+1
#下記と同じ
#	def myfunc(x):
#		return x*2+1
print(myfunc(5))
# 11
print(myfunc(6))
# 13



# sortedで使う
l1 = [(7,2),(3,4),(5,5),(10,3)]
l2 = sorted(l1, key=lambda x:x[1])
print(l2)
# [(7, 2), (10, 3), (3, 4), (5, 5)]



# mapで使う
# map()は、リストやタプルの各要素に対して同じ処理を施して、
# 同じ長さのリストにそのすべての結果を格納して返してくれる関数。
# map(関数, リスト)という形で使います。
l1 = [1,3,5]
l2 = list(map(lambda x: x**2, l1))		# 全要素の２乗
print(l2)
# [1, 9, 25]



# filterで使う
l1 = [1,2,3,4,5]
l2 = list(filter(lambda x: x%2==0, l1))		# あまり=0、つまり偶数だけ
print(l2)
# [2, 4]



