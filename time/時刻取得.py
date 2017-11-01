# -*- coding:utf-8 -*-

import datetime



d = datetime.datetime.today()
print(d)
# 2016-03-30 09:46:26.302337

print(type(d))
# <class 'datetime.datetime'>

print('%d年%02d月%02d日 %02d時%02d分%02d.%d秒//' \
	 % (d.year, d.month, d.day, d.hour, d.minute, d.second, d.microsecond))
# 2016年03月30日 09時46分26.302337秒//
# %dでも%sでも前ゼロはないので要注意

