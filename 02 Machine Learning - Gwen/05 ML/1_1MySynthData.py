import sklearn.datasets as ds

# 100 data objects from two classes described by two features
# X = features, y = target (class)
X, y = ds.make_classification(n_samples=100, n_features=2, n_redundant=0, n_classes=2)

# output the features and the target
print(X)
print(y)

import matplotlib.pyplot as plt

# output the data set with a scatter plot
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title('Data Set with 100 Data Objects, 2 Features, 2 Classes')
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.show()