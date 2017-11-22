set PY="C:\Program Files\Python34\python.exe"

%PY% 終了コード123.py
ECHO %ERRORLEVEL%

%PY% 終了コードなし.py
ECHO %ERRORLEVEL%

%PY% 終了コード文字列.py
ECHO %ERRORLEVEL%

PAUSE


