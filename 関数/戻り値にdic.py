# -*- coding: utf-8 -*-

# 戻り値にdic
# 2017/11/01 y.ikeda


# 
def myFunc1():
	dicA = {}
	dicA['a'] = 'A'
	dicA['b'] = 'B'
	
	return dicA


retDic = myFunc1()

print( retDic['a'] )	# 'A'

