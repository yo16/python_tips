# coding: utf-8

# 時間計測
# 2017 (c) yo16

import time


tm_start = time.time()

ary = []
for i in range(1500):
	ary.append(i)
time.sleep(1)

tm_end = time.time()


tm_elapsed = tm_end - tm_start
print(tm_elapsed)
# 1.0001001358032227
# 秒で取得できる
