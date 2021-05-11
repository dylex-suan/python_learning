# sometimes, it's harder to compare certain units of measurement
# when they don't have the same units
# we use standardization, which is done by the following 
# z = (x - u) / s.
# in Python, this is done through the sklearn module, in which
# a function called StandardScaler() which returns a Scaler object

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("./LearnMachineLearning/cars2.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]]) # predict the CO2 emission from a 1.3 liter car weighing 2300 kilograms

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)