import pandas
from sklearn import linear_model

# we can read csv files and return a DataFrame 
df = pandas.read_csv("./LearnMachineLearning/cars.csv")

# make a list of the independent values and call this variable X
# put the dependent values in a variable called y
# note that it's normla to have independent values as capital case X
# and dependent values listed with a lower case y
X = df[['Weight', 'Volume']]
y = df['CO2']

# sklearn module, we use LinearRegression() method to create
# a linear regression object
regr = linear_model.LinearRegression()
regr.fit(X, y)

# predict the CO2 emission of a car where weight is 2300 kg, and volume is 1300 cubic cm
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)
# essentially, we predict that a car with 1.3 L engine, and a weight of 2300 kg will release
# 107 grams of C02 for every kilometer it drives

print(regr.coef_)
"""
Essentially, we ask for the coefficient value of WEIGHT against CO2, and VOLUME against CO2.
The coefficient values of weight and volume are different, in that these
values tell us if the weight increases by 1kg, the CO2 emission increases by 0.00755g.
Similarly, if the engine volume increases by 1 cubic cm, CO2 emission increases by 0.00780526g.
"""

predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2)