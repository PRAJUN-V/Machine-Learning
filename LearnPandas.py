# https://www.w3schools.com/python/pandas/default.asp

import pandas as pd

mydataset = {
    'name': ['Prajun', 'Arjun', 'Akhil'],
    'age': [23, 21, 26],
    'department': ['Physics', 'Chemistry', 'BBA']
}

c = pd.DataFrame(mydataset)
# The DataFrame method in pandas is used to create a DataFrame,
# which is a two-dimensional, size-mutable, and potentially
# heterogeneous tabular data structure with labeled axes (rows and columns).
# A DataFrame is similar to a table in a database or an Excel spreadsheet.

# DataFrame covert dict to tabular form
# print(c)
# print(type(c))  # <class 'pandas.core.frame.DataFrame'>

# print(pd.__version__)

# Just refer https://www.w3schools.com/python/pandas/default.asp for more info
