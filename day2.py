# program 1
#          0       1         2          3
listA = ["pune","mumbai","bangalore","kolkata"]
print(listA)
print(listA[0])

# upadte 
listA[0] = "wardha"
print(listA)

#how many elements 
x = len(listA)
print(x)

# particular element exist in list
print("bangalore" in listA)
print("Bangalore" in listA)

# loops 
#           0        1        2        3
fruits = ["apple","banana","orange","grapes"]

for x in range(len(fruits)):
    #print(x)
    print(fruits[x])

fr = 0
while(fr < len(fruits)):
    #print(fr)
    print(fruits[fr])
    fr = fr + 1

for x in fruits:
    print(x)

# do list stores duplicate values 
city  = ["pune","pune"]
print(city)

# methods 
# methods of list 


# append()
vegetables = ["cabbage","cauliflower","spinach"]
vegetables.append("lafyfinger")
print(vegetables)

# extend()
vegetables.extend(["onion",'potato','tomato'])
print(vegetables)

# sort()
country  =["india","china",'bangladesh']
country.sort()
print(country)

# clear()
# country.clear()
# print(country)

# reverse()
country  =["india","china",'bangladesh']
country.reverse()
print(country)

#            0        1       2
country  =["india","china",'bangladesh']
#country.pop() by default will delete the last element
#country.pop(1)
#print(country)

#remove()
country.remove('china')
print(country)

# index()
country  =["india","china",'bangladesh']
g = country.index("china")
print(g)


numbers  =[11,22,33,44,11,22,33]
e = numbers.count(11)
print(e)







