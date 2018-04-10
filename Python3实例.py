# 1.数字求和
'''
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
sum = num1 + num2
print("{0} + {1} = {2}".format(num1, num2, sum))
	# 或者一句话
print("和为%.1f"%(float(input('请输入第一个数：'))+float(input('请输入第二个数：'))))
'''
# 2.求平方根 导入cmath模块
'''
import cmath
num = int(input('请输入一个数：'))
num_sqrt = cmath.sqrt(num)
print("{0}的平方根为：{1:0.3f}+{2:0.3f}j".format(num, num_sqrt.real, num_sqrt.imag))
'''
# 3.生成随机数 导入random模块
'''
import random
print(random.randint(0, 9))
'''
# 4.输出指定范围内的质数(没看太懂)
'''
lower = int(input('请输入区间下限：'))
upper = int(input('请输入区间上限：'))
for num in range(lower, upper+1):
	if(num>1):
		for i in range(2, num):
			if(num%i == 0):
				break
		else:
			print(num)
'''
# 5.九九乘法表
'''
for i in range(1, 10):
	for j in range(1, i+1):
		print('{}x{}={}\t'.format(i,j,i*j), end='')
	print()
'''
# 6.十进制转二进制、八进制、十六进制
'''
dec = int(input("请输入一个数："))
print("二进制：{}".format(bin(dec)))
print("八进制：{}".format(oct(dec)))
print("十六进制：{}".format(hex(dec)))
'''
# 7.ASCII码与字符相互转换
'''
c = input("请输入一个字符：")
a = int(input("请输入一个ASCII码："))
print(c + "的ASCII码是：", ord(c))
print(a, "对应的字符为："+ chr(a))
'''
# 8.简易计算器
'''
def add(a, b):
	return a+b
def subtract(a, b):
	return a-b
def multiply(a, b):
	return a*b
def divide(a, b):
	return a/b
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
operator = int(input("输入你的选择(1/2/3/4)："))
num1 = int(input("输入第一个数："))
num2 = int(input("输入第二个数："))
if(operator == 1):
	print('计算结果是：{}'.format(add(num1, num2)))
if(operator == 2):
	print('计算结果是：{}'.format(subtract(num1, num2)))
if(operator == 3):
	print('计算结果是：{}'.format(multiply(num1, num2)))
if(operator == 4):
	print('计算结果是：{}'.format(divide(num1, num2)))
'''
# 9.生成日历 导入calendar模块
'''
import calendar
yy = int(input("输入年份："))
mm = int(input("输入月份："))
print(calendar.month(yy, mm))
'''
# 10.获取昨天日期 导入datetime模块
'''
import datetime
def getYesterday():
	today = datetime.date.today()
	dayDelta = datetime.timedelta(days=1)
	yesterday = today - dayDelta
	return yesterday
print(getYesterday())
'''