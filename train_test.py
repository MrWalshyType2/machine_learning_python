# ML uses models to predict outcomes of certain events.
#   - How good the model is can be measured using the Train/Test method.

#########################################################
# What is Train/Test?
#   - A method to measure a models accuracy
#   - Data is split into two sets: a training set (80%) and a testing set (20%)

# Train the model = Create the model
# Test the model  = Test the models accuracy
import numpy
import matplotlib.pyplot as plot
from sklearn.metrics import r2_score
numpy.random.seed(2)

# The data set will illustrate 100 customers shopping habits in a shop
minutesBeforePurchaseX = numpy.random.normal(3, 1, 100) # mean = 3 minutes, sd = 1
moneySpentY = numpy.random.normal(150, 40, 100) / minutesBeforePurchaseX

plot.scatter(minutesBeforePurchaseX, moneySpentY)
plot.title("Original Data")
plot.show()

######################################################
# Split into Train/Test
#   - training set = random selection of 80% of the original data
#   - testing set  = remaining 20%
train_x = minutesBeforePurchaseX[:80]
train_y = moneySpentY[:80]

test_x = minutesBeforePurchaseX[80:]
test_y = moneySpentY[80:]

plot.scatter(train_x, train_y)
plot.title("Training data")
plot.show()

plot.scatter(test_x, test_y)
plot.title("Testing data")
plot.show()


########################################################
# Fitting the data set
#   - The data set appears to best fit a polynomial regression
#   - The polynomial regression line overfits the dataset, weird results could be given for time greater than 6 minutes
my_model = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
my_line = numpy.linspace(0, 6, 100)

plot.scatter(train_x, train_y)
plot.plot(my_line, my_model(my_line))
plot.title("Polynomial line of Regression")
plot.show()


########################################################
# R2
#   - R2, R-squared, measures the relationship between the x and y axis
#   - Use the skearn method called r2_score() to find the relationship

# Measure the relationship between the minutes a customer stays in the shop and how much money they spend.
#   - How well does the training data fit in a polynomial regression? 0.79... shows an OK relationship
trainR2Score = r2_score(train_y, my_model(train_x))
print("TRAIN DATA R2 SCORE: ", trainR2Score) # 0.7988645544629797

# Lets find the R2 score for the testing data
testR2Score = r2_score(test_y, my_model(test_x))
print("TEST DATA R2 SCORE: ", testR2Score) # 0.8086921460343581

# The testing datas R2 score of 0.809... shows the model fits the testing set.
#   - This means the model can be confidently used to predict future values

###########################################################
# Predict values
# How much money will a buying customer spend if they stay in the for 5 minutes?
print("CUSTOMER IN SHOP, 5 MINUTES, SPENDS: ", my_model(5)) # approx 22.88 which matches the polynomial regression