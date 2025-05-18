# 1.找出 100以内的偶数

# 直接打印
# for num in range(100):
#     if num % 2 == 0:
#         print(num)

# 以列表的形式打印
# num_print = []
# for num in range(100):
#     if num % 2 == 0:
#         num_print.append(num)
# print(num_print)

# 2.判断素数

# num = eval(input("请输入一个整数："))
# flag = 1
# for i in range(2, num):
#     if num % i == 0:
#         flag = 0      # 表示该数不是素数
#         break
# if flag == 1:
#     print(f"{num}是素数")
# else:
#     print(f"{num}不是素数")

# 3.求阶乘

# num = eval(input("请输入一个整数："))
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# print(f"{num}! = {fact}")

# 4.求圆的周长的面积

# 1.
# r = eval(input("请输入半径："))
# pi = 3.1415926
#
# # 2*pi*r, pi*r**2
# c = 2*pi*r
# a = pi*r**2
# print(f"圆的周长是：{c}，面积是：{a}")

# 2.
# import math
# r = eval(input("请输入半径："))
# c = 2*math.pi*r
# a = math.pi*r**2
# print(f"圆的周长是：{c}，面积是：{a}")

# 5.求直角三角形斜边长

# a, b = map(eval, input("请输入两个直角边：").split())
# c = (a**2 + b**2)**0.5
# print(f"斜边长是：{c}")
