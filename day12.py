setA = {11,22,33}
# setB  = setA
# setB.add(66)
# print(setA)
# print(setB)

setB = setA.copy()
setB.add(55)
print(setA)
print(setB)

setC = {11,22,33,44}
setC.discard(44)
#print(setC)

setC.pop()
print(setC)

setC.remove(22)
print(setC)

# remove and discard ??? return type

a = 10
print(a)
print(type(a))


b = 12.4
print(b)
print(type(b))

c = "chinmay"
print(type(c))

d = True
print(d)
print(type(d))

e  = [11,22,33,44]
print(e)
print(type(e))

f = {
    'firstName':"chinmay",
    'lastName':"deshpande"
}
print(f)
print(type(f))

g = 12,3
print(g)
print(type(g))

j = {11,22,33,44}
print(j)
print(type(j))

# fn 
# 16 dec