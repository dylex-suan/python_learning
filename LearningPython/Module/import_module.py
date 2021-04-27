# import mymodule
# we can import mymodule, but use a different name for it
import mymodule as mx
import platform

mx.greeting("Jonathan")
a = mx.person1["age"]
print(a)

x = platform.system()
print(x) # what system are you using?
x = dir(platform)
print(x) # all the function names in a module
