# class A:
#     def __init__(self):
#         print("A")
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B")
#
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print("C")
#
# class D(B, C):
#     pass
#
# D()

#多类继承
# class Aquatic_animals:
#     foot = 4
#     def get_foot(self):
#         print(self.foot)
#     def live(self):
#         print("生活在水里")
# class Terrestrial_animals:
#     foot = 0
#     def get_foot(self):
#         print(self.foot)
#     def living(self):
#         print("生活在陆地")
# class Frog(Aquatic_animals,Terrestrial_animals):
#     foot = Terrestrial_animals.foot
#     get_foot = Terrestrial_animals.get_foot
#
# frog = Frog()
# frog.live()
# frog.living()
# frog.get_foot()

# __mro__:显示方法解析顺序
# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass
# print(C.__mro__)

#class Parent:
#     def __init__(self):
#         self.value = 10
# class Child(Parent):
#     def get_value(self):
#         return self.value
# c = Child()
# print(c.get_value())

# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.r = radius
#
#     def area(self):
#         self.area = math.pi * self.r ** 2
#         return self.area
#
#     def perimeter(self):
#         self.perimeter = 2 * math.pi * self.r
#         return self.perimeter
#
#
# # 输入处理
# r = float(input("请输入圆的半径: "))
#
# # 创建对象并计算
# c = Circle(r)
# print("圆面积: {:.2f}".format(c.area()))
# print("圆周长: {:.2f}".format(c.perimeter()))

# [习题4-6]
# 定义父类person，有类属性name及age，有私有属性__height，有实例方法info，能输出person的name、age及__height信息。
# 子类student类继承person，有类属性grade，有实例方法info，能输出学生的name、age及grade信息。
#
# person类的定义
# class person:
#
#     def __init__(self, n, a, h):
#         self.name = n
#         self.age = a
#         self.__height = h
#
#     def info(self):
#         print(self.name)
#         print(self.age)
#         print(self.__height)
#
# # student类的定义
# class student(person):
#
#     def __init__(self, n, a, h, g):
#         super().__init__(n, a, h)   #通过继承并访问父类方法间接访问父类私有属性
#         self.grade = g
#
#     def info(self):
#         print("该生信息为: {}的年龄是{}岁，就读于{}年级。".format(self.name, self.age, self.grade))
#
#
# # 用户输入部分
# name = input()  # 请输入姓名：
# age = int(input())  # "请输入年龄："
# height = int(input())  # "请输入身高（厘米）："
# grade = int(input())  # "请输入年级："
#
# s = student(name, age, height, grade)
# s.info()

