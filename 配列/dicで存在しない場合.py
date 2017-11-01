
dicA = {}

dicA['a'] = 'A'
dicA['b'] = 'B'

print( dicA['a'] )

# 使用するとエラーになる
# print( dicA['c'] )
# KeyError 'c'

if 'c' in dicA:
	print('exist!')
else:
	print('not exist!')
