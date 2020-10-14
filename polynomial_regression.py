# If data does not fit a linear regression (straight line), it may be better to use polynomial regression.
#   - Polynomial regressions uses the relationship between the x and y axis vars to find the best way to draw
#     a line through data points on a graph.
import matplotlib.pyplot as plot
import numpy
from sklearn.metrics import r2_score

hourOfDay = [1,2,3,4,5,6,7,8,9,10,11,12] # PM values
carSpeeds = [85, 90, 70, 70, 65, 75, 80, 85, 80, 90, 110, 105]

# Make a polynomial model
my_model = numpy.poly1d(numpy.polyfit(hourOfDay, carSpeeds, 3))

# specify how the line will display
my_line = numpy.linspace(1, 12, 100)

# plot.scatter(hourOfDay, carSpeeds)
# plot.plot(my_line, my_model(my_line))
# plot.show()

###################################
# R-Squared
#   - The measurement for the relationship
#   - Ranges from 0 to 1, 0 = no relationship, 1 = 100% related
#   - Can be computed with the Sklearn module
print(r2_score(carSpeeds, my_model(hourOfDay))) # approx. 0.82

# Try to predict the speed of a car passing at 2PM
predictedSpeed = my_model(3)
print(predictedSpeed) # 74.02...