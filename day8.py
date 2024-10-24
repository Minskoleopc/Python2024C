
# fn = "chinmay"
# print(fn)

# ln = 'deshpande'
# print(ln)

# mn = """
#     This is multi-line string 
#     over the period
# """

# mn2 = '''
#     This is multiline string over the duration
# '''

# print(type(ln))
# print(type(mn))
# print(type(mn2))
# print(type(fn))


# program 2
# string stores the value by index  - yes
city2 = "pune"
#  0    1     2     3
#  p    u     n     e
print(city2[0])
print(city2[1])

# program 3
# check particular "ch" exist in string 
name2 = "chinmay"
# 0 1  2  3  4  5  6
#c  h  i  n  m  a  y
print("c" in city2)
print("C" in city2)
print('chi' in city2)

# program 4
name3 = "sarika"
e = len(name3)
print(e)

# program5
# name3 = "mitesh"

# # 0 1 2 3 4 5
# # m i t e s h

# # for loop - range
# for x in range(len(name3)):
#     print(x)
#     print(name3[x])

# # for without range 
# for x in name3:
#     print(x)

# # while loop

# i1 = 0 
# while(i1 < len(name3)):
#     #print(i1)
#     print(name3[i1])
#     i1 = i1 + 1

# program 6


city1 = "pune"
e = city1.upper()
print(e)

city2 = "PUNE"
e2 = city2.lower()
print(e2)

city3 = "pune"
e3 = city3.capitalize()
print(e3)

city4 = "pune"
e4 = city4.islower()
print(e4)

city5 = "PUNE"
e5 = city5.isupper()
print(e5)


info6 = "I Am Leaning javascript"
e3 = info6.istitle()
print(e3)

# 0  1  2  3 4 5 6 7 8 9
info7 = "123a"
e4 = info7.isdigit()
print(e4)

info8 = "asd1"
e5 = info8.isalpha()
print(e5)


info9 = "123ASD"
info10 = "123"
info11 = "sadasd"
e6 = info9.isalnum()
print(e6)
e7 = info10.isalnum()
e8 = info11.isalnum()
print(e6)
print(e7)
print(e8)













