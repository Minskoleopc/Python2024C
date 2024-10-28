# text = "hello"
# print(text.upper())


# text2 = "Hello"
# print(text2.lower())


# text3 = "learningNew"
# print(text3.capitalize())


# text4 =  "I am learning js"
# print(text4.title())



# program 1

# strip()

first_name = " amol "
print(first_name)
print(len(first_name))
e = first_name.strip()
print(len(e))

# rstrip()
first_name = " amol "
print(len(first_name))
f = first_name.rstrip()
print(len(f))
# lstrip()
first_name = " amol"
print(len(first_name))
g = first_name.lstrip()
print(len(g))
# " amol " ----> strip -- r strip  -----> lstrip

# program 2

info = "I am learning javascript"
e = info.replace("javascript","python")
print(e)


info2 = "I am learaning javascript and javascript is good langauge"
e2 = info2.split(" ")
print(e2)

firstName = "chinmaydeshpande"
e3 = firstName.split('a')
print(e3)
#["chinm","ydeshp","nde"]

e = ["I" ,"like","python","language"]
# I like python language
e4 = " ".join(e)
print(e4)

e5 = ["chinmay","gmail.com"]
e6 = "@".join(e5)
print(e6)

# program 3

fn = "chinmay"
ln = "deshpande"
text = f"My name is {fn} and lastName is {ln}"
print(text)
e7 =  "My name is {firstName} and lastName is {lastName}".format(firstName=fn,lastName = ln)
print(e7)

# program 5
# character type check
print("aasdas".isalpha())
print("32".isdigit())
print("234ad".isalnum())
print("234".isalnum())
print("asd".isalnum())
print("        ".isspace())

# program 6
print("dsad".islower())
print("DSAD".isupper())
print("Deshpande Chinmay Shirish".istitle())

















