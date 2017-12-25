# coding: utf-8

# ファイルの更新を確認
# 2017 (c) yo16
# 参考 https://qiita.com/ksato9700/items/ea4b769d010e8cf1fb0c

import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyHandler(PatternMatchingEventHandler):
    def __init__(self, command, patterns):
        super(MyHandler, self).__init__(patterns=patterns)
        self.command = command

    def _run_command(self):
        # モジュール、引数1、引数2・・・のリストが引数
        subprocess.call(self.command.split())
        return 0

    def on_moved(self, event):
        isdir = 'F'
        if event.is_directory:
            isdir = 'D'
        print("moved!["+isdir+"] "+ event.src_path + '=>' + event.dest_path)
        self._run_command()

    def on_created(self, event):
        isdir = 'F'
        if event.is_directory:
            isdir = 'D'
        print("created!["+isdir+"] "+ event.src_path)
        self._run_command()

    def on_deleted(self, event):
        isdir = 'F'
        if event.is_directory:
            isdir = 'D'
        print("deleted!["+isdir+"] "+ event.src_path)
        self._run_command()

    def on_modified(self, event):
        isdir = 'F'
        if event.is_directory:
            isdir = 'D'
        print("modified!["+isdir+"] "+ event.src_path)
        self._run_command()


def watch(path, command, extension):
    event_handler = MyHandler(command, ["*"+extension])
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("start watching! [" + path + "]")
    try:
        n = 10		# n秒ごとに終了を確認。
        while True:
            time.sleep(n)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    if 4 > len(sys.argv):
        print("Usage:", sys.argv[0], "dir_to_watch command extension")
    else:
        watch(sys.argv[1], sys.argv[2], sys.argv[3])


