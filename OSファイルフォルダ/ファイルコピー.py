# coding: utf-8

# ファイルをコピー
import shutil

f = open('file1.txt','w')
f.write('test')
f.close()

# ファイルをコピー
# from, to
shutil.copyfile('file1.txt', 'file2.txt')

# フォルダ指定をすると、
# PermissionError: [Errno 13] Permission denied: '../'
# が出て、コピーできない。
#shutil.copyfile('file1.txt', '../')
