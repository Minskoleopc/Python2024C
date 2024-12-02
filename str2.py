# captialize
fn = "chinmay"
print(fn.capitalize())

#upper()
print(fn.upper())

# lower()
ln = "deshpande"
print(ln.lower())

#swapcase
city = "Pune"
print(city.swapcase())

# title
info = "I am learning js"
print(info.title())

# string alignment
# center
text = "hello"
t = text.center(15,"-") # -----hello-----
print(t)


# ljust()
text = "hello"
t = text.ljust(15,"-") 
print(t)

# rjust()
text = "hello"
t = text.rjust(15,"-") 
print(t)

text = "42"
t = text.zfill(10)
print(t)


# Substring
h = "chinmaya" # string
h = h.count('a')
print(h)

# find()

text = "chinmay"
r = text.find('A')
print(r)

text = "chinmaya"
r = text.find('a')
print(r)

r = text.rfind('a')
print(r)

#index()

text = "banana"
# 0  1  2  3  4   5
# b  a  n  a  n   a

print(text[0])
e1 = text.index("a")
e2 = text.index("a",2)
print(e1)
print(e2)


#startswith()
city = "pune"
print(city)
print(city[0])
e2 = city.startswith("p")
print(e2)

f = city.startswith("pu")
print(f)

# endswith()
city2 = "mumbai"
e3 = city2.endswith("i")
e4 = city2.endswith("aI")
print(e3)
print(e4)


# strip()
ea = " goa "
print(len(ea))
ea = ea.strip()
print(len(ea))

# lstrip()

ea = " goa"
print(len(ea)) # 4
ea = ea.lstrip()
print(len(ea))

# rstrip()
ea = " goa "
print(len(ea)) # 5
ea = ea.rstrip()
print(len(ea)) #4

# replace()

mtext  = "I am  learning javascript"
q = mtext.replace("javascript","python")
print(q)

# split()
email = "chinmaydeshpande@gmail.com"
f = email.split("@")
print(f)
print(type(f))
#["chinmaydeshpande","gmail.com"]

text2 = "hello world"
f2 = text2.split(" ") #["hello","world"]
print(f2)

# join()
r1 = ["chinmaydeshpande","gmail.com"]
f3 = "@".join(r1)
print(f3)

r2 = ["apple","mango","banana"]
f4 = "-".join(r2)
print(f4) # apple-mango-banana

r3 = f4.split('-') #["apple","mango","banana"]
print(r3)