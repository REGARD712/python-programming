# class Cat():
#     def __init__(self, name):
#         self.name = name
#     def meow(self):
#         print("Meow~meow~")
#
# c1 = Cat('Judy')
# c1.meow()

class Vector3:
    # 构造方法，初始化，定义向量坐标
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    # 与另一个向量相加，对应分量相加，返回新向量
    def __add__(self, anotherVector):
        self.x = self.x + anotherVector.x
        self.y = self.y + anotherVector.y
        self.z = self.z + anotherVector.z
        return list([self.x,self.y,self.z])

# 从用户输入读取数字和两个向量的分量
x = list(map(int, input().split(',')))
y = list(map(int, input().split(',')))

# 创建两个Vector3实例
vec1 = Vector3(x[0], x[1], x[2])
vec2 = Vector3(y[0], y[1], y[2])

# 执行加法操作
vec_add = vec1 + vec2
print(vec_add)