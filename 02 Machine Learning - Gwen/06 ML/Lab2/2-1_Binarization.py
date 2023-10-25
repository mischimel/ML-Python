"""
2-1_Binarization.py
How to make categorical variables numerical
"""

import pandas as pd

# Import the census data set again:
data = pd.read_csv('census.data', header=None, index_col=False,
                   names=['age', 'workclass', 'fnlwgt',
                            'education', 'education-num', 'marital- status', 'occupation',
                            'relationship', 'race', 'gender', 'capital-gain',
                            'capital-loss', 'hours-per-week', 'native-country', 'income'])

# We select a subset of features
my_data = data[['age', 'workclass', 'gender', 'income']]

# The function head() returns the first n rows of your DataFrame.
    # It is useful for quickly checkin how your data set looks.
    # Alternatively, you can also view it in the 'Data' tab of the SciView Window.
    # (Notice that you need to activate 'Scintific Mode' In PyCharm professional to see the SciView Window.)
my_data.head()

# The method info() prints information about a DataFrame,
    # such as the column names, their data types and non-null values.
my_data.info()
    # We see from the Dtype that age is numerical variable while
    # workclass, gender and income are categorical variables.

# The method describe() prints a summary statistics of the variables in a DataFrame.
    # describe() includes only numerical data by default.
    # To include both, numerical and categorical variables, we must use the include argument:
my_data.describe(include='all')
    # unique tells us the number of unique values of the categorical variables.
    # E.g., gender has 2 unique values (namely Male and Female)

# get_dummies() transforms the categorical variables into binary variables
my_data_numerical = pd.get_dummies(my_data)
my_data_numerical.head()
    # We dont see much here, since Python does not show all the columns.
    # Better check it in the SciView Window.
    # Notice that the variable age has not been touched by get_dummies(), since it is numerical.
my_data_numerical.info()
    # Here we see that we have more variables after the transformation, and all varibales are numerical.
    # E.g., gender has been split up in 2 variables (gender_ Female and gender_ Male),
    # because the original variable had 2 unique values.
    # E.g., workclass has been split up in 9 variables, because the original variable had 9 unique values.
my_data_numerical.describe(include='all')
    # In the statistical summary, we see that all values are umerical now.
    # Notice that the quartiles of the dummy variables are either 1 or 0, since there are no values in between.

######### How to deal with numerical values that are actually categorical

# Sometimes a data set contains a numerical variable that is actually categorical.
    # E.g., somebody encoded the gender variable as 0 for male and 1 for femail in data acquisition.
    # With read_csv, it would be imported as a numerical variable.
    # The problem is that it is not *really* numerical. Some algorithm require us to honor that
    # by transforming them into dummies.
    # We have 2 possibilities to do that:
    #   1. We can convert the numerical variables that are actually categorical into strings and then use get_dummies().
    #   2. We can use the OneHotEncoder from scikit-learn, which binarises *all* features (not only the categorical ones.)


### Ad 1: We use the function astype() to convert the numerical variable age to a string variable age1:

my_data['age'] = my_data['age'].astype(str)
my_data.info()
    # We see that age is of Dtype int64 (numerical) while age1 is of Dtype object (categorical).

# Now we apply get_dummies() to "binarize" all variables:
my_data_numerical_gd = pd.get_dummies(my_data)
my_data_numerical_gd.info()
    # Remark: Notice that age has 73 unique values.
    # As a result, we end up with 86 variables in total.
my_data_numerical_gd.head()
    # Check the DataFrame in SciView: Why do we see so little ones in the first vew columns?


### Ad 2: We use the OneHotEncoder from scikit-learn:

# Before we start, we restore the original state of my_data:
my_data = data[['age', 'workclass', 'gender', 'income']]
my_data.info()

# Now import the OneHotEncoder
from sklearn.preprocessing import OneHotEncoder

# To use it, we need to initialize the OneHotEncoder:
onehot_data = OneHotEncoder(sparse=False)

# Now we can apply it to my_data:
my_data_numerical_ohe = onehot_data.fit_transform(my_data)
print(my_data_numerical_ohe)
    # Notice that the output of OneHotEncoder is not a DataFrame, but a NumPy array
    # To see this check type():
type(my_data_numerical_ohe)

