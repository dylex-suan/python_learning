# File Handling
import os
"""
There are four methods to open a file:
"r" - Read
"a" - Append
"w" - Write
"x" - Create

Specify if the file should be handled as binary or text mode
"t" - Text
"b" - Binary
"""

f = open("./File_Handling/demo_for_file.txt")
# will present an error -->
# f = open("demo.txt")

f = open("./File_Handling/demo_for_file.txt", "r")
print(f.read())

# return the first 5 characters of the file
f = open("./File_Handling/demo_for_file.txt", "r") # declare this every single time you read it
print(f.read(5))

f = open("./File_Handling/demo_for_file.txt", "r")
print(f.readline()) # reading two lines
print(f.readline())

f = open("./File_Handling/demo_for_file.txt", "r")
for x in f:
    print(x) # loop through the file line by line

f.close()

f = open("./File_Handling/demo_for_file.txt", "a")
# If we want to write more lines in an existing file
f.write("Now the file has more content!")
f.close()

# open and read the file after appending
f = open("./File_Handling/demo_for_file.txt", "r")
print(f.read())

# overwrite the content
f = open("./File_Handling/demo_for_file.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after appending:
f = open("./File_Handling/demo_for_file.txt", "r")
print(f.read())

# f = open("./File_Handling/myfile.txt", "x")
f = open("./File_Handling/myfile.txt", "w")


# removing myfile.txt requires us to use os.remove
if os.path.exists("./File_Handling/myfile.txt"):
    os.remove("./File_Handling/myfile.txt")
else:
    print("The file does not exist")