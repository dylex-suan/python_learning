# LISTS can contain any type of variable
list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1)) # class of list
# allows duplicate members

print(list1[0]) # abc
print(list1[-2]) # 40
print(list1[-5:-2]) #['abc', 34, True]
print(list1[:4]) # everything but "male"
print(list1[2:]) # everything but "abc" and 34
# the number in the second index is non-inclusive

wordcover = "abc"
if wordcover in list1:
    print(wordcover + " is in this list!")

# changing item values, multiple ways of doing it
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist[0:2] = ["cherry", "manna"]
print(thislist)
thislist.insert(2, "watermelon") # insert in between manna and cherry
print(thislist)
thislist.append("orange") # append orange to the end of the list
thislist.insert(1, "orange") # adds orange to the first index, and pushes everything back
print(thislist)
# appending other lists to the end
tropical = ["mango", "papaya", "dragonfruit"]
thislist.extend(tropical)
print(thislist)

# you can add any iterable object to the end
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# thislist.remove("popular") # it's not in this list so we should use an if statement
if "popular" in thislist:
    thislist.remove("popular")

thislist.remove("orange")
print(thislist)
thislist.pop(1) # pops the second item off the list
print(thislist) 
thislist.pop() # removes the last item
print(thislist)

# del is also useful
thislist = ["apple", "banana", "cherry"]
del thislist[0] # removes the first item
print(thislist)
del thislist # we delete the entire list
 # can no longer run this: print(thislist), because it's not defined

thislist = ["apple", "banana", "cherry"]
thislist.clear() # clears the contents, but doesn't undefine thislist
print(thislist)