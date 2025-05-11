# def calcsum(begin,end):
#     thesum = 0
#     for i in range(begin,end+1):
#         thesum += i
#     print(thesum)

# def EvenOdd(num):
#     if num % 2 == 0:
#         return 1    # 偶数
#     else:
#         return 0    # 奇数
#
# for i in range(10, 21):
#     if EvenOdd(i) == 1:
#         print(f"{i}是偶数")
#     else:
#         print(f"{i}是奇数")

# 牛客题目
# 二进制位运算
# x,y = map(int,input().split())
# r1 = x & y
# r2 = x | y
# print(r1,r2)

# 列表
# a = [1, 2, 3, 4]
# print(a)

# 列表与元组的区别：列表可以修改，元组不可修改

# 可以在列表里放不同类型的变量
# b = [12, 'Hello', True, [2, 3, 4]]
# print(b)

# 列表的访问下表操作
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a[2])
# a[2] = 20   # 列表元素的修改
# print(a[2])

# 使用内置函数 len() 获取列表的长度，与字符串一样
# a = [1, 2, 3, 4, 5]
# print(len(a))

#   a[-1] == a[len(a) - 1]

# 切片操作：取出连续的元素
# a = [1, 2, 3, 4, 5]
# print(a[1:3])   # 表示打印的元素范围为下标是1~2的元素(前闭后开区间)

# 列表的切片操作可以省略前后边界：
# a = [1, 2, 3, 4, 5]
# print(a[:4])    # 省略了前边界，表示从列表第一个元素开始获取
# print(a[2:])    # 省略了后边界，表示从下标为2元素开始一直获取直到列表末尾
# print(a[:])     # 前后均省略，表示获取整个列表

# 切片操作还可以指定 "步长" , 也就是 "每访问一个元素后, 下标自增几步"
# a = [1,2,3,4,5,6,7,8,9,10]
# print(a[::])
# print(a[::2])
# print(a[::5])

# 切片操作指定的步长还可以是负数, 此时是从后往前进行取元素. 表示 "每访问一个元素之后, 下标自减几步"
# a = [1,2,3,4,5,6,7,8,9,10]
# print(a[::-1])
# print(a[::-2])
# print(a[::-5])

# 如果切片中填写的数字越界了, 不会有负面效果. 只会尽可能的把满足条件的元素过去到
# alist = [1, 2, 3, 4]
# print(alist[100:200])

# 列表元素的遍历

# for循环
# a = [1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     print(i)

# a = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0, len(a)):      # 使用for按照长度生成下标，然后访问列表元素
#     print(a[i])

# while循环
# a = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# 向列表中增加元素：append() 、 insert()

# append()方法： 向列表末尾插入一个元素(尾插)
# a = [1,2,3,4,5]
# print(a)
# a.append('Hello')
# print(a)

# insert()方法： 向任意位置插入一个元素，第一个参数表示要插入位置的下标
# a = [1,2,3,4,5]
# print(a)
# a.insert(1,'Hello')
# print(a)

# 使用 in 操作符可以查找某元素是否存在列表中，返回值是布尔类型
# a = [1,2,3,4,5,6]
# print(2 in a)
# print(10 in a)

# 使用 index()方法可以查找元素在列表中的下标，返回值为整数
# a = [1,2,3,4,5]
# print(a.index(2))
# print(a.index(5))

# 删除元素：pop() 、 remove()

# pop()方法：括号内不填则默认删除列表最末尾的元素；括号内填下标则可以按照下标删除元素
# a = [1,2,3,4,5,6,7,8,9,10]
# print(a)
# a.pop()
# print(a)
# a = [1,2,3,4,5,6,7,8,9,10]
# print(a)
# a.pop(4)
# print(a)

# remove()方法：按照值删除元素
# a = [1,2,3,4,5,6,7,8,9,10]
# print(a)
# a.remove(3)
# print(a)

# 链接列表：使用操作符 + 可以将两个列表连接起来
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# print(a + b)    # 操作符 + 会创建一个新列表来存储 a、b 两个列表的数据

# 使用 extend()方法：a.extend(b)——>把 b拼接到 a后面，只会改变被拼接列表
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# print(a)
# print(b)
# a.extend(b)
# print(a)
# print(b)

# 元组tuple()在Python中是默认的集合类型
