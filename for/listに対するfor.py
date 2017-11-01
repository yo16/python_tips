# -*- coding: utf-8 -*-

# listに対するfor
# 2017/3/21 (c) y.ikeda

elements = ['aa','bb','cc']

# 0から始まるindexと値を同時に取れる
for i, elm in enumerate(elements):
	print(str(i)+":"+elm)

