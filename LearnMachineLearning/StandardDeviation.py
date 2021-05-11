import numpy

"""
Standard deviation refers to the spread of the values; how spread are they
with relation to the mean. We use numpy to calculate this. Represented
by sigma.

Variance is another number that indicates how spread out the values are;
also related since standard deviation is the square root of the variance. Represented
by sigma squared.
"""


# standard deviation
speed = [86, 87, 88, 86, 87, 85, 86] # standard deviation is 0.9
x = numpy.std(speed)
print(x)

speed = [32, 111, 138, 28, 59, 77, 97]
x = numpy.std(speed)
print(x)

# variance
x = numpy.var(speed)
print(x)

"""
We bring into question, percentiles, which describes the value a given
percent of the values are lower than. So when we say, the 75th percentile,
we are referring to 75% of the population who are of this statistic or younger/lower, etc.

"""
# question, what is the age that 90% of the people are younger than?
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80,
        82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
x = numpy.percentile(ages, 90)
print(x)