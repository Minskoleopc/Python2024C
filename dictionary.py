city = ["pune","mumbai","chennai","bangalore","pune"]
print(city)

# # update 
# city[0] = "solapur"

# # add 
# city.append("kolkata")
# city.insert(3,"nagpur")

# # delete

# city.pop()
# city.pop(2)
# city.remove('chennai')

# # retrive
# print(city[2])


# dictionary 
#         fn          ln      rn  ag
info = ["chinmay","deshpande",23,44]
print(info)

info = {
    # property:value
    # key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":44,
    "age":33
}
print(info)
print(type(info))

# length of dict
print(len(info))

# does dictionary allow to store duplicate values
print(info)

# how to check particular key exist ?
print("age" in info)
print("Age" in info)