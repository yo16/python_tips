# coding: utf-8

# strip
# 前後のスペースを除く

print('[' + ('   abc def ghi   '.strip()) + ']')
#[abc def ghi]

# タブや改行も除く
print('[' + ('  \t   aa   \n   '.strip()) + ']')
#[aa]



# 引数指定をすると、その文字を除く
# その場合、スペースや改行は除かない
print('[' + ('____ aa\n____'.strip('_')) + ']')
#[ aa
#]

# 文字列を渡すと複数指定
print('[' + ('xyxyzxyxyaaxxxxxx'.strip('xy')) + ']')
#[zxyxyaa]


