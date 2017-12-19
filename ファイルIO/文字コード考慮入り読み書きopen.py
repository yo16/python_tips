# -*- coding: utf-8 -*-

# 文字コードを考慮する場合

import codecs


# encoding
#   utf_8
#   shift_jis
#   euc_jp
f = codecs.open('intext.txt', mode='r', encoding='utf_8')
#f = codecs.open('intext.txt', 'r', 'utf_8')

for line in f:
	#print(line)
	# → コマンドプロンプトではshift_jisと思って出力するから文字化けする
	
	
	# コマンドプロンプトへ出力するまでに
	# shift_jisへ変換する方法はまだわからない！＜＜未解決＞＞
	
	#l_temp = codecs.encode(line, 'utf_8')
	#print(l_temp)
	#print(codecs.encode(l_dec, encoding='shift_jis'))
	
	print(codecs.decode(line).encode('shift_jis'))
	
	

f.close()
