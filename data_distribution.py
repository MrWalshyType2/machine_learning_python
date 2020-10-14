# Big data sets for testing can be created with the NumPy Python module.
import numpy
import matplotlib.pyplot as plot

# Create an array with 200 random floats between 0 and 10
myDataSet = numpy.random.uniform(0.0, 10.0, 200)
# print(myDataSet)

# Matplotlib can be used to visualise data.
# plot.hist(myDataSet, 10) # creates a histogram with 10 bars, each bar represents the amount of values in between values
# plot.show()


#######################
# Big Data Distribution
bigDataSet = numpy.random.uniform(0.0, 5.0, 1000000)
plot.hist(bigDataSet, 100)
plot.show()