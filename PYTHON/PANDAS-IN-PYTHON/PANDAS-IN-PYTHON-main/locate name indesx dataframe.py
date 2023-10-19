#Named Indexes------>With the index argument, you can name your own indexes.

#@Add a list of names to give each row a name:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

#Locate Named Indexes----.Use the named index in the loc attribute to return the specified row(s).
#Return "day2":

#refer to the named index:
print(df.loc["day2"])