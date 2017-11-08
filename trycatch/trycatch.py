# -*- coding: utf-8 -*-

# try-catch

import sys

for i in range(10):
	print(str(i))
	try:
		if i > 5:
			num = 5/0
			# ZeroDivisionErrorがraiseされる
	except OSError as oserr:
		print("os error! {0}".format(oserr))
	except ZeroDivisionError as ez:
		#print('zero-wari', ez)
		print('zero-wari')
	except:
		print('unexcepted error')
	else:
		# exceptionが何もない場合
		print('no-error!')
	finally:
		# exceptionがあってもなくても最後
		print('finally!')

