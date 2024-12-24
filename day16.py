# [statement/expression     loop     condition]

# program1 
lstA = [1,2,3,4,5,6,7,8,9,10]
# [1,4,9,16,25,36,49,64,81,10]
e = [x *x for x in lstA]
print(e)

# program 2
# table of 2
lstB = [1,2,3,4,5,6,7,8,9,10]
e2 = [x * 2 for x in lstB]
print(e2)

# program 3 
# list comprehension with condition
lstC = [11,22,33,-44,55,66,77,-90,56,77,99,20]
e3 = [x for x in lstC if x > 0]
print(e3)

# program 4 
names = ["chinmay","raj","sarika","poorva","shraddha","ram"]
e4 = [name.upper() for name in names]
print(e4)

# program 5
e = [x * x for x in range(1,6)]
print(e)

# program 6
lstD = [22,33,44,66,77]
# e3 = ["even" if x%2 == 0 else "odd" for x in lstD]
# print(e3)

f =[x*x if x % 2 == 0 else x for x in lstD]
print(f)

# program 7
cities = ["pune","mumbai",'bangalore',"kolkata"]
f2 = [x[0] for x in cities]
print(f2)

# numbers = [44,55,22,33,44,55,77]
# g = sorted({x for x in numbers})
# print(g)

# map filter reduce --->


def add(x,y):
    return x + y
e3 = add(12,3)
print(e3)

add = lambda x,y:x+y
e4 = add(4,5)
print(e4)