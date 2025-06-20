# 二次方程求解
#
# class Equation:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def getDiscriminant1(self):  # 判别式
#         self.getDiscriminant1 = self.b**2-(4*self.a*self.c)
#         return self.getDiscriminant1
#
#     def getRoot1(self):
#         if self.getDiscriminant1>=0:
#             self.getRoot1 = (-1*self.b+(self.getDiscriminant1)**0.5)/2*self.a
#             return self.getRoot1
#         else:
#             return 0
#
#     def getRoot2(self):
#         if self.getDiscriminant1>=0:
#             self.getRoot2 = (-1*self.b+(self.getDiscriminant1)**0.5)/2*self.a
#             return self.getRoot2
#         else:
#             return 0
#
# if __name__ == "__main__":
#     # 输入
#     a = eval(input())
#     b = eval(input())
#     c = eval(input())
#     equation = Equation(a, b, c)
#
#     # 输出
#     print(f"判别式： {equation.getDiscriminant1()}")
#     print(f"根1： {equation.getRoot1()}")
#     print(f"根2： {equation.getRoot2()}")

#定义矩形类
#
# class Rectangle:
#     def __init__(self, breadth, length):
#         self.breadth = breadth
#         self.length = length
#
#     def area(self):
#         self.area = self.breadth * self.length
#         return self.area
#
#
# # 输入处理
# b = float(input())
# l = float(input())
#
# # 创建对象并计算
# obj = Rectangle(b, l)
# print("{:.2f}".format(obj.area()))

# class Animal:
#     def eat(self):
#         print("Animals have to eat food")
#
# class Cat(Animal):
#     def eat(self):
#         print("Cats have to eat food")
#
# obj = Cat()
# obj.eat()

# class Animal:
#     def sound(self):
#         print("Animal sound")
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
#
# a = Animal()
# d = Dog()
# a.sound()
# d.sound()