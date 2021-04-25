# we have if, elif and else
a = 200
b = 2003
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

print("a is greater than b") if a > b else print("B") # ternary operators

# and
if a > b and a < b:
    print("this statement is impossible to reach")
elif a > b or a < b:
    print("a and b are not the same number")
else:
    print("a and b are equal")


# for while loops, we can run a block of code once when the condition is no longer true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# looping through the list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# exit the loop when x is the banana
for x in fruits:
    print(x)
    if x == "banana":
        break
    print(x)

# continue statement, we stop the current iteration of the loop
# and proceed onwards
for x in fruits:
    if x == "banana":
        continue
    print(x)

# we may use range to iterate through a specified number of times
for x in range(6):
    print(x)

print("\n")

# using a start parameter is also possible too:
for x in range(2, 10):
    print(x)

print("\n")
# increment everytime we iterate by a specific value is also possible
for x in range(2, 30, 3):
    print(x)

print("\n")

# else in for loop is also possible
for x in range(6):
    print(x)
else:
    print("finally finished!")

# we will NOT execute the else block if we end up stopping the loop by a break statement
for x in range(0, 56, 3):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

# pass is used if there's nothing inside the loop whatsoever
for x in [0, 1, 2]:
    pass