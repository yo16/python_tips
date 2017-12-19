# coding: utf-8

# pdfminerTest
# 2017 (c) y.ikeda
# pdfminerはpython2用で、
# 本プログラムはpython3を使いたかったのでpdfminer.sixを使用。

# 参考：http://irukanobox.blogspot.jp/2017/03/python3pdf.html
#       https://qiita.com/korkewriya/items/72de38fc506ab37b4f2d


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import codecs


# 入力ファイル
inFileName = './input/jo.pdf'
#inFileName = './input/simple1.pdf'
#inFileName = './input/simple2.pdf'
#inFileName = './input/simple3.pdf'
# 出力ファイルは、拡張子をtxtに変える
outFileName = inFileName[:inFileName.rfind('.')]+'.txt'


rsrcmgr = PDFResourceManager()
rettxt = StringIO()
laparams = LAParams()
# 縦書き文字を横並びで出力する
laparams.detect_vertical = True
device = TextConverter(rsrcmgr, rettxt, codec='utf-8', laparams=laparams)

# 処理するPDFを開く
fp = open(inFileName, 'rb')
interpreter = PDFPageInterpreter(rsrcmgr, device)

# maxpages：ページ指定（0は全ページ）
for page in PDFPage.get_pages(fp, pagenos=None, maxpages=0, password=None,caching=True, check_extractable=True):
    interpreter.process_page(page)

text = rettxt.getvalue()
fp.close()
device.close()
rettxt.close()


# ファイル出力
fout = codecs.open(outFileName, 'w', 'utf-8')
fout.write(text)
fout.close()



