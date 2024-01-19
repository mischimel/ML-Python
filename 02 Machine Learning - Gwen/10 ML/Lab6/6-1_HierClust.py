"""
6-1_HierClust.py

With the help of AgglomerativeClustering from sklearn.cluster we can create hierarchical clusterings on data.
The most important parameters are linkage ("single" or "complete") and n_clusters (e.g. 3 or 7).
The cluster assignment of the data objects can then be queried using the fit_predict function.

First we generate an initial data set with 4 clusters.
We then generate a hierarchical clustering with 4 clusters using the complete linkage distance.
We output the data objects and their affiliations to the clusters in a scatter diagram.
"""

from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# make artifical dataset with 4 "blobs"
X, y = make_blobs(n_samples=1000, centers=4, n_features=2, random_state=42)

# hierarchical clustering
agg = AgglomerativeClustering(linkage="complete", n_clusters=4)
assignment = agg.fit_predict(X)

# plotting the cluster assignment in a scatter plot
plt.scatter(X[:, 0], X[:, 1], c=assignment)
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
plt.show()


# Typically, the correct number of clusters in an application is not known in advance.
# The following code fragment tests various hierarchical clusterings with different
# numbers of clusters and calculates the silhouette index for each clustering
# (using the silhouette_score function from sklearn.metrics - here you will find
# further functions for calculating validation indices for clusterings):

# find optimal number of clusters
for k in range(2, 8):
     agg = AgglomerativeClustering(linkage="complete", n_clusters=k)
     assignment = agg.fit_predict(X)
     score = silhouette_score(X, assignment)
     print("K =", k, "Silhouette Score =", score)

# Visualizing a dendrogram is not (yet?) possible in Scikit-Learn.
# We therefore use the dendrogram function from scipy.cluster.hierarchy.
# To do this, a hierarchical clustering must first be created with the function
# complete or single (also from scipy.cluster.hierarchy).
# The return of this function defines the distances at which two clusters are merged.

# The color_threshold parameter can also be used to tell the dendrogram function
# from which height in the dendrogram the subclusters should be colored differently
# (in our example, we set color_threshold=10.0).

from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import single, complete
import matplotlib.pyplot as plt

# make artifical dataset stemming from 4 classes
X, y = make_blobs(n_samples=1000, centers=4, n_features=2, random_state=42)

# The SciPy single/complete function returns an array that
# specifies the distances bridged when performing agglomerative clustering
linkage_array = complete(X)

# Now we plot the dendrogram
dendrogram(linkage_array, color_threshold=10.0)
plt.xlabel("Data Object")
plt.ylabel("Cluster distance")
plt.show()