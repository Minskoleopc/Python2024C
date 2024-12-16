
# int as a parameter and interger as return type 
def add(x,y):
    return x + y
e = add(12,3)
print(e)

# float as a parameter and float as return type 
def addB(x,y):
    return x + y
f  = addB(12.5,2.6)
print(f)

# boolean as a parameter and boolean as return type 
def canDrive(age, haveVehicle):
    if age >= 18 and haveVehicle:
        return True
    else:
        return False
g = canDrive(18,True)
print(g)

# string as parameter and string as a return type 
def greet(name):
    return "welcome "+name+" !"
f = greet("chinmay")
print(f)

# list as parameter and list as a return 
names = ["chinmay","sarika","poorva","shrddha","manish"]
def addElement(lst):
    #lst = ["chinmay","sarika","poorva","shrddha","manish"]
    lst.append("mitesh")
    return lst

g = addElement(names)
print(g)

# dict as a parameter and dict as return type 

info = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}

def addCity(dict):
    dict.update({"city":"pune"})
    return dict

j = addCity(info)
print(j)

# tuple as parameter and tuple as return type 
tupleA = 11,22
def addE(tp):
    tp = list(tp)
    tp.append(33)
    tp = tuple(tp)
    return tp
h = addE(tupleA)
print(h)

# set as a parameter and set as a return 

setA = {11,22,32}

def addE(setE):
    setE.add(44)
    return setE
f = addE(setA)
print(f)


# difference between remove and discard
# print("hello")
# setA = {11,22,33}
# #e = setA.discard(44)
# setA.remove(44)
# print(e)
# print("bye")

# info 

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":13
}

print(info)

#info.pop('firstName')

info.popitem()
print(info)


# function as a parameter

# function as a return type