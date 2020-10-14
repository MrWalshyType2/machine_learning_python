# A decision tree is a flow chart to help make decisions based on previous experiences.

# This example will have a person decide if he/she would go to a comedy show or not.
#   - The example person has registered some useful information in a csv file for this purpose.
# AGE, EXPERIENCE, RANK, NATIONALITY, GO

# Using the supplied data set, Python can create a decision tree to decide if any new shows are worth attending.
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plot
import matplotlib.image as pltimg

# Lines 16 to 18 are required for Graphiz to be found and used for creating the decision tree
import os
path_graphviz = "C:/Program Files/Graphviz 2.44.1/bin" # replace by your Graphviz bin path
os.environ["PATH"] += os.pathsep + path_graphviz

dataframe = pandas.read_csv("shows.csv")

print(dataframe)

# Decision trees are made from numerical data
#   - Non numerical columns Nationality and Go should be turned into numerical values
#   - The Pandas map() method takes a dictionary with info on how to convert the values
nationalities = {"UK": 0, "USA": 1, "N": 2}
go = {"YES": 1, "NO": 0}

dataframe["Nationality"] = dataframe["Nationality"].map(nationalities)
dataframe["Go"] = dataframe["Go"].map(go)

print(dataframe)


# Now, the feature columns should be separated from the target column
#   - Feature columns are columns that are predicted from
#   - Target column is the column with values that are to be predicted
features = ['Age', 'Experience', 'Rank', 'Nationality']
featureColsX = dataframe[features]
targetColY = dataframe["Go"]
# print(featureColsX)
# print(targetColY)


# Create a decision tree, save it as an image, show the image
decisionTree = DecisionTreeClassifier()
decisionTree = decisionTree.fit(featureColsX, targetColY)
data = tree.export_graphviz(decisionTree, out_file=None, feature_names=features)

graph = pydotplus.graph_from_dot_data(data)
graph.write_png("mydecisiontree.png")

img = pltimg.imread("mydecisiontree.png")
imgplot = plot.imshow(img)
plot.show()


###########################################################
# Predicting values with the Decision Tree
#   - Should I go to see a show starring a 25 years old British comedian, with 13 years of experience and
#     a comedy ranking of 8
print(decisionTree.predict([[25, 13, 8, 0]])) # [1] = YES most times, but the answer may vary