# -*- coding: utf-8 -*-

import re
# 
# 参考
# http://shinriyo.hateblo.jp/entry/2015/01/28/Python%E3%81%A7%E5%85%A8%E3%81%A6%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A%E3%81%8B%E3%81%AE%E5%88%A4%E5%AE%9A


# 全て全角カタカナか？
# Pythonの正規表現で、渡された文字列が全てASCII文字かチェックします。(UTF-8向け)
# Python 正規表現 ASCII文字 UTF8


a = u"カタカナ".encode('utf-8')
print(a)
# b'\xe3\x82\xab\xe3\x82\xbf\xe3\x82\xab\xe3\x83\x8a'


regexp = re.compile(br'^(\xE3\x82[\xA1-\xBF]|\xE3\x83[\x80-\xB6])+$')
result = regexp.search(a)
if result != None:
    print(u"すべてが全角カタカナである")
else:
    print(u"すべてが全角カタカナというわけではない")
# すべてが全角カタカナである


# 解説
# encodeしたバイト文字列に対して正規表現で検索する場合には
# br'・・・'の表記で正規表現を書けばできる。
# r'・・・'だと、
# TypeError: cannot use a string pattern on a bytes-like object
# のエラー出る。rで指定した文字列をバイト列に適用できないというエラー。

