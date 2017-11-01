# -*- coding:utf-8 -*-

from PIL import ImageGrab

def main():
	img = ImageGrab.grab((0,0,500,500))
	img.save(".\img\PrintSreenTest.png")

if __name__ == "__main__":
	main()
