# -*- coding: utf-8 -*-

import requests

url = 'http://www.data.jma.go.jp/sakura/data/sakura003_02.html'

# get
response = requests.get(url)

# エンコードを指定
response.encoding = response.apparent_encoding
# ちなみに
print(response.apparent_encoding)
# utf-8

# テキストを抽出
html = response.text


log = open('requests_sample.log', 'w')
log.write(html)
log.close()
