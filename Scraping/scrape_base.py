# -*- coding: utf-8 -*-

# scraping
# 参考
# https://qiita.com/beatinaniwa/items/72b777e23ef2390e13f8

import lxml.html
import requests

target_url = 'http://www.data.jma.go.jp/sakura/data/sakura003_02.html'
target_html = requests.get(target_url).text
root = lxml.html.fromstring(target_html)

objContent = root.cssselect('pre')[0].text_content()

text = lxml.html.tostring(objContent, method='text', encoding='utf-8')
#http://furyu.hatenablog.com/entry/20130102/1357132357
#http://www.cafe-gentle.jp/challenge/tips/python_tips_003.html

f = open('sakura.log', 'w')
f.write(text)
f.close()
