# 1.3 Integrated Standard Data

# The scikit-learn project comes with a few small, real-world standard datasets for which you do not need
# to load an external file. Each of these datasets can be loaded with a function
# from the datasets module (e.g. load_iris() or load_breast_cancer()).
# The return of these functions is a so-called bunch. A bunch behaves similar to a dictionary
# dict, which contains the data and some metadata.
# • The feature values of the data are stored in the element with the key "data",
#   which is a two-dimensional NumPy array of size N x n (number of data objects times number of features).
# • The names of the features can be found in the list with the key "feature_names" and,
#   in the case of a supervised problem, the array with the key "target" holds the target variable.

import sklearn.datasets as ds

# load an integrated data set
iris = ds.load_iris()
print(iris)

# with the key „data“ we have access to the features
print("\ndata")
print(iris["data"])
print(iris.data)

# with the key „target“ we have access to the target variable
print("\ntarget")
print(iris["target"])
print(iris.target)

# with the key „feature_names“ we have access to the names of the features
print("\nfeature_names")
print(iris["feature_names"])
print(iris.feature_names)

# Note: In a bunch, in contrast to a dictionary, it is possible to read the values of a key
# directly with iris.data instead of iris["data"].


# We will also use the data structure DataFrame of the external package pandas. As you know, a DataFrame can be
# thought of as a spreadsheet in Excel: Each row (i.e. each data object) is numbered with an index (0, 1, 2, ...)
# and each column (i.e. each feature) is labelled with the name of the feature.
# In order to create a DataFrame we therefore need
# • the features of the data objects (e.g. iris["data"]) and
# • the names of the features (e.g. iris["feature_names"]):

import sklearn.datasets as ds
import pandas as pd

# load an integrated data set
iris = ds.load_iris()

# Create DataFrame from the data in iris.data and label the columns with iris.feature_names
X, f = iris["data"], iris["feature_names"]
iris_dataframe = pd.DataFrame(X, columns=f)
print("\n", iris_dataframe)

# Unfortunately, computer screens only have two dimensions, so that only two (or perhaps three) features
# can be displayed simultaneously in a scatter diagram. The data set used above, however, contains four features.
# For example, we could now map the feature sepal length (cm) on the x-axis and
# the feature petal length (cm) on the y-axis.
# Another possibility of visualisation would be to generate a representation of pairs,
# in which all possible pairs of features are shown in a scatter diagram.
# If you have a small number of features, such as the four we have here, this makes sense
# (for more features we need other strategies).

# With the function plotting.scatter_matrix, the module pandas offers the possibility
# to create a scatter diagram for all possible pairs of features in a DataFrame:

import sklearn.datasets as ds
import matplotlib.pyplot as plt
import pandas as pd

# load an integrated data set
iris = ds.load_iris()

# Create a scatterplot matrix from the DataFrame
X, y, f = iris["data"], iris["target"], iris["feature_names"]
iris_dataframe = pd.DataFrame(X, columns=f)
pd.plotting.scatter_matrix(iris_dataframe, c=y)

# workaround to keep the plot active
plt.show(block=True)

# (note that the diagonal of this matrix plot is automatically filled with the histograms of each feature).


