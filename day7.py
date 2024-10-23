# string introcution
firstName = "chinmay"
lastName = 'deshpande'
print(firstName)
print(lastName)
info = '''
    i am learning js 
    and python
'''
info2 = """
    i am learning python and 
    javascript
"""
print(type(firstName))
print(type(lastName))
print(type(info))
print(type(info2))

# does string stores the value by index ???

info3 = "ram"
#  0    1    2
#  r    a    m
print(info3[0])
print(info3[1])
print(info3[2])


# program 1
# using range - for
fn = "chinmay"
# 0   1   2   3   4   5   6
# c   h   i   n   m   a   y

# program 2
for ch in range(len(fn)):
    #print(ch)
    print(fn[ch])

firstN   = "abhisha"
for  x in range(len(firstN)):
    #print(x)
    print(firstN[x])

# program 3
# for  - without range
firstN   = "abhisha"
for i in firstN:
    print(i)

# while loop
i1 = 0 
while(i1 < len(firstN)):
    #print(i1)
    print(firstN[i1])
    i1 = i1 + 1


# program 4
fruits = "apple  mango banana orange papaya chikoo" 
print("apple" in fruits)
print("Apple" in fruits)


# program 5
# upper()
city2 = "raipur"
e1 = city2.upper()
print(e1)

city2 = "Goa"
e2 = city2.lower()
print(e2)

city3 = "rajasthan"
e3 = city3.capitalize()
print(e3)

















# revision
# city = "pune"
# print(type(city))
# print(city[0])
# print(len(city))

# # for - range
# for x in range(len(city)):
#     #print(x)
#     print(city[x])

# # for - without range
# for x in city:
#     print(x)

# # while loop
# i2  = 0 
# while(i2 < len(city)):
#     print(city[i2])
#     i2 = i2 + 2
