student = {
    "name": "Tom",
    "age": 20,
    "score": 90
}
print(student["name"]) #打印字典中的name键
student["score"] = 95 #修改字典中的score键
print(student) #打印整个字典
student["major"] = "Computer Science" #添加键值对
print(student)
del student["age"]#删除字典中的age键
print(student)
print("age" in student)#判断字典中是否存在age键

#遍历字典
for key in student:  # noqa: PLC0206
    print(key)
    print(key, student[key])


students = {
    "name": "Tom",
    "age": 20,
    "score": 90
}

for key, value in students.items():
    print(key, "=", value)

print(students.keys())
print(students.values())
print(students.items())

students1 = [
    {"name": "Tom", "score": 90},
    {"name": "Jerry", "score": 85},
    {"name": "Alice", "score": 95}
]

for student in students1:
    print(student["name"], student["score"])