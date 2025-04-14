# 凯撒密码
'''
字母表的对应关系如下：
原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
对于原文字符 P，其密文字符 C满足如下条件：C=(P+3) mod 26
上述是凯撒密码的加密方法，解密方法反之，即：P=(C-3) mod 26

假设用户可能使用的输入包含大小写字母a~zA~Z、空格和特殊符号，
请编写一个程序，对输入字符串进行恺撒密码加密，直接输出结果，其中空格不用进行加密处理。
使用input()获得输入。
'''
# s = input().strip()
# encrypted = []
# for char in s:
#     if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
#         base = ord('A') if char.isupper() else ord('a')
#         shifted = (ord(char) - base + 3) % 26
#         encrypted_char = chr(shifted + base)
#         encrypted.append(encrypted_char)
#     else:
#         encrypted.append(char)
# print(''.join(encrypted))
#
# 平方根格式化
'''
获得用户输入的一个整数a，计算a的平方根，保留小数点后3位，并打印输出。
输出结果采用宽度30个字符、右对齐输出、多余字符采用加号(+)填充。
如果结果超过30个字符，则以结果宽度为准。
'''
# import math
# import cmath
#
# a = int(input())
# if a >= 0:
#     sqrt_a = math.sqrt(a)
#     print(f"{sqrt_a:+>30.3f}")
# else:
#     c = cmath.sqrt(a)
#     real_str = f"{c.real:.3f}"
#     imag_str = f"{c.imag:+.3f}j"
#     combined = real_str + imag_str
#     print(f"{combined:+>30}")
#
# 字符串分段组合
'''
获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。
'''
# s = input()
# parts = s.split('-')
# if len(parts) >= 2:
#     print(f'{parts[0]}+{parts[-1]}')
# else:
#     print(s)
#
# 无空隙回声输出
'''
获得用户输入，去掉其中全部空格，将其他字符按收入顺序打印输出。
'''
# s = input()
# o = s.replace(" ","")
# print(o)
#
# 浮点数判断
'''
s="9e10"是一个字符串，
编写程序判断s是否是浮点数形式字符串，即包含小数点或采用科学计数法形式表示。
如果是则输出True，否则输出False。
'''
# s = "9e10"
# if type(eval(s)) == float:
#     print(True)
# else:
#     print(False)
#
# 字符串格式化输出
'''
获得用户的输入当作填充符号，以30字符宽居中输出PYTHON字符串。
'''
# a = input("")
# s = "PYTHON"
# print("{0:{1}^30}".format(s,a))
#
# 字符串输出格式宽度
'''
获得用户的输入当作宽度，以*作为填充符号右对齐输出PYTHON字符串。
'''
# w = input()
# s = "PYTHON"
# print("{0:*>{1}}".format(s,w))
#
# 强制输出10个字符
'''
获得用户输入，无论输入内容多少，以30字符宽度居中输出其中最多前10个字符，
如果不足10个字符，则全部输出。
'''
# s = input()
# print("{:^30.10}".format(s))






