# Percentiles are numbers that describe the value of a given percent of the values are lower than.
import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# The 75th percentile of ages is 43. This means 75% of the ages are 43 or younger.
percentile75th = numpy.percentile(ages, 75)
print("AGES: ", ages)
print("75th Percentile: ", percentile75th)

percentile90th = numpy.percentile(ages, 90)
print("90th Percentile: ", percentile90th)