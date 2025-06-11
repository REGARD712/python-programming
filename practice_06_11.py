# a,b,c,d = 10,20,"alice",True
# print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}")

a = 12.573502
# print("a = {:.2f}".format(a))
# print(f"a = {a}")
# print("a = %.2f"%a)

# print(eval("1" + "1"))

# import turtle as t
# # t.pensize(2)
# # for i in range(8):
# #     t.fd(150)
# #     t.left(135)
# t. pensize(5)
# for i in range(1,5):
#     t.fd(100)
#     t.left(90)
# t.penup()
# t.goto(150,150)
# t.pendown()
# t.seth(270)  # 更换朝向
# # t.goto(0,0)
# t.circle(10)
# t.done()

# import turtle as t
# color = ['red','green','blue']
# rs = [10,30,60]
#
# for i in range(3):
#     t.penup()
#     t.goto(0,0)
#     t.pendown()
#     t.pencolor(color[i])
#     t.circle(rs[i])
# t.done()

# 鸡兔同笼
# h,f = map(int,input().split())
#
# n = int((f-2*h)/2)
# m = int(h-n)
#
# if m>=0 and n>=0 :
#     print("有{}只鸡，{}只兔".format(m,n))
# else:
#     print("Data Error!")

# 物不知数
# n = int(input())
#
# if n>0 and n<=1000:
#     flag = 0
#     for i in range(n+1):
#         if i%3==2 and i%5==3 and i%7==2:
#             flag = 1
#             print(i)
#     if flag == 0:
#         print("No solution!")