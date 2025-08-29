from functools import reduce

add = lambda x, y: x + y
print(add(10,20))
print(add(2,5))
print((lambda x, y: x + y)(20,40))

maxnum = lambda x, y: x if x > y else y

print(maxnum(10,20))
print(maxnum(2,5))

names = ["india","usa","australia","japan", "china"]
sorte_names = sorted(names, key= lambda x : len(x))
print(sorte_names)

nos = [1,2,3,4,5,6,7,8,9,10]
squares = list(map(lambda x: x ** 2, nos))
print(squares)


data = list(filter(lambda x: x % 5 == 0, nos))
print(data)

total = reduce(lambda x, y: x + y, nos)
print(total)

multiply = lambda x : (lambda y : x*y)
double = multiply(2)

print(double(10))

keys = ['id','name','age']
values=[1001,'kumar',50]

to_dict = lambda k,v : dict(zip(k,v))
data = to_dict(keys,values)
print(data)