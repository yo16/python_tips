# coding: utf-8

# 非同期でプロセス実行
# 2017 (c) yo16

# 参考
# http://iuk.hateblo.jp/entry/2017/01/27/173449

import asyncio
import datetime
import subprocess


# コールバック関数
def display_date(end_time, loop):
	print(datetime.datetime.now())
	if( loop.time() + 1.0 ) < end_time:
		# time秒後にコールバック関数を呼ぶ処理を登録
		# loop.call_later(time, callback, *args)
		loop.call_later(1, display_date, end_time, loop)
	else:
		# loop.stop()関数をすぐ実行するように登録
		loop.call_soon(loop.stop)
		#loop.stop()				# この書き方でも動くけど、ダメなのか、よくわからない
		
		# loop.stop()が呼ばれると、現在実行中のイベントループ処理をすべて終えてから終了する
		
		print("stop!")


if __name__ == "__main__":
	# イベントループを取得
	loop = asyncio.get_event_loop()
	
	print("time:"+str(loop.time()))
	# → 秒のDouble値が入っている
	# （get_event_loopしたときの時刻？）
	
	# ５秒ごとにコールバック関数を呼んでほしいので+5.0する
	end_time = loop.time() + 5.0
	
	# call_soon関数を呼び出す
	# loop.call_soon(callback, *args)
	# コールバック関数の登録
	# イベントループをコントロールできるように、loopを渡している
	loop.call_soon(display_date, end_time, loop)
	print("run_forever")
	
	# イベントループを回す
	loop.run_forever()
	loop.close()
	
	print("end")




#全体の処理結果
# time:3393.77
# run_forever
# 2018-01-09 08:53:15.773574
# 2018-01-09 08:53:16.774674
# 2018-01-09 08:53:17.774774
# 2018-01-09 08:53:18.774874
# 2018-01-09 08:53:19.774974
# stop!
# end

# 非同期I/Oではなく、ノンブロッキングI/Oなので
# 日時が５回出るときと６回出るときがある
