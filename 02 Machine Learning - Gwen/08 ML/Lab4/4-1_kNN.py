"""

"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
from sklearn.model_selection import cross_val_score

# We import the diabetes (originally from Kaggle) using pandas
df = pd.read_csv('diabetes.csv')

# separate input features from target variable
X = df.drop(columns=['Outcome'])
y = df['Outcome'].values

# split the data to training and test set
# random_state is to have the same seed value, so it is comparable, in the final one you would take it out
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, test_size=0.4, random_state=23)

# We use the nearest neighbour classifier KNeighborsClassifier.
# The parameter n_neighbors specifies the number k of neighbours used for the majority vote.
knn = KNeighborsClassifier(n_neighbors=1) # initialize
knn.fit(X_train, y_train) # fit (learn)
y_pred = knn.predict(X_test) # predict (make predictions for each test object)
print("Test set score:", knn.score(X_test, y_test)) # evaluate (test recognition rate)
# Remark:
#   Remember that kNN is a lazy learner. Thus, the model cannot be learned independently of the training set.
#   Instead, the training set is an intrinsic part of the model that we "learn" with knn.fit.
#   When we do a prediction with knn.predict, the training data objects are needed to do the majority vote.

# Weighted k-NN
#   With the additional parameter weights='distance' the classifier can weight the neighbours according
#   to their distance to the new object.
knn = KNeighborsClassifier(n_neighbors=10, weights='distance') # initialize
knn.fit(X_train, y_train) # fit (learn)
print("Test set score (weighted k-NN):", knn.score(X_test, y_test)) # evaluate

# Finding the optimal k using the validation set approach
#   Remember that the number of neighbours k is a user-defined parameter (hyperparameter) that the
#   k-NN algorithm cannot learn. We - as users - have to choose it, but we also don't know which
#   value of k to choose: If we choose k too small, kNN might overfit. If we choose k to big,
#   kNN might underfit.
#   To find the "sweetspot" between over- and underfitting, we implement the *validation
#   set approach* for different values of k. In other words, we use different models (each with a
#   different value of k) to predict the classes of the data object in the test set.
#   We then evaluate the different models and compare their recognition rates. We choose the model
#   (and associated k) with the highest test recognition rate.

# The following code fragment implements the above approach as a search in the parameter space of k.
#   To save computing time, we only try a few different values, namely k = 1, 3, .. ., 29.
#   We plot the recognition rates as a function of k as a line plot.
training_accuracy = []
test_accuracy = []
neighbors_settings = range(1, 30, 2) # try n_neighbors from 1, 3, .. ., 29
for n in neighbors_settings:
    knn = KNeighborsClassifier(n_neighbors=n) # initialize
    knn.fit(X_train, y_train) # fit (learn)
    training_accuracy.append(knn.score(X_train, y_train))  # evaluate (and record) training recognition rate
    test_accuracy.append(knn.score(X_test, y_test))  # evaluate (and record) test recognition rate
    print("k =", n, "Test score:", knn.score(X_test, y_test))
# plot the results
plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.show()

# Cross Validation
#   Instead of applying the validation set approach to assess the generalization capabilities of
#   a model, we can also use cross validation (CV). The CV recognition rate is more reliable than the
#   test recognition rate, because it averages over the test recognition rates of several test sets.
#
#   To give an example, the following code applies 5-fold cross-validation to the 10-NN classifier.
#   Remember that CV does the training / test split automatically for us (in this case, 5 times).
#   Thus, we apply CV not on the training set X_train, but on the whole sample X.
#
#   To use CV, we import the function cross_val_score. It expects as parameters (1.) an initialized model,
#   (2.) the sample X, (3.) the class values y and (4.) the number of folds (e.g. cv=5).
#
#   Notice:
#   Usually we do the steps initialize-learn-evaluate. Here, we only need to initialize the model,
#   since the learning and evaluation step is done by CV - once in each fold).

knn = KNeighborsClassifier(n_neighbors=n) # initialize
scores = cross_val_score(knn, X, y, cv=5)
print("Cross-validation scores:", scores) # one score (recognition rate) per fold
print("Mean cross-validation score:", scores.mean()) # average of the 5 recognition rates

# Finding the optimal k using cross validation
#   Now we do the same hyperparameter-optimization as above: We implement a search in the parameter space
#   of k for k = k = 1, 3, .. ., 29. But instead of using the test recognition rate to evaluate each model,
#   we use the mean 10-fold cross validation recognition rate.
cv_accuracy = []
neighbors_settings = range(1, 30, 2) # try n_neighbors from 1, 3, .. ., 29
for n in neighbors_settings:
    knn = KNeighborsClassifier(n_neighbors=n) # initialize
    scores = cross_val_score(knn, X, y, cv=10) # calculate the 10-fold CV recognition rate
    print("k =", n, "Mean cross-validation score:", scores.mean())
    cv_accuracy.append(scores.mean())  # evaluate (and record) training recognition rate
# plot the results
plt.plot(neighbors_settings, cv_accuracy, label="cv accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.show()
# Remark:
#   Notice that the code is a bit shorter than above, but the computational effort is much higher:
#   For each k = 1, 3, 5, ..., 15, CV performs 10 train/test iterations.
#   So, all in all, the above code trains and evaluates 8 * 10 = 80 models, while the code above that uses
#   the validation set approach instead only trains and evaluates 8 models.
#   This is not a problem here, because our data set is so small. But with bigger data sets,
#   this may lead to a long computing time. This is true for all kinds of classifiers, but is particularly
#   problematic for kNN, because it is a lazy learner. It's computing time increases linearly with the size
#   of the training set.
