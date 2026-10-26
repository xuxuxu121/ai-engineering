person = ("Tom", 20, "Computer Science")
print(person)
print(person[0]) 
print(person[1])
print(person[2])
name,age,major = person
print(name)
print(age)
print(major)    
#person[0] = "Jerry" 
#尝试修改元组中的元素，会报错
#元组是不可变的，不能修改元素

numbers = (10, 20, 30, 40, 50)
print(numbers)
print(numbers[0])
print(numbers[len(numbers)-1])

for number in numbers:
    print(number)

print(sum(numbers))#计算元组中所有元素的总和

print(sum(numbers)/len(numbers)) #计算平均值


students = [
    ("Tom", 20),
    ("Jerry", 21),
    ("Alice", 19)
]

for name, age in students:
    print(name, age)