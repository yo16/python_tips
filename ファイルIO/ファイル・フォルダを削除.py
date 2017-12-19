# -*- coding:utf-8 -*-

import os
import shutil

file = 'tmpfile.txt'

# ファイルを作成
f = open(file, mode='w')
f.write('test')
f.close()

# 存在を確認
if os.path.exists(file):
	if os.path.isfile(file):
		# ファイルを削除
		os.remove(file)
		
	if os.path.isdir(file):		# elseでいいけど使ってみたかった
		# フォルダを削除
		os.rmdir(file)		# 空のディレクトリを削除
		#os.removedir(file)	# 再帰的に空のディレクトリを削除
		#shutil.rmtree(file)	# 再帰的にディレクトリを削除（空でなくても）
