# 定义People类
class People:
	name = ''
	age = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def Intrduct(self):
		print("姓名：%s，年龄：%d"%(self.name, self.age))
p = People('Paul', 23)
p.Intrduct()
# 继承
class Student(People):
	grade = 0
	def __init__(self, name, age, grade):
		People.__init__(self, name, age)
		self.grade = grade
	def Intrduct(self):
		print("姓名：%s，年龄：%d，年级：%d"%(self.name, self.age, self.grade))
s = Student('Paul', 18, 12)
s.Intrduct()
# 多继承
	# 1.若父类中有相同的方法名，而在子类使用时未指定，python从左往右搜索。即当前类中未定义该方法，则在父类中从左往右查找，直至找到为止。
class Composition:
	title = ''
	def __init__(self, title):
		self.title = title
class Writer(People, Composition):
	def __init__(self, name, age, title):
		People.__init__(self, name, age)
		Composition.__init__(self, title)
	def Intrduct(self):
		print("作家姓名：%s，年龄：%d，文章名：%s"%(self.name, self.age, self.title))
w = Writer('莫言', 55, '红高粱')
w.Intrduct()
# 方法重写
	# super()函数是用于调用父类(超类)的一个方法
class Parent:
	def method(self):
		print("调用父类方法")
class Child(Parent):
	def method(self):
		print("调用子类方法")
c = Child()
c.method()
super(Child, c).method()
# 类属性与方法
	# 私有属性：__private_attrs：两个下划线开头，表明该属性私有，不能在类外部被使用。在类内部使用self.__private_attrs
	# 类方法参数第一个参数必须是self，也可以使用this。
	# 私有方法：__private_method：同样两个下划线开头。
# 类的专有方法
# 运算符重载
class Test:
	a = 0;
	b = 0
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __str__(self):
		return 'Vector(%d, %d)'%(self.a, self.b)
	def __add__(self, other):
		return Test(self.a+other.a, self.b+other.b)
t1 = Test(5, 5)
t2 = Test(6, 6)
print(t1+t2)