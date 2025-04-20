输入一个十六进制数，输出对应的十进制数
num = int(input(),16)
print(num)

能够统计字符串长度函数：len()
s = input()
print(len(s))

格式化输出字符串
.lower() --- 全部小写
.upper() --- 全部大写
.title() --- 各个字符的首字母大写
.capitalize() --- 首字母大写
例：
name = input()
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
——————————————————————————————————————————
.strip() --- 删除两边空格
.lstrip() --- 删除左边空格
.rstrip() --- 删除右边空格
.replace(" "," ") --- 删除所有空格
.split() --- 先切分，" ".join() --- 再拼接
例：
a = input()
print(a.strip())    # 删除两边空格
print(a.lstrip())   # 删除左边空格
print(a.rstrip())   # 删除右边空格
print(a.replace(' ',""))    # 删除所有空格
x = a.split()  # 切片
print(x)
print("".join((x[0],x[1])))

重复输出字符串：str * 次数
————————————————————————————————————————————————————————————————————————————————
例：
name = input()
print(name * 5)

截取字符串
————————————————————————————————————————————————————————————————————————————————————————————————————
strname[start : end : step]
对各个部分的说明：
strname：要截取的字符串；
start：表示要截取的第一个字符所在的索引（截取时包含该字符）。
如果不指定，默认为 0，也就是从字符串的开头截取；
end：表示要截取的最后一个字符所在的索引（截取时不包含该字符）。
如果不指定，默认为字符串的长度；
step：指的是从 start 索引处的字符开始，
每 step 个距离获取一个字符，直至 end 索引出的字符。
step 默认值为 1，当省略该值时，最后一个冒号也可以省略。
例：
name = input()
print(name[0:10])

列表及其元素的替换
————————————————————————————————————————————————————————————————————————————————————————————————————
offer_list = ['Allen','Tom']    # 创建列表
# 利用循环依次发送信息
for i in offer_list:
    print('%s, you have passed our interview and will soon become a member of our company.' % i)
# 替换列表中的‘Tom’
offer_list[1] = 'Andy'
# 再次循环发送信息
for j in offer_list:
    print('%s, welcome to join us!' % j)

———————————————————————————————————————————————————————————————————————————————————————————————————————————
字符串常用函数：
text="only YOU Loving yoU,你是我的唯一，jUst YoU,我能等你下课吗？能不能一起去逛街？达能小王子"

#大小写转换
text.upper() #大写
text.lower() #小写
text.title()#首字母大写
text.capitalize()#第一个字母大写
text.swapcase()#大小写对调

#字符串的搜索
text.count("o")#搜索并统计"o"出现的次数
text.count("o",28)#搜索并统计，从第28位开始，"o"出现的次数
text.startswith("only")#text以"only"开通
text.startswith("only",2,10)#text的第3-9个字符以"only"开通
text.find("you")#查找you
text.replace("u","V",2)

#填充或者剔除某些信息

"1999".rjust(10,"$")#前一个字符代表填充后字符串的总长度
"1999".rjust(5,"$")
"1999".zfill(9)#用0填充，类似 "1999".rjust(9,"0")
"1999".rjust(9,"0")
"1999".center(50) #在左右两边都假设空格
"   1999   ".strip()#去重左右两边的空格
"1999".strip("9")#去重左右两边的"9"
" 1999 ".strip("9")#去重左右两边的"9",两边是空格没有9

#字符串的分割与合并

text.replace("能",",")
text1=text.replace("能","\n")
print(text1)
print(text.replace("能","\n"))
text.split("能")#以"能"为结点把str拆成一个字列表
text.partition("能") #以"能"为结点把str拆成一个字元组
text.rpartition("能")
text1.splitlines()#识别空行进行分割
text1.split("\n")#同上分割空行
"@".join(text)#把@插入到str的每一个字符中
"12345".join("  ")#重复并拼接





