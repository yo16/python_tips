# -*- coding: utf-8 -*-


# 配列基礎
# ３種類ある
# リスト
# タプル
#		リストとほぼ同じだが、追加できない
# 辞書



# -------------------
# リスト
print('list-----------------')
# -------------------
# 初期化
listA = [10, 20, 30]

# 参照
print(listA[1])
# 20

# 変更
listA[1] = 21

# 要素を追加
listA.append(40)

# リストを追加
listA.extend([50, 60])

print(listA)
# [10, 21, 30, 40, 50, 60]

# ループで１要素ずつ
for elm in listA:
	print(elm)

# 要素数
print('len:' + str(len(listA)))

# 存在
if 21 in listA:
	print('exists')
else:
	print('not exists')



# -------------------
# タプル
print('tuple-----------------')
# -------------------
# 初期化
tupleA = (10, 20, 30)

# 参照
print(tupleA[1])
# 20

# 設定
#tupleA[1] = 22
# TypeError: 'tuple' object does not support item assignment

# 要素を追加
#tupleA.append(40)
# AttributeError: 'tuple' object has no attribute 'append'

print(tupleA)
# (10, 20, 30)

# ループで１要素ずつ
for elm in tupleA:
	print(elm)

# 要素数
print('len:' + str(len(tupleA)))




# -------------------
# 辞書
print('dic-----------------')
# dicだと、追加するときに楽.appendとか言わなくていいから。
# -------------------
# 初期化 # 改行が許されている模様
dicA = {
	'a':10, 
	'b':20, 
	'c':30
}

# 参照
print(dicA['b'])
# 20

# 設定
dicA['b'] = 21

# 要素を追加
dicA['d'] = 40

print(dicA)
# {'b': 21, 'd': 40, 'a': 10, 'c': 30}		# 順番は保障されない

# ループで１要素ずつ		# 順番は保障されない
for elm in dicA:
	print(elm)
	# b、d、a、c
	
	print(dicA[elm])
	# 21、40、10、30

# 要素数
print('len:' + str(len(dicA)))

