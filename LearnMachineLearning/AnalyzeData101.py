# need for mean and for median
import numpy

# need for mode
from scipy import stats

"""
To note, we deal with three data types:

Numerical: (numbers which are either limited to integers (discrete),
            or can involve numbers of infinite value (continuous))
Categorical: values that can't be measured up against each other (color value, yes/no values, etc)
Ordinal: categorical data which CAN be measured up against each other
         (school grades where A is better than B)
"""


# Investigating average with mean
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.mean(speed)
print(x)

# Investigating average with median (important to sort it first)
x = numpy.median(speed)
print(int(x))

# Evidently, you divide the sum of the numbers by two
speed = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]
x = numpy.median(speed)
print(x)

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = stats.mode(speed)
print(x)  # returns ModeResult(mode=array([86]), count=array([3]))

