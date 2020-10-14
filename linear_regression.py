# Regression is the term used when trying to find the relationship between variables.
#   - ML and Statistical Modelling use the relationship to predict the outcome of future events

# Linear regression draws a straight line through data points to show the relationship. The line can
# be used for predicting future values.
import matplotlib.pyplot as plot
from scipy import stats

carAge = [27, 42, 2, 34, 6, 7, 1, 55]
carSpeed = [78, 56, 120, 82, 110, 108, 128, 50]

# Key values for Linear Regression
slope, intercept, r, p, std_err = stats.linregress(carAge, carSpeed)

# Gets the position on the y-axis that a corresponding x value will be placed
def getXPosOnY(x):
    return slope * x + intercept

# Map each value of carAge through the func to get a new array with new values for the y-axis
my_model = list(map(getXPosOnY, carAge))

# This scatterplot shows a relationship that older cars are generally slower than newer cars.
# plot.scatter(carAge, carSpeed)

# Draw the line of linear regression
# plot.plot(carAge, my_model)

# plot.show()


# R/r = coefficient of correlation (ranges from 0 to 1, 0 = no relationship, 100 = 100% relation)
#   - The relationship between the x-axis and y-axis values is important for prediction in linear regression.

# We can also predict future values, lets predict the speed of a 30 year old car:
someCarsSpeed = getXPosOnY(30)
print(someCarsSpeed) # approx. 80