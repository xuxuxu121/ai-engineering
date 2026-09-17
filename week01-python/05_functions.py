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
def is_even(num: int) ->bool:
    return num % 2 == 0

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

