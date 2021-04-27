# we may choose to import only person1 dictionary from module
from mymodule import person1
print(person1["age"])

import datetime

x = datetime.datetime.now()
print(x) # the current date
# year
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17) # this has the automatic time of midnight (value is 0)
print(x)

# name of the month
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))