# はじめてのNumPy
# 参考 http://qiita.com/wellflat/items/284ecc4116208d155e01
# 2016/1/16

import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

print(a)

print(a.flags)
#  C_CONTIGUOUS : True   ## データがメモリ上に連続しているか(C配列型)
#  F_CONTIGUOUS : False  ## 同上(Fortran配列型)
#  OWNDATA : True        ## 自分のデータかどうか、ビュー(後述)の場合はFalse
#  WRITEABLE : True      ## データ変更可能か
#  ALIGNED : True        ## データ型がアラインされているか
#  UPDATEIFCOPY : False  ## Trueには変更できないので特に気にしなくて良い

# 次元数
print( "%d次元" % a.ndim )
# 2

# 要素数
print( "要素数:%d" % a.size )
# 12

# 各次元の要素数（行数, 列数）
print( "各次元の要素数(行数, 列数):(%d, %d)" % a.shape )
# (4, 3)

# １要素のバイト数
print( "１要素のバイト数:%d" % a.itemsize )
# 4
# 64bit版だと、8かも

# 次の行までのバイト数
# 24バイトで次の行、8バイトで次の列
print( "%dバイトで次の行, %dバイトで次の列" % a.strides )
# (12, 4)
# 1,2,3
# 4,5,6
# の順で直列に並んでいるということ。

# 配列全体のバイト数
print( "配列全体のバイト数:%dbyte" % a.nbytes )
# 48	# a.itemsize * a.size

# 要素のデータ型
print( "型:%s" % a.dtype )
# int32


