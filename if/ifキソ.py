# -*- coding: utf-8 -*-


# 数字の比較
num1 = 10
num2 = 11

if num1 == num2 :
	print '***********'
elif num1 < num2 :
	print num1 < num2
else:
	print 'test1'

if num1 != num2:
	print 'test2'

if num1 < num2:
	print 'test3'

if num1 <= num2:
	print 'test4'


# 文字の比較
str1 = 'abc'
str2 = 'abc'

if str1 == str2:
	print 'test5'

str2 = str2+'d'
if str1 != str2:
	print 'test6'



# and or
if (num1 != num2) and (str1 != str2):
	print 'test7'

if (num1+1 == num2) or (str1 == str2):
	print 'test8'
