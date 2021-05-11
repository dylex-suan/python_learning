"""
Big Data Sets refer to NumPy which allows to create 
random data sets of any size.
"""

import numpy
import matplotlib.pyplot as plt 
from scipy import stats

# uniform distributions tend to have the same number of elements
# over the entire domain
x = numpy.random.uniform(0.0, 5.0, 2500000) # uniform distribution of 250 elements
# that are between 0 and 5
print(x)

plt.hist(x, 100) # draws a histogram
plt.show() # shows it when it's run

# bell curve is mainly demonstrated in a normal data distribution
x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()

# we should see that most of the values are concentrated
# around 5.0 and the standard deviation is 1.0

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y)
plt.show()

# this method returns some important key values of Linear Regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y) # plot the scatter plot
plt.plot(x, mymodel) # draw the line of the linear regression
plt.show() # show it

# r is the relationship between the value of the x-axis and the values of the y-axis
# 0 means there is no relationship
# and abs(1) means 100% related
print(r)

# predicting the speed of a 10 years old car
speed = myfunc(10)
print(speed)

# random data distributions
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()


# for any bad fit, we know that linear regression wouldn't be the best method
# to predict future values
x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20,
     26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10,
     26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc_2(x):
  return slope * x + intercept

mymodel = list(map(myfunc_2, x)) 

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
# ~ 0.01, which means it's a very bad relationship
print(r)