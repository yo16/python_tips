# -*- coding: utf-8 -*-

# pickleを使って保存したものを読む

import pickle

f = open('pickle_savetest.dump', 'rb')
l = pickle.load(f)
f.close()


print(l)
