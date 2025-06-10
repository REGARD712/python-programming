# 判断素数
# num = eval(input())
# flag = 1  #假定该数是素数
# for i in range(2, num):
#     if num % i == 0:
#         flag = 0  #代表该数不是素数
# if flag == 1:
#     print("该数是素数")
# else:
#     print("该数不是素数")
#

# 打印九九乘法口诀表
# for i in range(1,10):
#     print()
#     for j in range(1,i+1):
#         print("{}*{}={}".format(j,i,i*j), end = " ")

# 输出水仙花数(100-1000内)
# import math
# for i in range(100,1000):
#     thesum = 0
#     num = i
#     while num!=0:
#         thesum += math.pow(num%10, 3)
#         num = num // 10
#     if thesum == i:
#         print(f"{i}")

# 反向输出四位数
# num = eval(input())
# while num!=0:
#     print(f"{num%10}", end=" ")
#     num //= 10

# 判断字母
# value = list(input())
# flag = True
# for i in value:
#     if i>='a' and i<='z' or i>='A' and i<='Z':
#         continue
#     else:
#         flag = False
# if flag == True:
#     print("全是字母")
# else:
#     print("不全是字母")

# 判断三角形
# def Istriangle(a,b,c):  #判断是否为三角形
#     if a+b>c and b+c>a and a+c>b:
#         return 1
#     else:
#         return 0
#
# def main():
#     a,b,c = map(int, input().split())
#     ret = Istriangle(a,b,c)
#     if ret==1:
#         print("是一个三角形")
#     else:
#         print("不是一个三角形")
#
# if __name__ == '__main__':
#     main()
