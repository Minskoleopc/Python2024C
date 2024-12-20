# list comprehension

#[statement:loop:condition]


birthYear = [1990,2000,2021,1995]
ages = []
for x in birthYear:
    ages.append(2024- x)
print(ages)


# [statement:loop:condition]
e = [2024 - x for x in birthYear]
print(e)

# program 2
rOne = [11,22,33,44,55,66,77,88]

# [statement:loop:condition]
f1 = [x + 10 for x in rOne]
print(f1)

# program 3
t = [11,22,33,-33,-44,-55,55]
f2 = [x for x in t if x > 0]
print(f2)

f3 = [x for x in t if x < 0]
print(f3)

# program 4
f4 = [11,22,33,44,22,33]
#[odd,even,odd,even,even,odd]

f = ["even" if x %2 == 0 else "odd" for x in f4]
print(f)


x = 10
y = 5

if x > y:
    print('x is greater')
else:
    print('y is greater')

print("x is greater") if x > y else print("y is greater")


