# # [statement/expression     loop     condition]

# # program1 
# lstA = [1,2,3,4,5,6,7,8,9,10]
# # [1,4,9,16,25,36,49,64,81,10]
# e = [x *x for x in lstA]
# print(e)

# # program 2
# # table of 2
# lstB = [1,2,3,4,5,6,7,8,9,10]
# e2 = [x * 2 for x in lstB]
# print(e2)

# # program 3 
# # list comprehension with condition
# lstC = [11,22,33,-44,55,66,77,-90,56,77,99,20]
# e3 = [x for x in lstC if x > 0]
# print(e3)

# # program 4 
# names = ["chinmay","raj","sarika","poorva","shraddha","ram"]
# e4 = [name.upper() for name in names]
# print(e4)

# # program 5
# e = [x * x for x in range(1,6)]
# print(e)

# # program 6
# lstD = [22,33,44,66,77]
# # e3 = ["even" if x%2 == 0 else "odd" for x in lstD]
# # print(e3)

# f =[x*x if x % 2 == 0 else x for x in lstD]
# print(f)

# # program 7
# cities = ["pune","mumbai",'bangalore',"kolkata"]
# f2 = [x[0] for x in cities]
# print(f2)

# # numbers = [44,55,22,33,44,55,77]
# # g = sorted({x for x in numbers})
# # print(g)

# # map filter reduce --->


# def add(x,y):
#     return x + y
# e3 = add(12,3)
# print(e3)

# # lambda function
# add = lambda x,y:x+y
# e4 = add(4,5)
# print(e4)


add = lambda x,y:x+y
# add - function 
# x,y - parameter
# return - x + y
e = add(12,2)
print(e)

# lamda function
sub = lambda x,y:x-y
e = sub(12,4)
print(e)


# program 1
years = [1989,1990,1991,1992]
ages = []


# for loop 

for x in years:
    ages.append(2024-x)
print(ages)

# list comprehension
e = [2024 - x for x in years]
print(e)
# map()

f = list(map(lambda x:2024-x,years))
print(f)

listB = [11,22,33]
j = list(map(lambda x:x+10,listB))
print(j)



# program 2
listC  = [22,33,44,55,22,33,44,55,66,77]
above50 =[]
for x in listC:
    if x > 50:
        above50.append(x)
print(above50)

# list comprehension
r = [x for x in listC if x > 50]
print(r)

# filter()

g = list(filter(lambda x:x>50,listC))
print(g)

transactions = [11,-11,90]
deposit = list(filter(lambda x:x>0,transactions))
print(deposit)
withdrawl = list(filter(lambda x:x<0,transactions))
print(deposit)

# program 3
numbersC  = [11,22,33]
total = 0

for x in numbersC:
    total =  total + x   # 11 ===> 11 + 22 ====> 33 + 33 ====> 66
print(total)