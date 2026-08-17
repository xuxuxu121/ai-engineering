#猜数字
import random

num1 = random.randint(1,10)
count = 0
while True:
    count += 1
    num2 = int(input("Enter a number between 1 and 10:"))
    if num1 == num2:
        print("正确")
        break
    elif num1 > num2:
        print("猜小了")
    else:
        print("猜大了")
    
print(f"you have guessed {count} times")
        
