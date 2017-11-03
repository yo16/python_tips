# -*- coding: utf-8 -*-

# scraping
# 参考
# https://qiita.com/beatinaniwa/items/72b777e23ef2390e13f8
# http://furyu.hatenablog.com/entry/20130102/1357132357
# http://www.cafe-gentle.jp/challenge/tips/python_tips_003.html

import lxml.html
import requests
import codecs

target_url = 'http://www.data.jma.go.jp/sakura/data/sakura003_02.html'
target_html = requests.get(target_url).text
root = lxml.html.fromstring(target_html)

print('Length:'+str(len(root.cssselect('pre'))))

#objContent = root.cssselect('pre')[0].text_content()
objContent = root.cssselect('pre')[0]
print(type(objContent))
#<class 'lxml.html.HtmlElement'>


#print(str(objContent))
#-> ShiftJisだと文字化けして何か出る
#-> UTF8だと下記で止まる
#Traceback (most recent call last):
#  File "scrape_base.py", line 18, in <module>
#    print(str(objContent))

#print(objContent.text)
#-> AttributeError: 'lxml.etree._ElementUnicodeResult' object has no attribute 'text'

#text = lxml.html.tostring(objContent[0])
#-> Type 'str' cannot be serialized.

#text = objContent[0]
#-> 空


#text = lxml.html.tostring(objContent)
#text = lxml.html.tostring(objContent, encoding='utf-8')
#text = lxml.html.tostring(objContent, method='text')
#text = lxml.html.tostring(objContent, method='xml')
text = lxml.html.tostring(objContent, method='text', encoding='utf-8')
#text = lxml.etree.tostring(objContent, pretty_print=True)
#text = lxml.html.tostring(objContent, method='text', encoding='utf-8', pretty_print=True)

#bin = objContent.encode('utf-8')
#print(type(text))

text = text.decode('utf-8')

#f = open('sakura.log', 'w')
f = codecs.open('scrape_base.log','w','utf-8')
f.write(text)
f.close()
