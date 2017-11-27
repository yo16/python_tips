# -*- coding: utf-8 -*-

# w:上書き出力
# a:追記出力
f = open('out.txt', 'w')


# write系は、改行を一切しないので注意

# 通常
f.write('aaa')

# listは、順番に連結して出力
f.writelines(['AAAA','BBB'])

# \nで、CrLfが入った
f.write('ccc\n')
f.write('ddd\n')

f.close()
