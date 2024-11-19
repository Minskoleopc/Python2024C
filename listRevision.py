
# names = ["chinmay","deshpande","sarika"]
# print(type(names))

# # does store value by indec
# print(names[0])

# # update of element in list 
# names[2] = "rahul"
# print(names)

# # len of list 
# print(len(names))

# # element present in list 
# print("rahul" in names)

# # delete 
# del names

# loop

#for 
#            0        1       2       3
# flowers = ["lily","jasmine","rose","lotus"]

# for x in range(len(flowers)):
#     #print(x)
#     print(flowers[x])

# #for without range
# for x in flowers:
#     print(x)

# # while loop
# q1 = 0
# while(q1 < len(flowers)):
#     print(flowers[q1])
#     q1 = q1 + 1


# methods in list 

# append()
fruits = ["apple","mango","banana","orange"]
fruits.append("papaya")
print(fruits)

# program 2
#             0        1       2      3
animals = ["rabbit","snake","tiger","lion"]

# pop()
# pop(2)
# remove("snake")

animals.pop()
print(animals)

animals.pop(1)
print(animals)
animals.remove("rabbit")
print(animals)

# append(), pop(), remove()

# program 3
city = ["pune","banglore","kolkata","chennai"]
city2 = ["wardha","nagpur","sagamner"]

# city.extend(city2)
# print(city)

# city2.extend(city)
# print(city2)

# program 4
city = ["pune","banglore","kolkata","chennai"]

# city.reverse()
# print(city)

city.sort()
print(city)

# program 5
#            0          1          2          3
country = ["india","srilanka","pakistan","bangaladesh"]
country.clear()
print(country)

print('-----------------------------------')
# program 6
#            0         1          2         3            4       5       6
country = ["india","srilanka","pakistan","bangaladesh","india","china","india"]
# f = country.index("india")
# f = country.index("india",1)
f = country.index("india",1,5)
print(f)

country.insert(2,"china")
print(country)


numbers = [11,22,33,44,55,66,77,22,33,44,22]
e3 = numbers.count(22)
print(e3)

# copy

x = 10
print(x)
y = x
y = 90
print(x) # 10
print(y) # 90


names = ["chinmay",'ram',"sham","poorva"]
print(names)
names2 = names
names2[0] = "sarika"
print(names2)
print(names)

#              0       1       2        3
fruits   = ["apple","mango","banana","orange"]

fruits2 = fruits.copy()
fruits2[0] = "papaya"
print(fruits)
print(fruits2)