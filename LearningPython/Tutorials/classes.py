# classes were like structures, can be used to rewrite stuff
class Person:
    # constructor function
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)


# note how we don't have the self argument, that gets added in, almmost like this
p1 = Person("Dylex", 18)

print(p1.name)
print(p1.age)

p1.myfunc()

# but self need not to be used all the time, we can replace self with something
# else, so long as that is the first parameter of any function in the class:
class Person_2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self): # abc could be anything too!
        print("Hello my name is " + self.name)

p1 = Person_2("Mark", 24)
p1.myfunc()

print(p1.age)
# changing parts of the class is also fine
p1.age = 40
print(p1.age)

# deleting the age property from p1:
del p1.age
print(p1) # prints out the memory address
# deleting the p1 object
del p1

class Person_3:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

x = Person_3("Dylex", "Suan")
x.printname()

# creating a child class just means passing the parent object as a parameter
class Child(Person_3):
    # note that when we add the init function to this class,
    # the child class no longer take the __init__ in Person3()
    # in order to keep the inheritance of the parent's __init__() function, add a call to the parent's
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
    def minute(self):
        print("The child is Mike")

x = Child("Mike", "Olsen")

x.minute()

# we can also force inherit all the methods and properties from its parent:
class Student(Person_3):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019


x = Student("John", "Doe")
x.printname()

class Student_2(Person_3):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


# adding a method in the child class with the same name as a function in the parent class
# will make the inheritance of the parent method overridden
x = Student_2("Dylex", "Suan", 2020)
x.printname()
