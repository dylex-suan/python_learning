# functions are similar to those of other languages
def my_function(a, b):
    return a + b

print(my_function(3, 5))

# if we don't know how many arguments are being passed, we use *
def my_function_2(*kids):
    print("The youngest child is " + kids[2])

my_function_2("Emil", "Tobias", "Dylex", "Mark")

# key_value syntax also works too
def my_function_3(child3, child2, child1): 
    print("The youngest child is " + child3)

my_function_3(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# arbitrary keyword arguments are indicated by **
def my_function_4(**kid):
    print("His last name is " + kid["lname"])

my_function_4(fname = "Tobias", lname = "Refsnes")

# recursion in functions
def factorial(num):
    if (num == 0):
        return 1
    return num * factorial(num - 1)

print(factorial(130))