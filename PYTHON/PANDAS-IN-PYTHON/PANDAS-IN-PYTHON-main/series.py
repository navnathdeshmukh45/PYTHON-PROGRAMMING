#What is a Series?
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.
# Example
# Create a simple Pandas Series from a list:

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
#Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.

#Example
#Return the first value of the Series:

print(myvar[0])
#Create Labels
#With the index argument, you can name your own labels.

#example
#Create you own labels:

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
#When you have created labels, you can access an item by referring to the label.

#Example
#Return the value of "y":

print(myvar["y"])



#Key/Value Objects as Series
#You can also use a key/value object, like a dictionary, when creating a Series.

#Example
#Create a simple Pandas Series from a dictionary:

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)








