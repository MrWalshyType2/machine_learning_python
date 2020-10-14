import matplotlib.pyplot as plot

# Matplotlib has a method for drawing scatter plots.
#   - It must be passed two equal length arrays for the x & y axis

carAge = [27, 42, 2, 34, 6, 7, 1, 55]
carSpeed = [78, 56, 120, 82, 110, 108, 128, 50]

# This scatterplot shows a relationship that older cars are generally slower than newer cars.
plot.scatter(carAge, carSpeed)
plot.show()


####################################
# Random Data Distributions
# ML data sets may contain millions of values, numpy can be used to randomly generate the data for this
