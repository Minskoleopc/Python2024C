from functools import reduce
# program 1
birthYear = [1989,1990,1991,1992]
ages = []

for x in birthYear:
    ages.append(2024 - x)
print(ages)

# list comprehension
# list comprehension always returns lisy
ages = [2024 - year for year in birthYear]
print(ages)
#map()
ages = list(map(lambda x:2024-x,birthYear))
print(ages)

# program 2
marks = [44,55,22,33,44,55,6,77,88]
above50 = []

for x in marks:
    if x > 50:
        above50.append(x)
print(above50)

above50 = [x for x in marks if x > 50]
print(above50)

#filter method
above50 =  list(filter(lambda x : x > 50,marks))
print(above50)

transactions = [100,50,-100,-52,-100,-43]
deposit = list(filter(lambda x:x > 0,transactions))
withdrawl = list(filter(lambda x:x < 0,transactions))
print(deposit)
print(withdrawl)

totalDeposit  = reduce(lambda x,y:x+y,deposit,0)
print(totalDeposit)

totalWithDrawl  = reduce(lambda x,y:x+y,withdrawl,0)
print(totalWithDrawl)

# program 3
numbers = [11,22,33]
total = 0

for x in numbers:
    total  = total + x
print(total)
print(reduce(lambda a,b:a+b,numbers,0))