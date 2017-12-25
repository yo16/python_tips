# -*- coding: utf-8 -*-

# 関数の引数にリスト
# 2017/4/18 yo16


# 参照するのみ
def myFunc1(myLst):
	for elm in myLst:
		print(elm)		# →参照できる

# 追加
def myFunc2(myLst2):
	myLst2.append(40)


l1 = [10,20,30]
myFunc1( l1 )
myFunc2( l1 )
myFunc1( l1 )	# →追加されている


