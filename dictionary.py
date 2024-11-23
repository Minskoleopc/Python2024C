# city = ["pune","mumbai","chennai","bangalore","pune"]
# print(city)

# # # update 
# # city[0] = "solapur"

# # # add 
# # city.append("kolkata")
# # city.insert(3,"nagpur")

# # # delete

# # city.pop()
# # city.pop(2)
# # city.remove('chennai')

# # # retrive
# # print(city[2])


# # dictionary 
# #         fn          ln      rn  ag
# info = ["chinmay","deshpande",23,44]
# print(info)

# info = {
#     # property:value
#     # key:value
#     "firstName":"chinmay",
#     "lastName":"deshpande",
#     "age":23,
#     "rollNo":44,
#     "age":33
# }
# print(info)
# print(type(info))

# # length of dict
# print(len(info))

# # does dictionary allow to store duplicate values
# print(info)

# # how to check particular key exist ?
# print("age" in info)
# print("Age" in info)


info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":12,
    "skills":["python","javascript","html","css"],
    "age":34
}

print(type(info))

# len of dictionary 
print(len(info))

# how to ensure particular key exist ?
print("age" in info)

#consider the last as updated value 
print(info)

# retrive 

vehicle = {
    "color":"red",
    "company":"audi",
    "type":"sedance"
}
print(vehicle)

# retrive
# print("hello")
# e = vehicle['Color']
# print(e)
# print("bye")


# get method
print('hello')
e2 = vehicle.get('Color')
print(e2)
print("bye")

# program 3

vehicle = {
    "color":"red",
    "company":"audi",
    "type":"sedane"
}
vehicle.popitem()  # removes the last item
vehicle.pop('color') # property name
print(vehicle)

# program 4
vehicle = {
    "color":"red",
    "company":"audi",
    "type":"sedane"
}
vehicle.clear()
print(vehicle)

# program 5

vehicle = {
    "color":"red",
    "company":"audi",
    "type":"sedane"
}

vehicle.update({"yearOfManufacture":2024})
print(vehicle)

# program 6
vehicle = {
    "color":"red",
    "company":"audi",
    "type":"sedane"
}

# loops
for x in vehicle.keys():
    print(x)

for x in vehicle.values():
    print(x)

for (k,v) in vehicle.items():
    print(k,v)

for x in vehicle:
    print(x,vehicle[x])

# program 7
vehicle = {
    "color":"red",
    "company":"audi",
    "type":"sedane"
}

#e = vehicle.setdefault('color',"blue")
e = vehicle.setdefault('YOM',2024)
print(e)
print(vehicle)

# program 8
e = dict.fromkeys(["keyOne","keyTwo","keyThree"])
print(e)

#program 9


info2 = {
    "fn":"chinmay",
    "ln":"deshpande"
}

info3 = info2.copy()
info3["fn"] = "raj"
print(info3)
print(info2)

# print(type(info2))
# info3 = info2

# info2["fn"] = "tanmay"
# print(info2)
# print(info3)