# PYTHON VARIABLES
x = 5
y = "Hello World!"
# no commands for declaring a variable

# btw, no multi line comments
# This is a comment
# written in
# more than just one line

# you may choose to use a multiline string
"""
This is a comment written in
more than just one line
"""
print("Hello, World!")

# python can change the types pretty rapidly
x = 5
x = "Sally"
print(x)

# casting (allowing us to specify the data type of a variable)
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

# get the data type of a variable using type()
x = 5
y = "John"
print(type(x)) # displays <type 'int'>
print(type(y)) # <type 'str'>

# string variables can be declared either with single or double quotes
x = "John"
print(x)
# is the same as
x = 'John'
print(x)


# you can't "declare a variable", you create a variable when you assign a value to it
x = 5
y = "John" 
print(x)
print(y) # YOU CAN LITERALLY ASSIGN VARIABLES OF ANY TYPES

# specifying the data type of variable can be done through casting (same thing in Java)
x = str(3) # '3'
y = int(3) # 3
z = float(3) # 3.0

print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x)) 
print(type(y))

# obviously case sensitive characters in variables
# no numbers in the front
# no hyphens
# no spaces
# case-sensitive
# camel_case seems to be the best

# THIS IS POSSIBLE?!?!
x = y = z = "Orange"
print(x)
print(y)
print(z) # They're all the same

# Unpacking a list is also cool; you can extract the values into variables
fruits = ["apple", "banana", "cherry"]
x, a, s = fruits
print(a)
print(a)
print(s)

# output variables
x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)

# mathematical operators
x = 5
y = 10
print(x + y)

# don't combine strings and numbers
x = 5
y = "John"
# print(x + y)  # NOT GOOD

x = ("apple", "banana", "cherry")
print(type(x))
