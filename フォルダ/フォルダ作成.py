# -*- coding: utf-8 -*-

# フォルダ作成/削除


import os

if not os.path.isdir('abc'):
	os.mkdir('abc')

if not os.path.isdir('def'):
	os.mkdir('def')


if os.path.isdir('def'):
	os.rmdir('def')
