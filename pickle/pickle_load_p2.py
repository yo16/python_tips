# -*- coding: utf-8 -*-

# pickleを使って保存したものを読む
# python2で作成したdumpファイル
# 指定しなくても、勝手に解釈してくれる

import pickle

f = open('pickle_savetest_p2.dump', 'rb')
#f = open('banner.p', 'rb')
l = pickle.load(f)
f.close()


print(l)
