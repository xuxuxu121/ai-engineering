#计算器
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

