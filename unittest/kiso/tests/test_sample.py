# -*- coding: utf-8 -*-
# http://qiita.com/takus69/items/cde279266b46daf9972d
# http://qiita.com/Go-zen-chu/items/ddfe37c00324b1b8941e

import sys
import unittest
import sample

class TestSample(unittest.TestCase):
	"""メンバ変数"""
	HENSU = 0
	
	"""テストクラスの初期化"""
	@classmethod
	def setUpClass(jibun):
		if sys.flags.debug: print('\n** TestSample initialized !! **')
		jibun.HENSU = 1
	
	"""テストクラスのファイナライズ"""
	@classmethod
	def tearDownClass(jibun):
		if sys.flags.debug: print('\n** TestSample finalized !! **')
		jibun.HENSU = 2
	
	
	"""テストメソッドの開始のたびに呼ばれる"""
	def setUp(self):
		if sys.flags.debug: print('\n-- setup ! --')
	
	"""テストメソッドの終了のたびに呼ばれる"""
	def tearDown(self):
		if sys.flags.debug: print('\n-- finalize ! --')
	
	
	""" テスト名は、testで始まる関数名でないといけない """
	def test_add(self):
		self.assertEqual(sample.add(1,2),3)
	
	def test_add2(self):
		self.assertEqual(sample.add(5,6),12)
	
	def test_add3(self):
		self.assertEqual(sample.add(5,6),11)


"""クラスはいくつかあってよい"""
class Test2Sample(unittest.TestCase):
	def test_add2_2(self):
		self.assertEqual(sample.add(7,8),15)


if __name__ == "__main__":
	unittest.main()
