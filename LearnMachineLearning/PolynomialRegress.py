import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,50,60,65,70,70,75,76,78,79,90,99,99,100]

plt.scatter(x,y)
plt.show()

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3)) # allows us to make a polynomial model
myline = numpy.linspace(1,22,100) # specify how the line will display, we start at position1 and end at position 22
plt.scatter(x,y) # draw the original scatter plot
plt.plot(myline,mymodel(myline)) # draw the line of polynomial regression
plt.show() # display the diagram

# to see how well my data fits in a polynomial regression
print(r2_score(y, mymodel(x)))
# very good relationship! yay!

speed = mymodel(17)
print(speed)

# bad fit? polynomial regression may not work
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(2, 95, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# looking at the r-squared value
print(r2_score(y, mymodel(x))) # not good relationship < 0.009