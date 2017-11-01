# -*- coding:utf-8 -*-

# ディクショナリのsetdefault

# ディクショナリの参照で、
# 通常は存在しないキーを読むとエラーになるから
# 存在しないキーを読んだときにこれを返してねっていう値




# 'a'というキーが設定されていない場合は'*'を返すよう準備
dic1 = {}
dic1.setdefault('a', '*')
print( dic1['a'] )
# → *

# 設定した場合
dic2 = {}
dic2.setdefault('a', '*')
dic2['a'] = 'A'
print( dic2['a'] )
# → A



# 下記と同じ感じ
dic3 = {}
if 'a' not in dic3:
	dic3['a'] = '*'
print( dic3['a'] )

