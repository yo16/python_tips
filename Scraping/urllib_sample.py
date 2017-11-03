# -*- coding: utf-8 -*-

from urllib.request import urlopen

f = urlopen('http://www.data.jma.go.jp/sakura/data/sakura003_02.html')
#f = urlopen('http://qiita.com/advent-calendar/2014')


print(f.code)
# 200

print(f.getheader('content-type'))
# text/html

print(f.info().get_content_charset())
# None


bin = f.read()
f.close()
text = bin.decode('utf-8')

log = open('sakura.log', 'w')
log.write(text)
log.close()
