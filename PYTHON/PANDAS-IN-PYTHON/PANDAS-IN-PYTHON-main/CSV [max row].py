#max_rows
#The number of rows returned is defined in Pandas option settings.

#You can check your system's maximum rows with the pd.options.display.max_rows statement.


#Check the number of maximum returned rows:

import pandas as pd

print(pd.options.display.max_rows) 
#In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

#You can change the maximum rows number with the same statement.


#Increase the maximum number of rows to display the entire DataFrame:

import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df) 
