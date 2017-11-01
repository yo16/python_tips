# -*- coding: utf-8 -*-

# 関数内のスコープ
# グローバル変数をいじる


def myFunc1():
	aa = 100
	# グローバルだと思っていても、実際は外へのスコープがないので
	# 外の変数は変更されない

def myFunc2():
	global bb	# 内から、外のグローバル変数を使うという宣言をする
	bb = 200




print('start')

aa = 10
myFunc1()
print( aa )
# 10

bb = 20
myFunc2()
print( bb )
# 200


