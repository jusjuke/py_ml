import numpy as np

X = np.array([[25,2],[5,26],[3,7]])
print(X)
print(X.shape)
print(X.size)
print(X[:,0])
print(X[1,:])
#0 ~ 2 row, 0 ~ 2 column
print(X[0:2, 0:2])
print(X[0:3, 0:2])
