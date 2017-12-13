@echo off


set PATH=%PATH%;C:\Program Files\Python36;C:\Program Files\Python36\Scripts

rem watchdogモジュールを呼び出すpythonスクリプト
rem echo はモジュールがないので呼び出せない!
rem python 更新を確認.py "test01" "echo aa" "*.txt"

python 更新を確認.py "test01" "python testprint.py" "*"


pause

