# -*- coding: utf-8 -*-

import sys
import psutil
import time

#for p in psutil.process_iter():
#	print(p.name)


#process = filter(lambda p: p.pid == 7240, psutil.process_iter())
#process = filter(lambda p: p.name() == 'python.exe', psutil.process_iter())
process = filter(lambda p: p.name() == 'CADmeister.exe', psutil.process_iter())

# プロセスごとの情報取得
for i in process:
	print(i.name())
	print(i.pid)
	for tm in range(10):
		# intervalは、指定秒数の値を取得する
		print(i.cpu_percent(interval=1))
		# 指定しない場合は、前回呼び出したときからの秒数
		# 下記と同じ。
		# ただし最初の呼び出しは必ず０になる。
		#print(i.cpu_percent())
		#time.sleep(1)
		