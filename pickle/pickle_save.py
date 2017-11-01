# -*- coding: utf-8 -*-

# pickleを使って保存

import pickle

l = [10,20,30]

f = open('pickle_savetest.dump', 'wb')
pickle.dump(l, f)
f.close()

