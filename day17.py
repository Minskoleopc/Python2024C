numbers = [11,22,33]
total = 0

for x in numbers:
    total = total + x
    #         0   + 11
    #         11  + 22
    #         33  + 33
print(total)


from functools import reduce
r = reduce(lambda x,y:x+y,numbers,10)
print(r)