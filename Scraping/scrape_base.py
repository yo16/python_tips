# -*- coding: utf-8 -*-

# scraping
# 
# requestsでhtmlを取得して
# lxmlで解析して抽出
# 
# 参考
# https://qiita.com/beatinaniwa/items/72b777e23ef2390e13f8
# http://furyu.hatenablog.com/entry/20130102/1357132357
# http://www.cafe-gentle.jp/challenge/tips/python_tips_003.html

import requests
import lxml.html

target_url = 'http://www.data.jma.go.jp/sakura/data/sakura003_02.html'
response = requests.get(target_url)
response.encoding = response.apparent_encoding
target_html = response.text

# lxmlでhtmlを解析
root = lxml.html.fromstring(target_html)
objContent = root.cssselect('pre')[0]
bin = lxml.html.tostring(objContent, encoding='utf-8')	# 入力する文字はutf-8だと指示する
text = bin.decode('utf-8')	# utf-8としてdecode


f = open('scrape_base.log', 'w')
f.write(text)
f.close()
