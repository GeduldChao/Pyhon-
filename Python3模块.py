# 每个模块都有一个__name__属性，当其值为'__main__'时，表明该模块自身在运行，否则是被引入。__是双下划线。
# 内置函数dir(modulename)可以找到模块内定义的所有名称。以一个字符串列表的形式返回。如果nodulename为空，则返回当前定义的所有名称。
# __init__.py
# from XXX import * *读取的是__all__.py文件中的子模块，没有该文件则不加载子模块。
# __all__.py 包含代码： __all__ = ["echo", "surround", "reverse"] each,surround和reverse是子模块。

# 输入和输出
# 转成字符串函数 str()和repr()
	# str()函数返回一个用户易读的表达方式。
	# repr()产生一个解释器易读的表达方式。
s = "Hello, World!\n"
print(str(s))
print(repr(s))
# rjust() ljust() center() zfill()
print(s.ljust(10))

# 读写文件
# 打开一个文件
f = open("foo.txt", 'w')
f.write("我正在学习Python，爽歪歪！")
f.close()
f = open("foo.txt", 'a')
f.write("\n添加一句：哈哈哈！")
f.write("\n再添加一句：喂喂喂！")
# num = f.write("\n再添加一句：喂喂喂！") # num是写入的字符数。
f.close()
f = open("foo.txt", 'r')
# str = f.read()
# print(str)
str = f.readline() # 从文件中读取单独的一行。
print(str)
# str = f.readlines() # 返回文件中包含的所有行。
# print(str)
f.close()
# 如果写入一些不是字符串的东西，那么将需要先进行转换。
# f.tell()返回文件对象当前所处的位置，它是从文件开头开始算起的字节数。
f = open("foo.txt")
print("tell函数：%d"%(f.tell()))
f.close()
# f.seek()改变文件当前的位置，可以使用f.seek(offset, from_what)函数。
	# seek(x, 0):从文件起始位置开始移动x个字符。
	# seek(x, 1):从当前位置往后移动x个字符。
	# seek(-x, 2):从文件结尾往前移动x的字符。
# 当处理一个文件对象时，使用with关键字是非常好的方式。在结束时，它会帮你正确的关闭文件。(不太理解)
with open("foo.txt", 'r') as f:
	data = f.read()
f.close()

import pickle
# 使用pickle模块将数据对象保存到文件
data1 = {'a':[1,2.0,4+6j],'b':('string',u'Unicode string'),'c':None}
selfref_list = [1,2,3]
selfref_list.append(selfref_list)
output = open('data.pkl','wb')
pickle.dump(data1,output)
pickle.dump(selfref_list,output,-1)
output.close()

import pprint, pickle
pkl_file = open("data.pkl",'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()