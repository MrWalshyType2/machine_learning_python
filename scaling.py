# Sometimes, it is difficult to compare data with different values or units of measurement.
#   - i.e. kg compared to metres???

# The answer to the problem is 'scaling', scaling data into new values that are easier to compare.

# There are different ways to scale data, but an easy to understand method is called 'standardisation':
#   z = (x - u) / s
# Where z is the new value, x is the original value, u is the mean, and s is the standard deviation

# The first entry in cars2 has a volume of 1.0, a weight of 790, and CO2 emissions of 99
#   - Scale of weight is: (790 - 1292.23) / 238.74 = -2.1
#   - Scale of volume is: (1.0 - 1.61) / 0.38 = -1.59
# -2.1 with -1.59 is easier to compare than 790 with 1.0

# Sklearn has a method called StandardScaler() which returns a Scaler obj with methods for transforming data sets.
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

dataframe = pandas.read_csv("cars2.csv")

x = dataframe[['Weight', 'Volume']]
y = dataframe['CO2']

scaledX = scale.fit_transform(x)
print(scaledX) # First two values are -2.1 and -1.59 which corresponds to the application of standardisation above

#######################################################
# Predicting CO2 with Scaled data
#   - scaled data sets require the use of the scale when predicting values

# Predict the CO2 emission from a 1.3 litre car with a weight of 2300kg
regression = linear_model.LinearRegression()
regression.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regression.predict([scaled[0]])
print(predictedCO2) # 107.2...