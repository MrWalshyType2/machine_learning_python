import numpy
# The standard deviation is the amount of spread between values.
#   - Represented by the Sigma symbol

#   - Low standard deviation = most numbers are close to the mean (average) value
#   - High standard deviation = values are spread out over a wider range

speed = [86,87,88,86,87,85,86]
speed2 = [32,111,138,28,59,77,97]

lowDeviation = numpy.std(speed)
highDeviation = numpy.std(speed2)

print("DATASET SPEED: ", speed)
print("LOW DEVIATION: ", lowDeviation)

print("\nDATASET SPEED2: ", speed2)
print("HIGH DEVIATION: ", highDeviation)

###############################################################################
# Variance is another number that indicates how spread out values are.
#   - Represented by the Sigma Square
#   - The square root of the variance is the standard deviation.
#   - The square of the standard deviation is the variance.

# STEPS:
#   - Find the mean of a data set
#   - Find the difference from the mean for each value
#   - Find the square value for each difference
#   - The variance is the average/mean of these squared differences.
highDeviationVariance = numpy.var(speed2)
print("HIGH VARIANCE: ", highDeviationVariance)