#program 1
# len of list 
# index of list
#          0         1         2        3       4        5
names = ["sarika","poorva","abhisha","mayuri","komal","ruchira"]
e = len(names)
print(e)
# length -1 is always last index

# program 2
# retrivr
city = ["pune","mumbai","banglore","kolkata"]
print(city[0])
# update 
city[0] = "nagpur"
print(city)
# is it list ?
print(type(city))

# program 3
flowers = ["lily","jasmine","rose","sunflower"]
print('lily' in flowers) # boolean --- true or false
print('Lily' in flowers)

# program 4
#            0         1         2         3        4
country = ["india","pakistan","canada","srilanka","dubai"]

for x in range(5):
    print(x)


for x in range(len(country)):
    #print(x) #0
    print(country[x])


# program 5
# looping through list
#            0        1       2     3
animals = ["tiger","lion","rabbit","cat"]

# range()

for x in range(len(animals)):
    #print(x)
    print(animals[x])

# for
for x in animals:
    print(x)

# while
i1 = 0
while(i1 < len(animals)):
    print(animals[i1])
    i1 = i1 + 1

# methods --------------->