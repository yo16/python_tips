# -*- coding: utf-8 -*-

# 再帰の練習
# 2017/04/18 y.ikeda

def kaijou(a):
	if ( a <= 0 ) :
		return 1
	else :
		return kaijou(a-1)*a

print(kaijou(5))
# 5!=5*4*3*2*1=20*6 = 120


