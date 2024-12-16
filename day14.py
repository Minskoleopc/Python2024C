#         0    1   2    3
lstA = [2000,1999,1998,1997]
ages = [] #[24,25,26,27]
#[24,25,26,27]

for year in lstA:
    #print(year)
    #print(2024 - year)
    age = 2024 - year
    ages.append(age)
print(ages)

numbers = [10,20,30]
# [20,30,40]
add10 = []

for x in numbers:
    #print(x+10)
    add10.append(x+10)
print(add10)


# program 2

marks  = [23,44,55,22,57,58,66]
# [55,57,58,66]
above50 = []

for i in marks:
    if i > 50:
        above50.append(i)
print(above50)
        
transactions = [12,-12,100,200,300,400,500,-500,-300]
withdrawl = []
deposit = []

for x in transactions:
    if x < 0:
        withdrawl.append(x)
    else:
        deposit.append(x)
print(deposit)
print(withdrawl)

# program 3
lstB = [11,22,33]
total = 0
for x in lstB:
   total = total + x # 66
print(total)

# program 4
cities = ["pune","mumbai","banglore","kolkata"]

for x in cities:
    print('welcome '+x+" !")