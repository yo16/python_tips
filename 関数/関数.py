# -*- coding: utf-8 -*-

def myFunc1():
	print('this is in myFunc1.')

def myFunc2(param):
	print('***' + param + '***')

def myFunc3(p1, p2):
	return p1+p2



print('start')

myFunc1()
myFunc2('aaa')
#myFunc99()		# 下に定義されている関数は呼べない
print( myFunc3(3,5) )
print('end')



def myFunc99():
	print('this is in myFunc99.')