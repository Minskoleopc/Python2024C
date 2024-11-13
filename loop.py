
# loop - 

# for loop 
# while  loop 

# for - range 
# for - for without loop

#range(startIndex , endIndex (not included) , Step)
# startIndex - by default - 0 
# step - by default - 1


# program 1
for x in range(3):
    print(x)

for x in range(5):
    print(x)

# program 2 
# print 1 to 5
for x in range(1,6):
    print(x)

# program 3
for x in range(3):
    print("hello")

# program 5
# table of 2

for x in range(1,11):
    print(x * 2)

for x in range(2,21,2):
    print(x)

# program 5
# print table 
for x in range(5,51,5):
    print(x)

# program 6
# table of 5 in reverse
for x in range(50,4,-5):
    print(x) 

# program 7
# break with for loop

for x in range(1,6):
    print(x)
    if x == 3:
        break

for x in range(1,6):
    if x == 3:
        break
    print(x)
    
# 10,8,6,4,2
for x in range(10,0,-2):
    if x == 4:
        break
    print(x)

# program 8
# continue with for
for x in range(1,6):  #2 #3 #4 #5 #6
    if x == 3:
        continue
    print(x)  #1#2#4#5

# program 9

for x in range(5,0,-1):
    if x == 2:
        continue
    print(x) # 5 ,4 ,3 ,1


# while loop 

#intialization
# while(condition):
    #statement
    #increment / decrement


i1 = 1
while(i1 <= 3):
    print(i1) # 1 # 2 # 3
    i1 = i1 + 1 # 2 # 3 # 4


i2 = 1
while(i2 <= 3):
    print("hello") # "hello" , "hello" , "hello"
    i2 = i2 + 1 # 2 # 3 # 4

i3 = 1
while(i3 <= 5):
    print(i3)
    i3 = i3 + 1

i4 = 2
while(i4 <= 20):
    print(i4) # 2 # 4 --------- 20
    i4 = i4 + 2 # 4 # 6 -------- 22

i5 = 5
while(i5 <= 50):
    print(i5)
    i5 = i5 + 5


i6 = 20
while(i6 >= 2):
    print(i6) # 20  # 18 ----------2
    i6 = i6 - 2 # 18 # 16 --------------0
    

# break statement with while 

i7 = 1
while(i7 <= 5):
    if i7 == 3:
        break
    print(i7) #1 #2
    i7 = i7 + 1 #2 #3


i7 = 1
while(i7 <= 5):
    print(i7)  # 1 #2 #3
    if i7 == 3:
        break
    i7 = i7 + 1 #2 #3

# continue

















