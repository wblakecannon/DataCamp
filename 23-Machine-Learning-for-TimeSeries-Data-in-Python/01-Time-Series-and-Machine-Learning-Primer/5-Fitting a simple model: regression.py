"""
Fitting a simple model: regression
In this exercise, you'll practice fitting a regression model using data from the Boston housing market. A DataFrame called boston is available in your workspace. It contains many variables of data (stored as columns). Can you find a relationship between the following two variables?

"AGE": proportion of owner-occupied units built prior to 1940
"RM" : average number of rooms per dwelling
"""

from sklearn.svm import LinearSVC

# Construct data for the model
X = data[['petal length (cm)', 'petal width (cm)']]
y = data[['target']]
# Fit the model
model = LinearSVC()
model.fit(X, y)