# loop

# print to 5

print(1)
print(2)
print(3)
print(4)
print(5)

#for      while 
# range()
# range(startIndex(default-0),endIndex(not included),Steps)
# without start index ...
# print 0 to 2
for x in range(3):
    print(x)

# print 1 to 2
# with startindex 
for x in range(1,3):
    print(x)

# print "hello" 3 tyms
for x in range(3):
    print("hello")
    print('bye')

# print 1 to 5
for x in range(1,6):
    print(x)

# table of 2 
for x in range(1,11):
    print(x * 2)

# table of 2 -v2
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
for x in range(2,21,2):
    print(x)

#table of 3 
for x in range(3,31,3):
    print(x)

# table of 5
for x in range(5,51,5):
    print(x)

# reverse 5 to 1
for x in range(5,0,-1):
    print(x)

# reverse 3 to 1
for x in range(3,0,-1):
    print(x)

# table of 2 in reverse 
for x in range(20,1,-2):
    print(x)

# table of 5 in reverse 
for x in range(50,4,-5):
    print(x)

# break statement with for loop

for x in range(6): # 1 # 2 # 3
    if x == 3:
        break
    print(x) # 0 , 1 , 2


for x in range(6): # 1 # 2 # 3
    print(x) # 0 # 1 # 2 # 3
    if x == 3:
        break
  













