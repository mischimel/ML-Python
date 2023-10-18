import numpy as np

# one-dimensional array
a = np.array([1, 2, 3, 4, 5, 6])
print(a[3]) # 4
print(a[2:5]) # [3 4 5]

# two-dimensional array
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[0]) # [1 2 3 4]
print(a[2][3]) # 12

# attributes on an array a
print(a.ndim) # number of dimensions = 2
print(a.size) # number of elements = 12
print(a.shape) # Size of the data set (rows, columns) = (3, 4)

# whole row or parts of rows from an array a
row1 = a[1, :] # equivalent to: row1 = a[1]
print(row1) # [5 6 7 8]
part_of_row1 = a[1, 1:3]
print(part_of_row1) # [6 7]

# complete columns from the array a (not possible on lists!)
col0 = a[:, 0]
print(col0) # [1 5 9]

# needed for the plotting ------------------------------------------------------------------
import sklearn.datasets as ds

# 100 data objects from two classes described by two features
# X = features, y = target (class)
X, y = ds.make_classification(n_samples=100, n_features=2, n_redundant=0, n_classes=2)

# output the features and the target
print(X)
print(y)
# needed for the plotting ------------------------------------------------------------------

import matplotlib.pyplot as plt

# output the data set with a scatter plot
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title('Data Set with 100 Data Objects, 2 Features, 2 Classes')
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.show()