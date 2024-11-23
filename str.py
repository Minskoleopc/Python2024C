fn = 'chinmay'
fn2 = "chinmay"
fullname = """
    chinmay deshpande
    I am learning js 
"""
fullname2 = '''
    chinmay deshpande
    I am learning python
'''
print(type(fn))
print(type(fn2))
print(type(fullname))
print(type(fullname2))

# program 2
fn = 'sarika'
ln = 'pansare'

# my firstName is sarika and my lastName is pansare
print(f"my firstName is {fn} and my lastName is {ln}")
# 0  1 2 3 4 5 6
# c  h i n m a y
fn  ="chinmay"
# does string does the value by index 
print(fn[0])
# can we update single character in string 
#fn[1] = "c"
# can we verify particular character exist in string 
print('C' in fn)
# can we find length of string 
print(len(fn))
# how to delete string 
del fn
# how to loop over string - for , for -range , while loop
lastName = "deshpande"

# 0 1 2 3 4 5 6 7 8
# d e s h p a n d e

for x in lastName:
    print(x)

for x in range(len(lastName)):
    #print(x)
    print(lastName[x])

i1 = 0
while(i1 < len(lastName)):
    print(i1)
    print(lastName[i1])
    i1 = i1 + 1

# slicing 
# methods