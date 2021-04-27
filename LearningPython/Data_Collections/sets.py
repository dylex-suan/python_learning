# sets are collections of data that are both unordered and unindexed
# we don't know what order the items will appear

# once a set is created, you can't change its items, but you can add new items
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # duplicates are ignored

# looping through the set is the same with lists and tuples
print("banana" in thisset)

# adding an item
thisset.add("orange")
print(thisset)

# adding sets
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# update need not have a set argument, it could be a list, tuple, or even a dictionary
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# remove items are similar
thisset.remove("kiwi") # this will raise an error if the item to remove doesn't exist
print(thisset)

thisset.discard("kiwi") # this will not
print(thisset)

# if you use the pop method, you won't know which item gets removed
x = thisset.pop()
print(x) # it's why you print out this first
print(thisset)

thisset.clear()
print(thisset)

del thisset # deletes the set completely

# might add intersection later