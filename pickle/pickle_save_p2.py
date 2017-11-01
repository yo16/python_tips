# -*- coding: utf-8 -*-

# pickleを使って保存
# protocol 0
# python2のときの保存形式

import pickle

l = [10,20,30]

f = open('pickle_savetest_p2.dump', 'wb')
pickle.dump(l, f, 0)
f.close()

