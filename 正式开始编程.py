a, b = 0, 1
while b < 10:
	print("a=%d, b=%d"%(a, b))
	a, b = b, a+b
'''
1.每个条件后面要使用冒号(:)，表示接下来是满足条件后要执行的语句块。
2.使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3.在Python中没有switch-case语句。
'''
# CTRL+C可以退出当前的无限循环
num = int(input("请输入一个数字："))
print("输入的数字是：%d"%(num))
# while...else...在条件语句为false时执行else的语句块。
# range()函数生成数列。range(5)即0，1，2，3，4。range(5,9)即5，6，7，8。range(0,10,3),3为步长。
# pass语句是空语句，是为了保持结构的完整性。pass不做任何事情，一般用做占位语句。
# 迭代器，两个基本方法：iter()生成迭代器对象，next()输出迭代器的下一个对象。
# 生成器，使用了yield的函数被称为生成器(generator)。生成器是一个返回迭代器的函数，简单点理解生成器就是一个迭代器。
	# 在执行过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行。
import sys
def fibonacci(n):
	a,b,counter = 0,1,0
	while True:
		if(counter>n):
			return
		yield a
		a,b = b,a+b
		counter += 1
f = fibonacci(10)
# while True:
try:
	print(next(f))
except StopIteration:
	sys.exit()
# 定义一个函数
'''
1.函数代码块以def关键字开头，后接函数标识符名称和圆括号()。
2.任何传入参数和自变量必须放在圆括号中间，圆括号之间用于定义参数。
3.函数的第一行语句可以选择性的使用文档字符串用于存放函数说明。
4.函数内容以冒号启始，并且缩进。
5.return[表达式]结束函数，选择性的返回一个值给调用方。不带return表达式的相当于返回None。
'''
# 参数分为：必需参数，关键字参数，默认参数，不定长参数
# 不定长参数：加了星号(*)的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，他就是一个空元组。
def test(arg1, *arg2):
	print(arg1)
	for i in arg2:
		print(i)
test(10)
test(11, 12, 13)
# 匿名函数：使用lambda创建匿名函数。
sum = lambda a,b:a+b;
print(sum(10,20))