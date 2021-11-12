import pandas as pd
import numpy as np

# CREATE A FEW WRONG AND RIGHT DUMMY DATAFRAMES FOR TESTING
# create dataframe with redundant primary key and null value
data_pk_null = {'id': [1, 2, 1, 3], 'Name': [np.nan, 'Joseph', 'Krish', 'John']}
df_pk_null = pd.DataFrame(data_pk_null)

# create an empty dataframe
df_empty = pd.DataFrame()

# create dataframe with null value
data_null = {'id': [1, 2, 3, 4], 'Name': [np.nan, 'Joseph', 'Krish', 'John']}
df_null = pd.DataFrame(data_null)

# create the right dataframe 1
correct_data1 = {'id': [1, 2, 3, 4], 'fname': ['Kia', 'Joseph', 'Krish', 'John'],
                 'lname': ['KA', 'JM', 'PT', 'XY'], 'cid': [100, 200, 100, 100]}
correct_df1 = pd.DataFrame(correct_data1)

# create the right dataframe 4
correct_data2 = {'id': [1, 2], 'fname': ['Japan', 'London'],
                 'lname': ['Orange', 'Apple'], 'cid': [100, 200]}
correct_df2 = pd.DataFrame(correct_data2)
