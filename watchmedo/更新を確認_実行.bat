@echo off


set PATH=%PATH%;C:\Program Files\Python36;C:\Program Files\Python36\Scripts

rem watchdog���W���[�����Ăяo��python�X�N���v�g
rem echo �̓��W���[�����Ȃ��̂ŌĂяo���Ȃ�!
rem python �X�V���m�F.py "test01" "echo aa" "*.txt"

python �X�V���m�F.py "test01" "python testprint.py" "*"


pause

