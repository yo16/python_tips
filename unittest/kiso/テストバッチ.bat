python -d -m unittest tests.test_sample

rem 全部正常だと、0が返る
rem 一部でも異常だと、1が返る
ECHO %ERRORLEVEL%

pause
