# Week 01 Python 学习记录与复习手册

> 学习方向：AI 应用工程师\
> 当前阶段：AI Engineering 第 1 周 ------ Python 基础回顾\
> 学习参考：CS50P + 本周实战练习\
> 状态：已完成本阶段核心练习

------------------------------------------------------------------------

## 1. 本周学习目标

本周的目标不是重新学习所有 Python，而是通过 CS50P
的基础内容和小练习，把后续 AI 工程开发需要的 Python 基础重新建立起来。

本周重点：

-   Python 变量
-   `input()` 输入
-   数据类型
-   类型转换
-   f-string
-   `if / elif / else`
-   `for` 循环
-   `while` 循环
-   `break / continue`
-   `random` 模块
-   变量自增
-   简单命令行程序
-   基础错误排查
-   Ruff 基础使用

------------------------------------------------------------------------

# 2. Python 基础知识

## 2.1 变量

变量用于保存数据。

``` python
name = "xu"
age = 23
```

变量可以保存不同类型的数据：

``` python
name = "xu"       # str
age = 23          # int
score = 95.5      # float
is_student = True # bool
```

可以使用 `type()` 查看变量类型：

``` python
print(type(name))
print(type(age))
```

------------------------------------------------------------------------

## 2.2 input()

`input()` 用于获取用户输入。

``` python
name = input("What is your name?")
```

需要特别记住：

> `input()` 得到的数据默认是 `str`（字符串）。

例如：

``` python
age = input("What is your age?")
```

即使输入：

``` text
23
```

Python 得到的实际上是：

``` python
"23"
```

而不是：

``` python
23
```

------------------------------------------------------------------------

# 3. 类型转换

如果需要把用户输入转换成数字，可以使用：

``` python
int()
float()
str()
```

例如：

``` python
age = int(input("What is your age?"))
```

或者：

``` python
score = float(input("Enter your score:"))
```

常见转换：

``` python
int("23")       # 23
float("23.5")   # 23.5
str(23)         # "23"
```

## 本周遇到的典型错误

错误：

``` text
TypeError: '>=' not supported between instances of 'str' and 'int'
```

原因：

``` python
age = input("Age:")
if age >= 18:
    ...
```

这里 `age` 是字符串。

正确：

``` python
age = int(input("Age:"))

if age >= 18:
    ...
```

------------------------------------------------------------------------

# 4. f-string

f-string 用于把变量或表达式放进字符串中。

语法：

``` python
f"文字 {变量}"
```

例如：

``` python
name = "xu"
age = 23

print(f"My name is {name}.")
print(f"I am {age} years old.")
```

也可以直接放表达式：

``` python
num1 = 10
num2 = 3

print(f"The sum is: {num1 + num2}")
```

输出：

``` text
The sum is: 13
```

可以简单理解为：

> `f` 表示这个字符串允许在 `{}` 中插入 Python 表达式。

------------------------------------------------------------------------

# 5. 条件判断

## 5.1 if

``` python
if condition:
    ...
```

例如：

``` python
age = 23

if age >= 18:
    print("Adult")
```

------------------------------------------------------------------------

## 5.2 elif

`elif` 表示：

> 否则，如果......

例如：

``` python
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
```

一个 `if` 可以有多个 `elif`。

------------------------------------------------------------------------

## 5.3 else

`else` 表示：

> 前面的所有条件都不满足时执行。

例如：

``` python
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
else:
    print("F")
```

------------------------------------------------------------------------

## 5.4 if / elif / else 的执行特点

Python 会按照顺序检查条件。

一旦找到第一个满足条件的分支，就执行该分支，后面的 `elif` 和 `else`
不再执行。

例如：

``` python
grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
```

输出：

``` text
B
```

虽然 85 也满足 `grade >= 70`，但不会继续检查，因为 `grade >= 80`
已经满足。

------------------------------------------------------------------------

# 6. 本周练习一：计算器

## 目标

输入两个数字，计算：

-   加法
-   减法
-   乘法
-   除法

完成代码：

``` python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter next number: "))

print(f"The sum is: {num1 + num2}")
print(f"The difference is: {num1 - num2}")
print(f"The product is: {num1 * num2}")
print(f"The quotient is: {num1 / num2}")
```

## 学到的知识

这个练习串联了：

``` text
input()
   ↓
float()
   ↓
变量
   ↓
+ - * /
   ↓
f-string
   ↓
print()
```

## 可以进一步改进

后续学习异常处理以后，可以解决除数为 0 的问题。

------------------------------------------------------------------------

# 7. 本周练习二：成绩判断

完成了一个成绩等级判断程序：

``` python
grade = float(input("Enter your grade:"))

if grade >= 90:
    print("Your grade is A.")
elif grade >= 80:
    print("Your grade is B.")
elif grade >= 70:
    print("Your grade is C.")
elif grade >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")
```

## 对应知识

``` text
输入成绩
   ↓
float()
   ↓
if
   ↓
elif
   ↓
elif
   ↓
else
```

## 需要掌握

-   `if`：如果
-   `elif`：否则如果
-   `else`：否则

------------------------------------------------------------------------

# 8. random 随机数

Python 可以使用 `random` 模块生成随机数。

首先：

``` python
import random
```

生成 1～100 的随机整数：

``` python
number = random.randint(1, 100)
```

`randint(a, b)`：

> 生成 `a` 到 `b` 之间的随机整数，并且包含两端。

例如：

``` python
random.randint(1, 10)
```

可能得到：

``` text
1
2
3
...
10
```

------------------------------------------------------------------------

# 9. Python 循环

Python 最常用的循环：

-   `for`
-   `while`

------------------------------------------------------------------------

## 9.1 for 循环

适合：

> 已经知道要循环多少次，或者需要遍历一组数据。

例如：

``` python
for i in range(1, 6):
    print(i)
```

输出：

``` text
1
2
3
4
5
```

注意：

> `range()` 包含开始值，不包含结束值。

例如：

``` python
range(1, 6)
```

实际上是：

``` text
1 2 3 4 5
```

------------------------------------------------------------------------

## 9.2 while 循环

适合：

> 根据条件决定什么时候结束。

例如：

``` python
count = 1

while count <= 5:
    print(count)
    count += 1
```

------------------------------------------------------------------------

# 10. break 和 continue

## break

`break`：

> 立即结束当前循环。

例如：

``` python
while True:
    number = int(input("Enter a number:"))

    if number == 0:
        break
```

------------------------------------------------------------------------

## continue

`continue`：

> 跳过本次循环，直接开始下一次循环。

例如：

``` python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

输出：

``` text
0
1
3
4
```

------------------------------------------------------------------------

# 11. 死循环

例如：

``` python
while True:
    print("Hello")
```

这是无限循环。

如果程序在 VS Code 终端中进入死循环，可以按：

``` text
Ctrl + C
```

终止当前程序。

代码中的：

``` python
break
```

则是正常结束循环。

------------------------------------------------------------------------

# 12. 变量自增

本周在猜数字游戏中使用了：

``` python
count += 1
```

它等价于：

``` python
count = count + 1
```

例如：

``` python
count = 0

while True:
    count += 1
```

每次循环：

``` text
0 → 1
1 → 2
2 → 3
3 → 4
...
```

注意：

不要写成：

``` python
count = +1
```

因为这相当于：

``` python
count = 1
```

它不是自增。

------------------------------------------------------------------------

# 13. 本周综合项目：猜数字游戏

这是本周最重要的练习。

## 功能

电脑随机生成 1～10 的数字。

用户不断输入数字：

-   猜对 → 显示正确
-   猜小 → 提示猜小了
-   猜大 → 提示猜大了
-   记录一共猜了多少次

完成代码：

``` python
import random

num1 = random.randint(1, 10)
count = 0

while True:
    count += 1

    num2 = int(input("Enter a number between 1 and 10: "))

    if num1 == num2:
        print("正确")
        break
    elif num1 > num2:
        print("猜小了")
    else:
        print("猜大了")

print(f"You have guessed {count} times")
```

------------------------------------------------------------------------

# 14. 猜数字游戏的程序结构

整个程序可以理解成：

``` text
random.randint()
       ↓
产生答案
       ↓
count = 0
       ↓
while True
       ↓
count += 1
       ↓
input()
       ↓
if / elif / else
   ↙    ↓    ↘
猜对   猜小   猜大
 ↓      ↓      ↓
break  继续   继续
 ↓
输出猜测次数
```

这个项目把本周学习的核心知识全部串联起来。

------------------------------------------------------------------------

# 15. 本周遇到的问题与解决方法

## 问题 1：字符串和整数不能直接比较

错误：

``` text
TypeError: '>=' not supported between instances of 'str' and 'int'
```

原因：

``` python
age = input(...)
```

得到的是字符串。

解决：

``` python
age = int(input(...))
```

------------------------------------------------------------------------

## 问题 2：输入了错误的数据

例如程序显示：

``` text
Enter first number:
```

却输入了 Python 运行命令：

``` text
C:\Users\...\python.exe ...
```

程序会尝试：

``` python
float("C:\\Users\\...")
```

因此出现：

``` text
ValueError
```

解决：

> 程序出现 `Enter first number:` 后，只输入数字。

------------------------------------------------------------------------

## 问题 3：Ruff I001

提示：

``` text
Import block is un-sorted or un-formatted
Ruff[I001]
```

这不是 Python 运行错误，而是 Ruff 的代码规范检查。

可以使用 VS Code：

``` text
Shift + Alt + O
```

整理 imports。

或者：

``` text
ruff check --fix 文件名.py
```

如果使用 uv：

``` text
uv run ruff check --fix 文件名.py
```

------------------------------------------------------------------------

# 16. CS50P 学习对应关系

本周学习内容与 CS50P 的基础知识可以这样对应：

  本周内容              CS50P 相关基础
  --------------------- -----------------------
  变量                  Functions / Variables
  `input()`             用户输入
  `int()` / `float()`   类型转换
  f-string              格式化输出
  `if`                  条件判断
  `elif` / `else`       多分支条件
  `for`                 循环
  `while`               循环
  `break`               循环控制
  `random`              Python 标准库
  猜数字游戏            综合练习

CS50P 学习时不要只看视频。

推荐采用：

``` text
观看课程
   ↓
理解概念
   ↓
自己敲代码
   ↓
完成 Problem Set
   ↓
遇到报错
   ↓
自己定位
   ↓
查文档 / AI 辅助
   ↓
重新实现
```

------------------------------------------------------------------------

# 17. 本周掌握程度检查

完成下面的自测，如果大部分都可以独立完成，就可以进入下一阶段。

## 基础

-   [x] 能创建变量
-   [x] 能使用 `input()`
-   [x] 知道 `input()` 返回字符串
-   [x] 能使用 `int()` 和 `float()`
-   [x] 能使用 f-string
-   [x] 能使用 `if / elif / else`

## 循环

-   [x] 能写简单 `for`
-   [x] 能使用 `range()`
-   [x] 能写简单 `while`
-   [x] 理解死循环
-   [x] 知道 `Ctrl + C`
-   [x] 会使用 `break`
-   [x] 了解 `continue`

## 综合

-   [x] 能使用 `random.randint()`
-   [x] 能使用 `count += 1`
-   [x] 完成计算器
-   [x] 完成成绩判断
-   [x] 完成猜数字游戏

------------------------------------------------------------------------

# 18. 下一步：不要继续重复简单语法

当前阶段已经完成：

``` text
变量
↓
输入
↓
类型
↓
条件
↓
循环
↓
随机数
↓
综合小项目
```

下一阶段建议进入：

## Python 数据结构

重点学习：

1.  `list`
2.  `tuple`
3.  `dict`
4.  `set`
5.  字符串常用操作
6.  列表遍历
7.  字典遍历
8.  列表推导式
9.  函数
10. 参数和返回值

然后继续学习：

``` text
函数
 ↓
文件操作
 ↓
异常处理
 ↓
模块
 ↓
typing
 ↓
面向对象
 ↓
Git + 项目规范
```

这些内容会逐渐进入 AI 应用工程真正需要的 Python 能力。

------------------------------------------------------------------------

# 19. 下一阶段练习建议

完成以下练习：

### 练习 1：列表统计

创建一个数字列表：

``` python
numbers = [10, 20, 30, 40, 50]
```

计算：

-   总和
-   最大值
-   最小值
-   平均值

------------------------------------------------------------------------

### 练习 2：单词统计

让用户输入一句话，统计：

-   单词数量
-   最长单词
-   最短单词

------------------------------------------------------------------------

### 练习 3：学生成绩管理

使用列表保存多个学生成绩，计算：

-   平均成绩
-   最高成绩
-   最低成绩
-   及格人数

------------------------------------------------------------------------

### 练习 4：升级猜数字游戏

给当前猜数字游戏增加：

-   最大猜测次数
-   猜测次数提示
-   猜测范围
-   游戏结束后询问是否重新开始

------------------------------------------------------------------------

# 20. GitHub 提交建议

本周代码建议整理为：

``` text
ai-engineering/
│
├── week01-python/
│   ├── 01_variables.py
│   ├── 02_calculator.py
│   ├── 03_grade.py
│   ├── 04_guess_number.py
│   └── README.md
│
└── README.md
```

每完成一个小项目：

``` bash
git add .
git commit -m "feat: complete week01 python exercises"
git push
```

------------------------------------------------------------------------

# 21. 本周总结

本周最重要的不是记住大量语法，而是建立下面这种思维：

``` text
问题
 ↓
拆解
 ↓
变量保存数据
 ↓
input 获取数据
 ↓
类型转换
 ↓
if 判断
 ↓
循环重复
 ↓
break 控制结束
 ↓
输出结果
```

你已经完成了第一个真正的 Python 综合练习：

> 猜数字游戏。

这说明你已经从"看懂 Python 代码"开始进入"自己写 Python 程序"的阶段。

------------------------------------------------------------------------

# 22. 给下一阶段自己的要求

进入下一阶段以后，坚持：

-   不要直接复制答案
-   先自己写
-   报错先读最后一行
-   能自己解决的小问题先自己解决
-   可以使用 AI，但要理解 AI 给出的代码
-   每个练习至少自己修改一次
-   所有项目都提交 GitHub
-   每周保留学习记录

最终目标不是"会写几个 Python 小程序"，而是：

> **能够独立阅读、修改和编写 AI 工程项目中的 Python 代码。**

------------------------------------------------------------------------

## Week 01 状态

**完成度：核心内容已完成 ✅**

下一阶段：

**Python 数据结构 + 函数**
---

# 23. 函数练习

本阶段完成了 Python 函数基础练习。

## add()

```python
def add(a: int, b: int) -> int:
    return a + b

用于计算两个数字的和。

subtract()
def subtract(a: int, b: int) -> int:
    return a - b

用于计算两个数字的差。

multiply()
def multiply(a: int, b: int) -> int:
    return a * b

用于计算两个数字的乘积。

divide()
def divide(a: int, b: int) -> float:
    return a / b

用于计算两个数字的商。

注意：除数不能为 0。

is_even()
def is_even(num: int) -> bool:
    return num % 2 == 0

使用 % 判断数字除以 2 后的余数，从而判断是否为偶数。

get_grade()
def get_grade(score: int) -> str:
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

根据分数判断成绩等级。

24. 计算器项目

创建：

06_calculator.py

使用函数实现简单计算器。

支持：

+ 加法
- 减法
* 乘法
/ 除法

程序使用：

input()
float()
def
参数
return
if / elif / else
函数调用

程序流程：

输入第一个数字
        ↓
输入运算符
        ↓
输入第二个数字
        ↓
判断运算符
        ↓
调用对应函数
        ↓
得到计算结果
        ↓
输出结果

示例：

请输入第一个数字: 10
请输入运算符: *
请输入第二个数字: 5
50.0

通过这个项目进一步理解了：

先定义函数，再根据需要调用函数。

25. 循环练习总结

完成了以下循环练习：

 for 循环
 while 循环
 range()
 1～100 奇数
 1～100 求和
 99 乘法表
 嵌套 for 循环

1～100 求和结果：

5050

99 乘法表使用了嵌套循环和 f-string。

26. Week 01 最终完成情况
Python 基础
 变量
 input()
 int() / float()
 f-string
 if / elif / else
循环
 for
 while
 range()
 break
 continue
 嵌套循环
函数
 def
 参数
 return
 函数调用
 类型注解
 add()
 subtract()
 multiply()
 divide()
 is_even()
 get_grade()
综合项目
 猜数字游戏
 成绩判断
 计算器
 循环综合练习
 函数综合练习
27. Week 01 状态

完成度：100% ✅

本周已经完成 Python 基础核心内容：

变量
 ↓
输入
 ↓
类型转换
 ↓
条件判断
 ↓
循环
 ↓
函数
 ↓
综合项目

下一阶段：

Python 数据结构

重点学习：

list
tuple
dict
set
字符串操作
列表遍历
字典遍历
列表推导式---

# 23. 函数练习

本阶段完成了 Python 函数基础练习。

## add()

```python
def add(a: int, b: int) -> int:
    return a + b

用于计算两个数字的和。

subtract()
def subtract(a: int, b: int) -> int:
    return a - b

用于计算两个数字的差。

multiply()
def multiply(a: int, b: int) -> int:
    return a * b

用于计算两个数字的乘积。

divide()
def divide(a: int, b: int) -> float:
    return a / b

用于计算两个数字的商。

注意：除数不能为 0。

is_even()
def is_even(num: int) -> bool:
    return num % 2 == 0

使用 % 判断数字除以 2 后的余数，从而判断是否为偶数。

get_grade()
def get_grade(score: int) -> str:
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

根据分数判断成绩等级。

24. 计算器项目

创建：

06_calculator.py

使用函数实现简单计算器。

支持：

+ 加法
- 减法
* 乘法
/ 除法

程序使用：

input()
float()
def
参数
return
if / elif / else
函数调用

程序流程：

输入第一个数字
        ↓
输入运算符
        ↓
输入第二个数字
        ↓
判断运算符
        ↓
调用对应函数
        ↓
得到计算结果
        ↓
输出结果

示例：

请输入第一个数字: 10
请输入运算符: *
请输入第二个数字: 5
50.0

通过这个项目进一步理解了：

先定义函数，再根据需要调用函数。

25. 循环练习总结

完成了以下循环练习：

 for 循环
 while 循环
 range()
 1～100 奇数
 1～100 求和
 99 乘法表
 嵌套 for 循环

1～100 求和结果：

5050

99 乘法表使用了嵌套循环和 f-string。

26. Week 01 最终完成情况
Python 基础
 变量
 input()
 int() / float()
 f-string
 if / elif / else
循环
 for
 while
 range()
 break
 continue
 嵌套循环
函数
 def
 参数
 return
 函数调用
 类型注解
 add()
 subtract()
 multiply()
 divide()
 is_even()
 get_grade()
综合项目
 猜数字游戏
 成绩判断
 计算器
 循环综合练习
 函数综合练习
27. Week 01 状态

完成度：100% ✅

本周已经完成 Python 基础核心内容：

变量
 ↓
输入
 ↓
类型转换
 ↓
条件判断
 ↓
循环
 ↓
函数
 ↓
综合项目

下一阶段：

Python 数据结构

重点学习：

list
tuple
dict
set
字符串操作
列表遍历
字典遍历
列表推导式
