print("Hello World!")
# 单行注释
# 多行注释
'''
多行注释
'''
if True:
	print('True')
	print('缩进一致属于同一代码块')
else:
	print("False")
# 语句较长时，使用\实现多行语句。在[],{},()中的多行语句，不需要写\。
a = 1+\
2+\
3
print(a)
print(1+2
	  +3)
# 数字类型 int,float(3E-2),bool,complex(1+2j)
# 三引号(''')可以指定一个多行字符串
s = '''这是一个
多行字符串'''
print(s)
# 转义字符\。但是r可以让\不发生转义。
s = R'hhh\nooo'
print(s)
# +连接字符串，*字符串重复
s = 'aaa'*2
print(s)
# 不存在字符类型，一个字符就是长度为1的字符串。
# 字符串截取 变量[头下标:尾下标]
ss = s[2:4]
print(ss)
# 空行也是程序代码的一部分
# input()方法等待用户输入
input('按下Enter键后退出')
# 同一行中显示多条语句，语句之间用分号(;)隔开
import sys; x="runoob"; sys.stdout.write(x+'\n')
# 代码组
# print默认输出是换行的，如果要实现不换行需要在变量末尾加上end=""
print("换行输出")
print('不换行',end="")
print("输出")
# inport导入整个模块，from...import导入模块中的某一或某几个函数
import sys
print("命令行参数为：")
for i in sys.argv:
	print(i)
print("python路径为：",sys.path)
from sys import argv,path
for i in argv:
	print(i)
print("path: ",path)