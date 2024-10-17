
info = ["chinmay","deshpande",34,55]

# infoA = {
#     "firstName":"chinmay",
#     "lastName":"deshpande",
#     "rollNo":34,
#     "age":55,
#     "age":40
# }
# print(infoA)
# # property available 
# print("age" in infoA)
# # retrive 
# print(infoA['lastName'])
# # update
# infoA['age'] = 66
# print(infoA)
# # how many properties in dict 
# e = len(infoA)
# print(e)
# # add 
# infoA['language'] = "marathi"
# print(infoA)
# # does it store the value by index
# print(infoA[0])



infoA = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "rollNo":34,
    "age":55,
}

for prop in infoA:
    print(prop,infoA[prop])

for x in infoA.keys():
    print(x)

for x in infoA.values():
    print(x)

for k,v in infoA.items():
    print(k,v)

# day 5
infoA = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "rollNo":34,
    "age":55,
}

# program 3
e = infoA.get('firstName')
print(e)

# program 2
# infoA.clear()
# print(infoA)

infoA.update({'language':"marathi"})
print(infoA)

# remove the last order item(prop as well value)
infoA.popitem()
print(infoA)

infoA.pop('firstName')
print(infoA)

# program 2

vehicle = {
    "color":"red",
    "company":"audi"
}
# vehicle2 = vehicle
# vehicle2['color'] = "blue"

# print(vehicle)
# print(vehicle2)

vehicle3 = vehicle.copy()
vehicle3['color'] = "blue"
print(vehicle)
print(vehicle3)


vehicle = {
    "color":"red",
    "company":"audi"
}

e = vehicle.setdefault('regNo',"123")
print(vehicle)
print(e)


q1 = dict.fromkeys(['key',"key1","key3"])
print(q1)