# dictionaries have keys and values
# items are ordered, changeable, and does not allow duplicates

# first item is a key, second item is the value associated
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2000,
    "year_alt": 1964
}

print(thisdict)
print(len(thisdict))

# getting the value of the model
x = thisdict["model"]
print(x)
x = thisdict["year"]
print(x)

# same functionality with get()
x = thisdict.get("model")

# if you return all of the keys in the dictionary
x = thisdict.keys()
print(x)

# adding a key
thisdict["color"] = "white"
print(x)

# if you return a list of all the values
x = thisdict.values()
print(x)

# any changes also gets reflected in the values
thisdict["year"] = 2021
print(x)
thisdict["color"] = "red"
print(x)

# getting a list of the key:value pairs
x = thisdict.items()
print(x)

# checking whether a particular key or value is in the dictionary
part_key = "model"
if part_key in thisdict:
    print("Yes, "  + part_key + " is one of the keys in the thisdict dictionary")

# in order to update a particular key:value pair, you must use update()
thisdict.update({"year": 2002})
print(thisdict)

# thisdict.update({"bran", "Toyota"}) # you cannot update a key:value pair if it doesn't exist
print(thisdict)

# to remove an item with the key name, use pop()
thisdict.pop("model")
print(thisdict)
# removing the last inserted item is done through popitem()
thisdict.popitem()
print(thisdict)

# you may remove the item with the key name
del thisdict["brand"]
print(thisdict)

# clearing the dictionary
thisdict.clear()
print(thisdict)

# looping through the dictionary is about the same
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2000,
    "year_alt": 1964
}

for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

# printing out the values
for x in thisdict.values():
    print(x)

# printing out the keys
for x in thisdict.keys():
    print(x)

# printing out the path in sync
for x, y in thisdict.items():
    print(x, y)

# copying a dictionary
mydict = thisdict.copy()
print(mydict)

# we may have multiple dictionaries in one dictionary 
myfamily = {
    "child1" : {
        "name": "Emil",
        "year": 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Dylex",
        "year": 2011
    }
}

print(myfamily)

# we can add multiple dictionaries in one dictionary
child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2001
}
newfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(newfamily)