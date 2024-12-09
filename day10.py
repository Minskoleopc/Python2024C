# a = 10
# print(a)
# print(type(a))

# a = 10.5
# print(a)
# print(type(a))

# a = True
# print(a)
# print(type(a))

# c = 'chinmay'
# print(c)
# print(type(c))

# c = [11,22,33,44]
# print(c)
# print(type(c))

# d = {
#     "fullName":"chinmay",
#     "age":35
# }
# print(d)
# print(type(d))

# d = (11,22)
# print(d)
# print(type(d))


# set 
listA = [11,22,33,44,11]
print(listA)
print(type(listA))

setA = {11,22,33,44,55,11}
print(setA)

# set does not store duplicate values

# program 1
setB = {11,22,33,44}
print(setB)
print(type(setB))

# program 2
# does set stores the value by index ?? - NO
#print(setB[0])

#program3
# element available in set
setA = {11,22,33,44,55}
print(11 in setA)

# program4
# looping through set 

setB = {11,22,33,44}
for x in setB:
    print(x)

# program 5
setB = {11,22,33,44}
print(len(setB))

# program 6
#del setB


#program7
# add()
setB = {11,22,33,44}
setB.add(55)
print(setB)

# removes the any element 
setB.pop()
print(setB)

# remove()
setA = {"chinmay","shirish","ram","rahul"}
setA.remove("chinmay")
print(setA)

# clear
setA = {"chinmay","shirish","ram","rahul"}
setA.clear()
print(setA)


setD = {11,22,33,44}
setD.update([55,66])
setD.update((77,88))
setD.update({99,100})
print(setD)



