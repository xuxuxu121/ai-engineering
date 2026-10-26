student1 = [
    {
        "name": "Tom",
        "age": 20,
        "score": 90
    },
    {
        "name": "Jerry",
        "age": 21,
        "score": 85
    },
    {
        "name": "Alice",
        "age": 19,
        "score": 95
    }
]
print(student1[0]) 
student1[0]["name"] = "xu"
print(student1[0])
students = [
    {"name": "Tom", "score": 90},
    {"name": "Jerry", "score": 85},
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 78}
]
#遍历学生
for student in students:
    print(student)
#计算平均成绩
total_score = 0

for student in students:
    total_score += student["score"]

avg = total_score / len(students)
print("平均成绩：", avg)
#最高分
max_score = 0
for student in students:
    max_score = max(max_score, student["score"])
print("最高分：",max_score)
#最低分
min_score =100
for student in students:
    min_score = min(min_score, student["score"])
print("最低分：",min_score)
#遍历及格学生
print("及格学生：")
for student in students:
    if student["score"] >= 60:
        print(student["name"])
#遍历学生姓名
print("学生姓名：")
for student in students:
    print(student["name"])
#去掉重复姓名
print("去掉重复姓名：")
name_set = set()
for student in students:
    name_set.add(student["name"])
print(name_set)

