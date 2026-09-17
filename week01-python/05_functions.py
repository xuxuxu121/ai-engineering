def add(a: int, b: int) -> int:
    return a + b


result = add(10, 20)

print(result)

#减法
def subtract(a: int,b: int) ->int:
    return a - b

result = subtract(10,20)
print(result)

#乘法
def multiply(a: int,b: int) ->int:
    return a * b

result = multiply(10,20)
print(result)

#除法
def divide(a: int,b: int) ->float:
    return a / b

result = divide(10,20)
print(result)

#判断是不是偶数
def is_even(mun: int) ->bool:
    return mun % 2 == 0

result = is_even(10)
print(result)
print(is_even(7))

#判断等级
def get_grade(score: int) ->str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"      

print(get_grade(95))
print(get_grade(82))
print(get_grade(73))
print(get_grade(60))
print(get_grade(45))

#计算器
# 计算器

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a = float(input("请输入第一个数字: "))
x = input("请输入运算符: ")
b = float(input("请输入第二个数字: "))

if x == "+":
    result = add(a, b)

elif x == "-":
    result = subtract(a, b)

elif x == "*":
    result = multiply(a, b)

elif x == "/":
    result = divide(a, b)

else:
    result = "运算符错误"

print(result)