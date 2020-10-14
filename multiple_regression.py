# Multiple regression is similar to linear regression, except that we can try to predict
# a value based on two or more variables.
import pandas
from sklearn import linear_model

# The Pandas module allows the reading of csv files, which returns a DataFrame object
dataFrame = pandas.read_csv("cars.csv")

# List of independant values | What is being used for the prediction
x = dataFrame[['Weight', 'Volume']]

# Dependant value | What is being predicted
y = dataFrame['CO2']

# The sklearn LinearRegression() method creates a linear regression object
#   - The object created has a method called fit() to take the independant and dependant values
#     as parameters, then fill the object with data describing the relationship
regression = linear_model.LinearRegression()
regression.fit(x, y)

# The regression object is ready to predict CO2 values vased on a car's weight and volume
# weight = 2300kg, volume = 1300cm^3
predictedCO2 = regression.predict([[2300, 1300]])
print(predictedCO2) # Release approx. 107 grams of CO2 for every km driven


###########################################
# Coefficient
#   - A factor that describes a relationship with an unknown variable

# If x is a variable, then 2x is 2 * x. x is the unknown, 2 is the coefficient

# Get the coefficient value of weight against CO2, and for volume against CO2. The answer tells
# what happens if the weight or volume (independant values) increase or decrease.
print(regression.coef_) # [weight = 0.00755095, volume = 0.00780526]
# Tell us that increasing the weight by 1kg would increase the emissions by 0.00755095 grams