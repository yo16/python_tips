# -*- coding: utf-8 -*-

# 外部モジュールを使用する
# asをつけないと認識してくれない
# ファイル名は日本語でも大丈夫
import モジュール分割_外 as mm
import AnotherDir.モジュール分割_外2 as mm2

print('start')

mm.myFunc1()

mm2.myFunc2()


# PathDirへモジュールのパスを通してから呼ぶ

import モジュール分割_外3 as mm3
mm3.myFunc3()


print('end')


