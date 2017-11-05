# -*- coding : utf-8 -*-

# 参項演算子
# 2017/11/4 y.ikeda

def kigu(n):
	return str(n) + ' is ' + ('even' if n%2==0 else 'odd')


print( kigu(10) )
print( kigu(11) )



print('------------')

# 上記であれば、lambdaを使うと少しスマート？
kigu2 = lambda n: str(n) + ' is ' + ('even' if n%2==0 else 'odd')

print(kigu2(20))
print(kigu2(21))
