"""运算符重载"""
# class Calculator:
#     def __init__(self, num):
#         self.number = num
#     def __add__(self, num2):  # 加法
#         return self.number + num2
#     def __sub__(self, num3):  # 减法
#         return self.number - num3
#     def __mul__(self, num4):  # 乘法
#         return self.number * num4
#     def __mod__(self, num5):  # 取模
#         return self.number % num5
#     def __pow__(self, num6):  # 幂指
#         return self.number ** num6
#     def __truediv__(self, num7):  # 浮点数除法
#         return self.number / num7
#     def __floordiv__(self, num8):  # 整数除法
#         return self.number // num8
#     def __radd__(self, num9):  # 加法
#         return num9 + self.number
#     def __and__(self, num10):  # 位与运算
#         return self.number and num10
#     def __or__(self, num11):  # 位或运算
#         return self.number or num11
#
# c = Calculator(100)
# print(c+1)
# print(c-2)
# print(c*3)
# print(c%4)
# print(c**5)
# print(c/6)
# print(c//7)
# print(c+8)
# print(c and 9)
# print(c or 10)

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
# v1 = Vector(1,2)
# v2 = Vector(2,3)
# v3 = v1 + v2