# I can use floats with scientific numbers
x = 35e3 #35000.0
y = 12E4
z = -87.7e100 # e or E is used for 10^x 

print(type(x))
print(type(y))
print(type(z))

print(x)
print(y)
print(z)

x = int(35e3)
print(x) #35000

# complex numbers
x = 3 + 5j
y = 4j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# one caveat: you can't convert complex numbers into another number type


# importing random module to give a random number between
# bottomlimit and toplimit (exclusive)
import random
print(random.randrange(1, 10)) # between 1 and 9
