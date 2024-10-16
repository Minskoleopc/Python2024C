#            0        1      2         3       4
names = ["chinmay","ninad","sameer","vijeet","satish"]
print(names)
print(type(names))

# add
names.append("ram")

# retrive 
print(names[0])

# update 
names[0] = "ninad"
print(names)

# delete
names.pop()
names.pop(1)
names.remove('sameer')
# element present or not


# program 1
info = ["chinmay","despande", 23,34]
infoA = {
    #  prop:value
    #  key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":23
}
print(type(infoA))

# dictionary stores the value by index ? No
#print(infoA[0])
# retrive 
print(infoA['age'])
print(infoA['lastName'])
print(infoA['firstName'])
print(infoA['rollNo'])

# any particular key or value available in dictionary
# program 2
vehicle = {
    "color":"red",
    "company":"blue",
}
print("color" in vehicle)
print("Color" in vehicle)

# do dictionary stores duplicate properties ?
vehicle2 = {
    "color":"red",
    "company":"blue",
    "regNo":123,
    "color":"blue"
}
print(vehicle2)
vehicle2['color'] = "blue"
# how many properties available in dictionary 
print(len(vehicle2))



# program 3

infoB = {
    #  prop:value
    #  key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":23
}
print(infoB['firstName'])


for prop in infoB:
    print(prop,infoB[prop])

# methods of dictionary

student = {
    "fullName":"chinmay",
    "age":34,
    "skills":["python","javascript","css","html"],
    "canDrive":True
}

for prop in student:
    print(prop,student[prop])

# program 4
for x in student.keys():
    print(x)

for x in student.values():
    print(x)

for k,v in student.items():
    print(k,v)

print(student['age'])
print(student.get('age'))