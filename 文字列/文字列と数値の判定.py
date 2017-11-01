# -*- coding: utf-8 -*-

# 自前で用意するのがベターか
# 参考：http://www.python.ambitious-engineer.com/archives/420
def is_float_str(num_str, default=0):
	try:
		return {"is_float": True ,"val": float(num_str)}
	except ValueError:
		return {"is_float": False , "val": default}

print(is_float_str("1.5x")) # 変換に失敗{'is_float': False, 'val': 0}
print(is_float_str("-1.5")) # 変換に成功{'is_float': True, 'val': -1.5}
print(is_float_str("1E16")) # 変換に成功{'is_float': True, 'val': 1e+16}







# 以下は参考



# isdigit
#isdigitは、文字列が0～9で成り立っているか、ということだけを見ている

print("100".isdigit())
# True

print("-1".isdigit())
# False  <-!?

print("3.14".isdigit())
# False  <-!?

print("a".isdigit())
# False



print("------------------")

# isnumeric
# ヨクワカラナイ

print("-1".isnumeric())
# False

print("三十五".isnumeric())
# True
# 柔軟すぎるのもどうかと思う・・・

print("百二十一京".isnumeric())
# False
print("百二十一兆".isnumeric())
# True
print("百二十一億".isnumeric())
# True

