# try tests a block of code for errors
# except block lets you handle the error
# finally block lets you execute the code

try:
    print(x)
except:
    print("An exception occurred")

# NameError is using a variable or a function that is not valid (uninitialized variable)
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# if no errors were raised, else goes at the end:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("nothing went wrong")

# finally block is executed regardless if there was an error
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


# for a file that is not writable
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

# raise an error and stop the program if x is lwoer than 0:
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero") # this stops the program entirely

# you define what kind of error to raise, text prints to the user

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")