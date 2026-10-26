numbers = {1, 2, 3, 4}
print(numbers)
numbers.add(5) #添加元素
print(numbers)
numbers.remove(3) #删除元素
print(numbers)


#判断元素是否存在集合中
print(3 in numbers)
print(5 in numbers) 

#集合的并集
numbers2 = {3,4,5,6}
union_all = numbers.union(numbers2)
print(union_all)

#集合的交集
numbers3 = {4,5,6,7}
both = numbers.intersection(numbers3)
print(both) 

