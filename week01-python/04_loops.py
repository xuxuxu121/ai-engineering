for i in range(1, 11):
    print(i)

number = 1
while number <= 10:
    print(number)
    number += 1

#打印1-100的偶数
for i in range(1, 101, 2):
    print(i)

#打印1-100的和
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

#99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()