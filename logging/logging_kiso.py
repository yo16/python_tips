# -*- coding:utf-8 -*-

# loggingの使い方
# https://docs.python.jp/3/howto/logging.html
# https://qiita.com/amedama/items/b856b2f30c2f38665701

# DEBUG		おもに問題を診断するときにのみ関心があるような、詳細な情報。
# INFO		想定された通りのことが起こったことの確認。
# WARNING	想定外のことが起こった、または問題が近く起こりそうである (例えば、'disk space low') ことの表示。
# ERROR		より重大な問題により、ソフトウェアがある機能を実行できないこと。
# CRITICAL	プログラム自体が実行を続けられないことを表す、重大なエラー。
# デフォルトはWARNING


# おまじない的に下記を書く！
from logging import getLogger, StreamHandler, Formatter, DEBUG
global __mylogger
__mylogger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)

# formatter
#formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ミリ秒はasctimeにないので、別にする
formatter = Formatter('%(asctime)s.%(msecs)d|%(levelname)s|%(message)s', '%Y/%m/%d %H:%M:%S')
handler.setFormatter(formatter)

__mylogger.setLevel(DEBUG)
__mylogger.addHandler(handler)
__mylogger.propagate = False



# 使うとき
__mylogger.debug('hello')
# hello


def testProc(num1,logger=None) :
	# 使うとき２
	logger = logger or __mylogger
	logger.debug('debug ['+str(num1)+']')
	logger.info('info ['+str(num1)+']')
	logger.warning('warning ['+str(num1)+']')
	logger.error('error ['+str(num1)+']')
	logger.critical('critical ['+str(num1)+']')
	
	



testProc(1)
