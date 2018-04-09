# 位运算符 &位与，|位或，^异或(对应的二进位相异时，结果为1)，~取反，<<左移，>>右移
a = 60
b = 13
print(a&b,"   00001100")
print(a|b,"   00111101")
print(a^b,"   00110001")
print(~a,"   11000011")
print(a<<2,"   11110000")
print(b>>2,"   00000011")
# 逻辑运算符 (逻辑运算时，0不等同False)
x = False; y = 20
# and:布尔“与”,x and y,如果x为False,x and y返回False,否则返回y的值。
print(x and y)
# or:布尔“或”,x or y,如果x是True,返回x的值,否则返回y的值。
print(x or y)
# not:布尔“非”,not x,如果x是True,返回False。如果x为False,返回True。
print(not x)
# 成员运算符
	# in:如果在指定的序列中找到值返回True，否则返回False。
	# not in:如果在指定的序列中没有找到值返回True，否则返回False。
order1 = 10
order2 = 11
numberList = [2,5,7,9,10,15]
if(order1 in numberList):
	print("order1存在于列表numberList中")
if(order2 not in numberList):
	print("order2不存在列表numberList中")
# 身份运算符：用于比较两个对象的存储单元
	# is判断两个标识符是不是引用自同一个对象
	# is not判断两个标识符是不是引用自不同对象
# id()函数用于获取对象内存地址
a = 20
b = 20
if(a is b):
	print("a和b有相同的标识")
else:
	print("a和b没有相同的标识")
if(id(a) == id(b)):
	print("a和b有相同的标识")
else:
	print("a和b没有相同的标识")
# is与==的区别：is用于判断两个变量引用对象是否为同一个，==用于判断引用变量的值是否相等。
