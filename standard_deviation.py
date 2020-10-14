import numpy
# The standard deviation is the amount of spread between values.

#   - Low standard deviation = most numbers are close to the mean (average) value
#   - High standard deviation = values are spread out over a wider range

speed = [86,87,88,86,87,85,86]
speed2 = [32,111,138,28,59,77,97]

lowDeviation = numpy.std(speed)
highDeviation = numpy.std(speed2)

print("LOW DEVIATION: ", lowDeviation)
print("HIGH DEVIATION: ", highDeviation)