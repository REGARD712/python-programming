# 设计一个水果类 Fruit，要求如下：
#
# 私有属性：
# __color（颜色），通过无参数 input() 交互式输入初始化。
# __city（产地），通过无参数 input() 交互式输入初始化。
# 私有方法：
# __outputColor()：打印 __color 的值。
# __outputCity()：打印 __city 的值。
# 公有方法：
# output()：调用 __outputColor() 和 __outputCity()，分两行输出颜色和产地。
# 静态方法：
# setPrice(p)：设置全局价格 price。
# getPrice()：返回全局价格 price。
# 主程序要求：
# 创建 Fruit 类的对象，调用 output() 方法输出颜色和产地。
# 通过静态方法 setPrice() 设置价格，并调用 getPrice() 输出更新后的价格。
# 所有输入均无提示参数，价格需通过 int(input()) 动态获取。
#
# class Fruit:
#     price = 0
#
#     def __init__(self):
#         self.__color = input()
#         self.__city = input()
#
#     def __outputColor(self):
#         print(self.__color)
#
#     def __outputCity(self):
#         print(self.__city)
#
#     def output(self):
#         self.__outputColor()
#         self.__outputCity()
#
#     @staticmethod
#     def getPrice():
#         return Fruit.price
#
#     @staticmethod
#     def setPrice(p):
#         Fruit.price = p
#
#
# # 交互式操作流程
# apple = Fruit()
# apple.output()
#
# # 动态设置价格
# print(Fruit.getPrice())  # 先显示当前价格
# Fruit.setPrice(int(input()))  # 将输入转为整型设置价格
# print(Fruit.getPrice())  # 显示更新后的价格

