# fn = 'chinmay'
# fn2 = "chinmay"
# fullname = """
#     chinmay deshpande
#     I am learning js 
# """
# fullname2 = '''
#     chinmay deshpande
#     I am learning python
# '''
# print(type(fn))
# print(type(fn2))
# print(type(fullname))
# print(type(fullname2))

# # program 2
# fn = 'sarika'
# ln = 'pansare'

# # my firstName is sarika and my lastName is pansare
# print(f"my firstName is {fn} and my lastName is {ln}")
# # 0  1 2 3 4 5 6
# # c  h i n m a y
# fn  ="chinmay"
# # does string does the value by index 
# print(fn[0])
# # can we update single character in string 
# #fn[1] = "c"
# # can we verify particular character exist in string 
# print('C' in fn)
# # can we find length of string 
# print(len(fn))
# # how to delete string 
# del fn
# # how to loop over string - for , for -range , while loop
# lastName = "deshpande"

# # 0 1 2 3 4 5 6 7 8
# # d e s h p a n d e

# for x in lastName:
#     print(x)

# for x in range(len(lastName)):
#     #print(x)
#     print(lastName[x])

# i1 = 0
# while(i1 < len(lastName)):
#     print(i1)
#     print(lastName[i1])
#     i1 = i1 + 1

# # slicing 
# # methods


# fn = "chinmay"
# fn = 'chinmay'
# fn = """
#     I am learning js 
# """
# ln = '''
#     I am learning javascript and python
# '''

# # program 2
# city = 'pune'
# # 0  1   2   3
# # p  u   n   e
# print(city[0])

# # program 3
# city2 = "chandrapur"
# e = len(city2)
# print(e)

# # program 4
# info = "I am learning js"
# print("learning" in info) 

# # program 5
# # city4 = "goa"
# # city4[0] = "G"

# # program 6
# city = "jaipur"
# del city

# # loops 
# city8 = "nagpur"

# for x in city8:
#     print(x)

# for x in range(len(city8)):
#     #print(x)
#     print(city8[x])

# i1 = 0 
# while(i1 < len(city8)):
#     #print(i1)
#     print(city8[i1])
#     i1 = i1 + 1

#Slicing

name = "chinmay"
#            0         1         2          3        4      5 
names  = ["chinmay","sarika","shraddha","abhisha","ninad","mohan"]
#           -6        -5         -4         -3         -2       -1


# startIndex:EndIndex(not included):Steps
# 0  1  2  3  4  5   6
# c  h  i  n  m  a   y
#-7 -6 -5 -4 -3 -2  -1

# print(names[1:len(names):2])
# print(names[::3])
# print(names[::2])
# print(names[::-2])
# print(names[::-1])


# print(name[1:3])
# print(names[1:3])
# print(name[1:])
# print(names[1:])
# print(names[:len(names)])
# print(name[:len(name)])
# print(names[:4])
# print(names[-6:-1])
# print(names[-4:-2])
# print(names[-6:])
# print(names[-6:5])
# print(names[1:-2])

# 1   2   3    4     5    6    7     8     9   10   11   12 


# methods in string 
# upper()
first_name = "chinmay"
print(first_name)
e  = first_name.upper()
print(e)

# lower()
last_name = "Deshpande"
e2 = last_name .lower()
print(e2)

# captialize
middle_name = "shirish"
e3 = middle_name.capitalize()
print(e3)

# checkMethods

str1 = "chinmay"
e2 = str1.islower()
print(e2)


str2 = "CHINMAY"
e3 = str2.isupper()
print(e3)


str3 = "123"
e4 = str3.isdigit()
print(e4)

str3 = "Abc"
e5 = str3.isalpha()
print(e5)

str4 = "123asdsa"
str5 = "123"
str6 = "asd"

print(str4.isalnum())
print(str5.isalnum())
print(str6.isalnum())


str7 = "Chinmay Is Learning Js"
print(str7.istitle())


# trim methods 


str8 = " goa "
print(len(str8))

e6 = str8.strip()
print(len(e6))


str9 = " goa "
e7 = str9.lstrip()
print(len(e7))

str10 = " goa "
e8 = str10.rstrip()
print(len(e8))

str10 = "chinmay"

# 0   1   2  3  4  5  6
# c   h   i  n  m  a  y

e9 = str10.index("c")
print(e9)

str11 = "I am learnning javascript"
e10 = str11.replace("javascript","python")
print(e10)




