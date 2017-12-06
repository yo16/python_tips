# -*- coding: utf-8 -*-


# python 2.7だと、あいうえお にできるけど
# python 3.4だと、b'\x82\xa0\x82\xa4\x82\xa2\x82\xa6\x82\xa8'になる

#print(u"あういえお".encode('shift_jis'))
print(u"あういえお".encode('cp932'))
