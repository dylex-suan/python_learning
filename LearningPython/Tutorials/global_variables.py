# Global variables

x = "awesome"
y = "heck yeah"

def myfunc():
    x = "fantastic" # only used within the function
    print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc2():
    global xx # will be global, and will belong to the global scope
    xx = "fantastic"

myfunc2() # this allows for the variable to be initialized

print("python is " + xx)



