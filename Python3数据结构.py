# 列表：列表可以修改，而字符串和元组不能。
	# list.append(x) == a[len(a):]=[x] 把一个元素x添加到列表的结尾。
	# list.extend(L) == a[len(a):] = L
	# list.insert(i, x)
	# list.remove(x)
	# list.pop([i]) []表示可选，即[]内参数可有可无。
	# list.clear() == del a[:]
	# list.index(x)
	# list.count(x)
	# list.sort()
	# list.reverse()
	# list.copy() == a[:]
a = [66.25, 333, 333, 1, 1234.5]
b = [44, 55, 66, 77, 88]
a.append(100)
a.extend(b)
a.insert(0, 99)
a.remove(333)
a.sort()
# print("pop:%d "%a.pop())
# for i in a:
	# print(i)
# 列表当作栈使用
# 列表当作队列使用 
'''
	from collections import deque
	queue = deque([11,11,11,12])
	print(queue.popleft())
'''
# 列表推导式 
vec = [2, 4, 6]
fruit = [' apple ', ' banana']
list = [3*x for x in vec]
list = [3*x for x in vec if x>3]
list = [f.strip() for f in fruit]
# for x in list:
	# print(x)
# 嵌套列表
matrix = [[1,2,3,4],[4,6,7,8],[9,10,11,12]] # 矩阵
list = [[row[i] for row in matrix] for i in range(4)]
# for i in list:
	# print(i)
# 元组定义时括号可有可无，但是输出时有括号，定义时括号通常是必须的。
# 集合：关系测试，消除重复元素（所以将一些序列转为集合后可以消除重复元素）。
# 字典：构造函数dict()直接从键值对元组列表中构建字典。
# dict = dict((("sape",4139),("guido",4111)))
# dict = {x: x**2 for x in (1,2,3)} # 推导式
# dict = dict(sun=1, moon=2) # 关键字
# print(dict)
# 在字典中遍历时。关键字和对应的值可以使用items()方法同时解读出来。
# 在序列中遍历时，索引位置和对应的值可以使用enumerate()函数同时得到。
# for i,v in enumerate(vec):
	# print(i,v)
# 同时遍历两个或更多的序列，可以使用zip()组合。
key = ["name","age"]
value = ["sb",18]
for k,v in zip(key,value):
	print("属性：{0}: {1}".format(k,v))
# 要反向遍历一个序列，首先指定这个序列，然后调用reverced()函数。
# 要按顺序遍历一个序列，使用sorted()函数返回一个已经排序的序列，并不修改原值。