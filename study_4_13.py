# 格式化输出

# 希望输出 "a = 5"
# a = 5
# # print("a = " + a)  # python语法不支持：字符串与整型无法拼接
# print(f"a = {a}")    # 正确的格式化输出
# print(f"a = {a + 10}")      # 可进行运算

# 通过控制台输入数据
# num = input('请输入一个整数：')    # input函数有返回值，需要用一个变量接收
# print("您输入的数据是：" + num)
# print(f"您输入的数据是：{num}")
# print(type(num))        # 注意：input函数的返回值是字符串类型

# a = input("请输入第一个整数：")
# b = input("请输入第二个整数：")
# print(f"a + b = {a + b}")
# 仅仅是字符串的拼接，并不是算术运算

# 进行类型转换：str ——> int
# a = int(input("请输入第一个整数："))
# b = int(input("请输入第二个整数："))
# print(f"a + b = {a + b}")

# 例子：输入四个小数，求平均值
# a = float(input("请输入第一个小数："))
# b = float(input("请输入第二个小数："))
# c = float(input("请输入第三个小数："))
# d = float(input("请输入第四个小数："))
# aver = (a + b + c + d) / 4.0
# print(f"四个小数的平均值是：{aver}")

# Python中的运算符：算数、关系、逻辑、赋值

# 注意：除法操作时，除数不能是 0;

# python中，整数除以整数可能会得到小数：1/2==0.5
# print(1/2)

# print(7 % 3)

# ** 乘方运算：及支持整数，也支持小数（开根号）
# print(4 ** 2)   # 表示 4 的 2 次方
# print(4 ** 0.5)     # 表示 4 的 0.5 次方

# // 地板除法：会根据计算的结果向下取整
# print(7 // 2)
# print(-7 // 2)

# a = 10
# a = 'Hello'     # 比较每一个字母的顺序大小
# b = 20
# b = 'World'     # abcdefghijklmnopqrstuvwxyz
#
# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)
# print(a == b)
# print(a != b)

# 对于浮点数来说，使用 == 和 != 来进行比较有一定的风险：
# 因为浮点数在内存中的存储和表示时可能存在误差的，
# 这样的误差在算术运算的时候可能被放大，从而导致 == 出现误判

# print(0.1 + 0.2 == 0.3)
# print(0.1)
# print(0.2)
# print(0.1 + 0.2)        # 得数与 0.3 相差十分接近，但是仍不相等
# print(0.3)

# 正确比较浮点数
# a = 0.1 + 0.2
# b = 0.3
# print(-0.000001 < (a - b) < 0.000001)

# 逻辑操作符
# a = 10
# b = 20
# c = 30
# print(a < b < c)        # 宜采用链式比较方法
# print(a < b and b > c)
#
# print(a > b or b < c)
# print(a < b or b > c)
# print(a > b or b > c)
#
# print(not a < b)
# print(not a > b)

# a = 10
# b = 20
# c = 30
#
# # 短路求值
# print(a > b and 10 / 0 == 1)
# print(a > b or 10 / 10 == 1)
# print(a < b or 10 / 0 == 1)


# 赋值运算符

# a = b =20       # 链式赋值(不建议)

# a , b = 10, 20      # 多元赋值
# print(f"a = {a}, b = {b}")
#
# # 使用多元赋值一步完成互换
# a , b = b , a
# print(f"a = {a}, b = {b}")

# 复合赋值运算

# a = 0
# a = a + 1
# print(a)
#
# a = 0
# a += 1
# print(a)
#
# a = 0
# b = 1
# c = 2
#
# a -= 1
# b *= 2
# c /= 10
# print(a,b,c)

# Python不支持自增自减操作符：++a;a++;--a;a--

# 整数可以与布尔类型进行运算，但是这样的操作没有意义
# a = 10
# b = False
# c = True
# print(a + b)
# print(a + c)

# python中若要使用分号，通常是这种场景：
#a = 10;print(a)












