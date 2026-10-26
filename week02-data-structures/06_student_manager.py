students = [
    {"name": "Tom", "score": 90},
    {"name": "Jerry", "score": 85},
    {"name": "Alice", "score": 95}
]

#遍历学生显示姓名和成绩
def show_students():
    for student in students:
        print(
            f"姓名：{student['name']}，成绩：{student['score']}"
        )

show_students()
#添加学生
def add_student(name, score):
    student = {
        "name": name,
        "score": score
    }
    students.append(student)
#删除学生
def delete_student(name):
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print(f"已删除学生：姓名：{student['name']}")
            return
    print(f"未找到学生：{name}")
#查看学生
#修改成绩
def update_student_score(name, new_score):
    for student in students:
        if student["name"] == name:
            student["score"] = new_score
            print(f"已更新学生：姓名：{student['name']}，新成绩：{student['score']}")
            return
    print(f"未找到学生：{name}")
#查询学生 
def find_student(name):
    for student in students:
        if student["name"] == name:
            print(f"找到学生：姓名：{student['name']}，成绩：{student['score']}")
            return
    print(f"未找到学生：{name}")

#计算平均成绩
def calculate_average():
    if len(students) == 0:
        print("暂无学生数据")
        return

    total_score = 0

    for student in students:
        total_score += student["score"]

    average = total_score / len(students)
    print(f"平均成绩：{average}")
#找出最高分
def calculate_max_score():
    if len(students) == 0:
        print("暂无学生数据")
        return
    max_score = students[0]["score"]
    for student in students:
        max_score = max(max_score, student["score"])
    print(f"最高成绩：{max_score}")
#找出最低分
def calculate_min_score():
    if len(students) == 0:
        print("暂无学生数据")
        return
    min_score = students[0]["score"]
    for student in students:
        min_score = min(min_score, student["score"])
    print(f"最低成绩：{min_score}")


#菜单
def main():
    while True:
        print("\n===== 学生成绩管理系统 =====")
        print("1. 显示所有学生")
        print("2. 添加学生")
        print("3. 查询学生")
        print("4. 修改学生成绩")
        print("5. 删除学生")
        print("6. 计算平均分")
        print("7. 查看最高分")
        print("8. 查看最低分")
        print("0. 退出系统")

        choice = input("请选择功能：")

        if choice == "1":
            show_students()
        elif choice == "2":
            name = input("请输入学生姓名：")
            score = float(input("请输入学生成绩："))
            add_student(name, score)
        elif choice == "3":
            name = input("请输入要查询的学生姓名：")
            find_student(name)
        elif choice == "4":
            name = input("请输入要修改的学生姓名：")
            new_score = float(input("请输入新成绩："))
            update_student_score(name, new_score)
        elif choice == "5":
            name = input("请输入要删除的学生姓名：")
            delete_student(name)
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            calculate_max_score()
        elif choice == "8":
            calculate_min_score()
        elif choice == "0":
            print("已退出系统")
            break
        else:
            print("无效选项，请重新输入")

main()