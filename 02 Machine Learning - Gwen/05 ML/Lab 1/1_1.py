# 1.1 Create your own synthetic data set

# The module sklearn.datasets contains functions that can generate synthetic datasets.
# With the function make_classification we can generate a synthetic dataset with any
# number of data objects (n_samples), features (n_features) and classes (n_classes).
# (The parameter n_redudandant specifies how many of the features should be redundant.
# There are further parameters). The return of the function are the features X and the target
# variable y.

import sklearn.datasets as ds

# 100 data objects from two classes described by two features
# X = features, y = target (class)
X, y = ds.make_classification(n_samples=100, n_features=2, n_redundant=0, n_classes=2)
# output the features and the target
print(f"features:\n{X}")
print(f"Target:\n{y}")

# It looks as if X and y are lists - but in fact they are so-called NumPy arrays. While a Python list
# can contain different data types within a single list, all elements in a NumPy array must be of
# the same type. NumPy arrays are faster and use less memory than Python lists.