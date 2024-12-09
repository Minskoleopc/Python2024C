# insection gives common between two elements
setA = {11,22,33,44}
setB = {55,66,77,88,11,22}
e = setA.intersection(setB)
print(e)

# program 2

setC = {11,22,33,44}
setD = {66,77,88}
f = setC.union(setD) # {11,22,33,44,66,77,88}
print(f)

# program 3
setG = {11,22,33,44}
setH = {11,22,44,55}


t = setG.difference(setH)
print(t)
t2 = setH.difference(setG)
print(t2)

# program 4
setG = {11,22,33,44,55,88,99} # 88 ,99
setH = {11,22,33,44,55,66,77}

# setH.difference_update(setG)
# print(setH)

# print(setG.difference(setH))
# setG.difference_update(setH)
# print(setG)

# program 5

setJ = {11,22,33,44}
setK = {66,77,88,99,11,22}

print(setJ.intersection(setK))
setJ.intersection_update(setK)
print(setJ)

# program 6
# symmetric difference

setH = {11,22,33,44,55}
setJ = {44,55,66,77}

g = setH.symmetric_difference(setJ)
print(g)
setH.symmetric_difference_update(setJ)
print(setH)

# program 7 
# return true incase of no common element else return false
setK = {11,22,33,44}
setH = {44,55,66,77}
g = setK.isdisjoint(setH)
print(g)

# program 8 
setJ = {11,22}
setK = {11,22,33}
print(setJ.issubset(setK))
print(setK.issuperset(setJ))