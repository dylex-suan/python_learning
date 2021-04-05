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