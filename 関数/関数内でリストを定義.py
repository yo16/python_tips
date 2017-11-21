

def test1(ary):
	ary = [10,20]
	# ↑別のリストを変数に入れてしまうと
	#   呼び出し元のリストはもう更新できない
	ary.append(30)
	# objectの参照渡しとはちょっと違うみたい



param = [1, 2]

test1(param)

print(param)
# [1, 2]
