mytuple = ("apple", "banana", "cherry")

# Creating a tuple: multiple values allowed too!
thistuple = ("apple", "banana", "cherry", "banana", "apple")
print(thistuple)
# once the tuple is created, we can't add or remove items
print(len(thistuple))

# for one item tuples, remember the commas
thistuple = ("apple", )
print(type(thistuple))

# although you can't change tuple values directly, you can instead
# convert tuples into lists, change the list, then convert
# it back to a tuple
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y) # this converts x back into the tuple

print(x)

# you also can't remove items from a tuple, but
# you can change or add tuple items in the same manner as above
thistupple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)


# we can extract values back into variables if we wanted to
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# only use asterisks if we know there are less variables than number of values
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)
