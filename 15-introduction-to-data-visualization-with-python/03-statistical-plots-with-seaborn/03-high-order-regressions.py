'''
Higher-order regressions

When there are more complex relationships between two variables, a simple first order regression is often not sufficient to accurately capture the relationship between the variables. Seaborn makes it simple to compute and visualize regressions of varying orders.

Here, you will plot a second order regression between the horse power ('hp') and miles per gallon ('mpg') using sns.regplot() (the function sns.lmplot() is a higher-level interface to sns.regplot()). However, before plotting this relationship, compare how the residual changes depending on the order of the regression. Does a second order regression perform significantly better than a simple linear regression?

A principal difference between sns.lmplot() and sns.regplot() is the way in which matplotlib options are passed (sns.regplot() is more permissive).
For both sns.lmplot() and sns.regplot(), the keyword order is used to control the order of polynomial regression.
The function sns.regplot() uses the argument scatter=None to prevent plotting the scatter plot points again.
INSTRUCTIONS
100XP
Modify the call to plt.scatter() to plot auto['weight'] on the x-axis and auto['mpg'] on the y-axis, filled with red circles and with label='data'.
Plot a linear regression line of 'order 1' between 'weight' and 'mpg' in 'blue' without the scatter points.
You need to specify the label and color parameters, in addition to scatter=None.
Plot a linear regression line of 'order 2' between 'weight' and 'mpg' in 'green' without the scatter points.
To force a higher order regression, you need to specify the order parameter. Here, it should be 2.
Add a legend to the 'upper right'.
'''
# Generate a scatter plot of 'weight' and 'mpg' using red circles
plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')

# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, color='blue', label='First Order')

# Plot in green a linear regression of order 2 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, order=2, color='green', label='Second Order')

# Add a legend and display the plot
plt.legend(loc='upper right')
plt.show()
