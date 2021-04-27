# Strings
a = "Hello, World"
print(a[2])

for x in "banana":
    print(x + " ")

print(len(a))

# check if a certain phrase is in a string
txt = "The best things in life are free!"
print("free" in txt)
print("not free" in txt)

# printing stuff if only free is present
txt = "The best things in life are free"
if "free" in txt:
    print("yes, 'free' is present.")
elif "not free" in txt:
    print("yes, 'not free' is present.")

if "free" in txt: print("yes, 'free' is present.")

a = 200
b = 33
print("A") if a > b else print("B")

c = 5000
if a > b and c > a:
    print("Both conditions are True")

if a > b or a > c:
    print("At least one of the conditions is True")

x = 41
if x > 10:
    print("Above ten, ")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


# pass statement: if statement with no content
a = 33
b = 200
if b > a:
    pass

# check if not
if "free" not in txt:
    print("Yes, 'expensive' is NOT present")

# slicing strings
b = "Hello, World!"
print(b[2:5]) # slicing from index 2 to index 5
print(b[:5]) # slicing from the beginning

# negative indexing: used for indexes starting from the end of the string
print(b[-5:-2]) # note that when we count from the end, it starts at -1

# upper_case
a = "Hello, World!"
print(a.upper())

# lower_case
a = "Hello, World!"
print(a.lower())

# strips the whitespace from the beginning to the end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# replace method repalces a string with another string
a = "Hello, World"
print(a. replace("H", "J"))

a = "Hello, World"
print(a.split(",")) # returns ['Hello', ' World!'] # splits the string into substrings
# IF we can find the character we want to use to separate

# concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)

# no combining strings and numbers like this
# txt = "My name is John, and I am " + age

# format() method
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# all in order
quantity = 3
itemnum = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemnum, price))

# index numbers work so that we can make sure they are placed
# in the right arguments
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemnum, price))

# most of the signs are the same except for exponentation
print(2 ** 3) # 2^3
print(2.5 // 3) # 0

