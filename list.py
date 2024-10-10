# program 1  string
#         0         1         2       3         4
city = ["pune","bangalore","kolkata","mumbai","chennai"]
print(city[0])
print(city[1])


# program 2 numbers
#          0  1  2  3  4  5  6
numbers = [11,22,33,44,55,66,77]
print(numbers[0])

#program 3 (retrive the value from string)
print(numbers[0])

# update
numbers[1] = 222
print(numbers)


# program 4
#           0    1    2    3
states  = ["MH","UP","RJ","MP"]
# for 
for x in range(4):
    #print(x)
    print(states[x])

#          0         1       2       3
city2 = ["nagpur","pune","mumbai","bangalore"]
q1 = len(city2)
print(q1)

for x in range(q1):
    #print(x)
    print(city2[x])


# program 5
# while loop 
city2 = ["nagpur","pune","mumbai","bangalore"]
i1  = 0
while(i1 < len(city2)):
    #print(i1)
    print(city2[i1])
    i1 = i1 + 1



# program 6
# basic loop for
#          0       1        2         3
city2 = ["pune","jaipur","udaipur","bangalore"]
for x in city2:
    print(x)

# program 7
# particular element visible in loop
fruits = ["apple","mango","banana","oranges","grapes"]
print("apple" in fruits)
print("Apple" in fruits)