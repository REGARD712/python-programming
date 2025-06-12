# 旋转字符串
# def rotateString(s, goal):
#     if len(s) != len(goal):
#         return False
#     return goal in (s + s)
#
# print(rotateString("abcde", "cdeab"))
# print(rotateString("abcde", "cdefg"))

# 判断字符串前缀数
# def countprefixes(words: list, s: str):
#     count = 0
#     for word in words:
#         if s.startswith(word):
#             count += 1
#     return count
#
# print(countprefixes(['a','b','c','ab','bc','abc'], "abc"))

# 实现文件查找工具：
# 输入要查找的路径，再输入要搜索的文件名
# 自动地在指定的路径中查找
# import os  #标准库
# inputPath = input('请输入要查找的路径：')
# patter = input('请输入要搜索的文件名：')
#
# # 只需要简单的使用循环，就可以完成递归遍历
# for dirpath, _, filenames in os.walk(inputPath):
#     for f in filenames:
#         if pattern in f:
#             print(f"{dirpath}/{f}")

# for i in range(100,1000):
#     thesum = 0
#     num = i
#     while num!=0:
#         thesum += (num%10)**3
#         num //= 10
#     if i==thesum:
#         print(i,end=' ')

# s = ""
# for i in range(100,1000):
#     a =i//100
#     b =i//10%10
#     c =i%10
#     if a**3+b**3+c**3==i:
#         s = s + str(i) + ","
# print(s[:-1])