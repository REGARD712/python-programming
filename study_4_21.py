# 读取输入并分割成体重和身高
weight, height = map(float, input())

# 计算BMI
bmi = weight / (height ** 2)

# 国际BMI分类判断
if bmi < 18.5:
    international = '偏瘦'
elif 18.5 <= bmi < 25:
    international = '正常'
elif 25 <= bmi < 30:
    international = '偏胖'
else:
    international = '肥胖'

# 国内BMI分类判断
if bmi < 18.5:
    domestic = '偏瘦'
elif 18.5 <= bmi < 24:
    domestic = '正常'
elif 24 <= bmi < 28:
    domestic = '偏胖'
else:
    domestic = '肥胖'

# 输出结果
print("BMI数值为:{:.2f}".format(bmi))
print(f"BMI指标为:国际\'{international}\',国内\'{domestic}\'")