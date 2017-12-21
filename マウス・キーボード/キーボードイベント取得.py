# coding: utf-8

# 参考
# https://qiita.com/tortuepin/items/9ede6ca603ddc74f91ba

from msvcrt import getch

def main():
    while True:
        key = ord(getch())
        print(key)
        
        if key == 27: #エスケープ
            break
        elif key == 13: #エンター
            print('enter!')
        
        elif key == 224: #スペシャルキー（矢印、Fキー、ins、del、など）
            key2 = ord(getch())
            print('special-key:'+str(key2))
            if key2 == 80: #上矢印
                print('up!')
            elif key2 == 72: #下矢印
                print('down!')


main()
