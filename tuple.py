# names = ["chinmay","sarika","shraddha","raj"]
# print(type(names))
# names[0] = "tanmay"
# print(names)

# tuple
#           0          1      2
names2 = ("chinmay","sarika","shraddha")
names2 = ("chinmay","sarika","shraddha","raj")
print(type(names2))
#names2[0] = "raj"
print(names2)

# program 1
city = ("pune","mumbai","banglore")
city2 = "pune","mumbai","banglore"

print(type(city))
print(type(city2))

#program 2
# does tuple stores the value by index 

flowers = ("lotus","jasmine","rose")
print(flowers)
print(flowers[0])

# program 3 particular element present in tuple
print("rose" in flowers)
print("Rose" in flowers)

# program 4 how to change particular value in tuple
alphabets = ("a","c","c")
f = len(alphabets)
print(f)

alphabets = list(alphabets)
alphabets[1]  = "b"
alphabets = tuple(alphabets)
print(alphabets)

# program 5

alphabets = ("a","c","c")

for x in range(len(alphabets)):
    print(alphabets[x])

for x in alphabets:
    print(x)

k1 = 0
while(k1 < len(alphabets)):
    print(alphabets[k1])
    k1 = k1 + 1


# methods in tuple
#           0           1       2          3
names2 = ("chinmay","sarika","shraddha","chinmay")
e = names2.count("chinmay")
print(e)

e2 = names2.index("sarika")
print(e2)

#tuple unpacking 
a , b = ("ram","sham")
print(a)
print(b)











