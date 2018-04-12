# _*_ coding:utf-8 _*_

from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser();

parser.add_argument('file')	#输入文件
parser.add_argument('-o', '--output')	#输出文件
parser.add_argument('--width', type=int, default=80)	#输出字符画宽
parser.add_argument('--height', type=int, default=80)	#输出字符画高

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
	if(alpha==0):
		return ' '
	length = len(ascii_char)
	print(length)
	gray = int(0.2126*r + 0.7152*g + 0.0722*b)
	
	unit = (256 + 1)/length
	return ascii_char[int(gray/unit)]
	
if __name__ == '__main__':
	img = Image.open(IMG)
	img = img.resize((WIDTH,HEIGHT), Image.NEAREST)
	txt = ""
	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*img.getpixel((j,i)))
		txt += '\n'
	print(txt)

#输出字符画到文件
	if OUTPUT:
		with open(OUTPUT, 'w') as file:
			file.write(txt)
	else:
		with open('小聪明蛋.txt', 'w') as file:
			file.write(txt)