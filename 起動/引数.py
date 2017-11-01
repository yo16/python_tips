# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":

	params = sys.argv
	
	print(params)
	
	#print("数:%d" % sys.argc)	# argcはない
	paramnum = len(params)
	print("数:%d" % paramnum)
	
	print("第０引数(スクリプト名):%s" % params[0])
	print("第１引数:%s" % params[1])
	print("第２引数:%s" % params[2])
	print("第３引数:%s" % params[3])
	print("第４引数:%s" % params[4])
	# print("第５引数:%s" % params[5])	# 超えると、実行時エラー
