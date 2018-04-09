# python中变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 同时为多个变量赋值
a = b = c = 1	#a,b,c被分配到相同的内存空间上。
# 一条语句赋值多个变量
a, b, c = 1, 2, "runoob"
# 查看变量类型
print(type(a), type(b), type(c))
#input('按下Enter即可退出')
# 此外还可用isinstance来判断
isinstance(a,int) #测试没反应
# True的值是1，False的值是0，所以True和False可以与数字相加
print(True+3, False+4, True*4)
# del语句删除单个或多个对象
del a, b
# 数值的除法(/)总是返回一个浮点数，要获取整数使用//操作符
print(10/3)
print(10//3)
# 乘方，例2的5次方
print(2**5)
# 混合运算时，python会把整型转换成浮点型
# python支持复数，可以用a+bj或者complex(a,b)表示，a和b都是浮点数
# 字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
# 字符串不能被改变
# List写在方括号([])之间，用逗号分隔开的元素列表，列表内元素类型可以不一致，列表内的元素是可以改变的。
# Tuple元组与List相似，但是Tuple内元素不能被改变，且元组写在小括号里，元素之间用逗号隔开。
'''
set集合是一个无序且不重复元素的序列。
1.基本功能是进行成员关系测试和删除重复函数。
2.可以使用大括号或者set()函数创建。
3.创建空集合时必须用set()，因为{}是创建空字典。
'''
a = set('abracadabra')
b = set('alacazam')
print(a-b)	#差集
print(a|b)	#并集
print(a&b)	#交集
print(a^b)	#不同时存在的元素
# Dictionary对象是一种映射类型，用{}标识，在字典中，key必须是唯一的。无序，元素可以是不同类型。
tinydict = {'name':'runoob', 'code':1, 'site':'runoob.com'}
print(tinydict.keys())
print(tinydict.values())
tinydict.clear()
print(tinydict.keys())
# 数据类型转换，只需要将类型名作为函数名，待转换对象作为参数即可。返回一个新的对象，表示转换的值。
