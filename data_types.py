# A couple of built in data types
# text types: str
# numeric types: int, float, complex
# sequence types: list, tuple, range
# mapping type: dict
# set types: set, frozenset
# boolean type: bool
# binary types: bytes, bytearray, memoryview


# you use the type(x) function to get the type
x = "ALLOW"
print(type(x))

x = '20'
print(type(x))

x = 20.5
print(type(x))

x = 20
print(type(x))

x = 2 + 1j #complex
print(type(x))

x = ["apple", "banana", "cherry"]#list
print(type(x))

x = ("apple", "banana", "cherry") #tuple
print(type(x))

x = range(6)
print(type(x))

x = {"name" : "John", "age" : 36} #dict
print(type(x))

x = {"apple", "banana", "cherry"} #set
print(type(x))

x = frozenset({"apple", "banana", "cherry"}) #frozenset
print(type(x))

x = True
x = False
print(type(x))

x = b"Hello" # byte
print(type(x))
print(type(x))

x = bytearray(5) #bytearray
print(type(x))

x = memoryview(bytes(5))
print(type(x))

# specifying the data type is also useful with constructors