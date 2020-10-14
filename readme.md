# Python Machine Learning
This repository acts to demonstrate the basics of machine learning.

# Dependencies
- Python 3.8
- Pandas
- Sklearn
- Pydotplus
- Matplotlib

# Decision Tree Example Explained
- Rank <= 6.5 means every comedian with a rank of 6.5 or lower is True, the rest is False
- gini = 0.497 refers to the quality of the split. Always a num between 0.0 and 0.5 where 0.0 means all samples got the same result, and 0.5 means the split is done exactly in the middle.
- samples = 13 means that there are 13 comedians left at this point of the decision
- value = [6, 7] means that 6 comedians get a NO and 7 comedians get a GO

## The GINI method
The Gini method uses the formula:
- Gini = 1 - (x/n)^2 - (y/n)^2
- x = num of positive answers, n = num of samples, y = num of negative anwers