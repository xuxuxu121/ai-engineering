fruits = ["apple", "banana", "orange"]
print(fruits[0]) #打印第一个元素
fruits.append("watermelon") #添加元素
fruits.remove("banana") #删除元素
fruits[1] = "grape" #修改元素
print(fruits) #打印整个列表
for fruit in fruits:
    print(fruit) #遍历列表并打印每个元素

#成绩
scores = [80, 90, 75, 88, 92]
total = 0
for score in scores:
    total += score
print(total)
print(sum(scores)) #使用内置函数sum()计算总分

#平均分
avg = total / len(scores)
print(avg)
print(sum(scores) / len(scores)) #使用内置函数sum()和len()计算平均分

#最高分
max_score = 0
for score in scores:
    max_score = max(max_score, score)
print(max_score)
print(max(scores)) #使用内置函数max()计算最高分

#最低分
min_score = 100
for score in scores:
    min_score = min(min_score, score)
print(min_score)
print(min(scores)) #使用内置函数min()计算最低分