#Read CSV Files
#A simple way to store big data sets is to use CSV files (comma separated files).

#CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

#In our examples we will be using a CSV file called 'data.csv'.

#Download data.csv. or Open data.csv

#Load the CSV into a DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 




#If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:


#Print the DataFrame without the to_string() method:

import pandas as pd

df = pd.read_csv('data.csv')

print(df) 
