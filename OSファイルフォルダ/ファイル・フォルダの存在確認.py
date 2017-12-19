# -*- coding:utf-8 -*-

# ファイルの存在確認

import os

# ファイル
print( os.path.exists('tekito-.txt') )
# → False


# ファイルかどうか
print( os.path.isfile('tekito-.txt') )
# → False
# ない場合もFalseになる。注意。


# ついでにフォルダかどうか
print( os.path.isdir('C:\Windows') )
# → True
# ない場合もFalseになる
