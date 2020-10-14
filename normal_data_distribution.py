# When values are concentrated around a given value, it is known as the normal data distribution.
#   - According to Probability theory
#   - Also known as the Gaussian data distribution

import numpy
import matplotlib.pyplot as plot

mySet = numpy.random.normal(5.0, 1.0, 100000) # (mean, standard-deviation, size)

plot.hist(mySet, 100)
plot.show()