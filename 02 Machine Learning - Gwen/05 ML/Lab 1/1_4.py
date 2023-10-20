# 1.4 Data from External Sources

# The pandas module provides tools for reading data from common formats such as CSV, Excel, JSON and SQL
# and returns a DataFrame object.
# In the following programme we read in data from a CSV file "census.data" – the variable data is of the type DataFrame.

import pandas as pd

# .csv file has no header that names the columns, so we pass header=None and explicitly specify the column names in "names".
data = pd.read_csv("./census.data", header=None, index_col=False,
                   names=['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
                          'relationship', 'race', 'gender', 'capital-gain', 'capital-loss', 'hours-per-week',
                          'native-country', 'income'])

# select some columns
reduced_data = data[['age', 'workclass', 'education', 'income']]
# Output the data
print(reduced_data)

# Reminder: In a DataFrame, you can access individual columns via the names of the features (note the double brackets):
# reduced_data = data[['age', 'workclass', 'education', 'income']]
# The variable reduced_data is still of the type DataFrame.

# With the help of the loc function, we also have the option of specifying the start and end features
# when reading the data from a DataFrame. We can, e.g., use it here to extract all the input variables
# for our machine learning algorithm (starting with 'age' and ending with 'native-country').

# using loc() to extract a slice of the DataFrame by specify start and end features.
data_input = data.loc[:, 'age':'native-country']
print(data_input)


# The algorithms of the scikit-learn project usually work with NumPy arrays for features X and target variables y.
# An extraction of the features from a DataFrame as a NumPy array is easily possible via the attribute values.
# In the following example, we extract all input variables from the DataFrame data using loc,
# and then apply values to convert them into a numpy array:

# Convert a DataFrame to NumPy array data_input_num
data_input_num = data.loc[:, 'age':'native-country'].values
print(data_input_num)


# Analogously, we can separately extract the target variable income as a numpy array
# to use it in a machine learning algorithm of scikit-learn:
data_target_num = data[["income"]].values
print(data_target_num)


