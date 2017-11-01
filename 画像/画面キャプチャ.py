# -*- coding: utf-8 -*-

from PIL import ImageGrab

def main():
	img = ImageGrab.grab((0,0,400,400))
	img.save(".\img\capture.jpg")
	img.show()

if __name__ == "__main__":
	main()

