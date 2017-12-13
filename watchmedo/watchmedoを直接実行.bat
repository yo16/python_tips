@echo off


set PATH=%PATH%;C:\Program Files\Python36;C:\Program Files\Python36\Scripts


rem watchdog‚Ì•t˜^‚Ìwatchmedo‚ğ’¼ÚŒÄ‚Ño‚·
watchmedo shell-command --recursive --patterns "*.txt;" --command "echo ${watch_event_type} :: ${watch_src_path}" "test01"

pause
