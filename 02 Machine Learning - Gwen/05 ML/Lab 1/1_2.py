# 1.2 NumPy Examples and Plotting

# Fortunately, NumPy arrays behave almost the same as lists.
# For example, accessing individual elements via index or slicing works exactly the same as with lists:

import numpy as np

# one-dimensional array
print("one-dimensional array")
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(a[3])  # 4
print(a[2:5])  # [3 4 5]

# two-dimensional array
print("\ntwo-dimensional array")
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[0])  # [1 2 3 4]
print(a[2][3])  # 12

# In addition, NumPy arrays offer a few attributes (number of dimensions, elements and size of the data set):

# attributes on an array a
print("\nattributes on an array a")
print(a)
print(a.ndim)  # number of dimensions = 2
print(a.size)  # number of elements = 12
print(a.shape)  # Size of the data set (rows, columns) = (3, 4)

# The biggest difference to lists (in terms of syntax) is the access to whole rows or columns:

# whole row or parts of rows from an array a
print("\nwhole row or parts of rows from an array a")
print(a)
row1 = a[1, :]  # equivalent to: row1 = a[1]
print(row1)  # [5 6 7 8]
part_of_row1 = a[1, 1:3]
print(part_of_row1)  # [6 7]

# complete columns from the array a (not possible on lists!)
print("\ncomplete columns from the array a")
print(a)
col0 = a[:, 0]
print(col0)  # [1 5 9]

# One of the best ways to examine data is to visualise it. One way to do this is to use a scatter plot.
# For this the code form 1.1 is needed:

# Code 1.1
import sklearn.datasets as ds

# 100 data objects from two classes described by two features
# X = features, y = target (class)
X, y = ds.make_classification(n_samples=100, n_features=2, n_redundant=0, n_classes=2)
# output the features and the target
print(f"features:\n{X}")
print(f"Target:\n{y}")

# here is the code bit what created the scatter plot
import matplotlib.pyplot as plt

# output the data set with a scatter plot
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title('Data Set with 100 Data Objects, 2 Features, 2 Classes')
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.show()

# In the example above, we use the scatter() function:
# on the x-axis are the values of the 0th column (X[:, 0])
# and on the y-axis the values of the 1st column (X[:, 1]) of the data objects.
# Each data object is now drawn in the plane as a point according to its features - the
# colour c of the point is given by the class y of the respective data objects.
