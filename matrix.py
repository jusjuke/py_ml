import numpy as np
import torch
import tensorflow as tf

X = np.array([[25,2],[5,26],[3,7]])
print(X)
print(X.shape)
print(X.size)
print(X[:,0])
print(X[1,:])
#0 ~ 2 row, 0 ~ 2 column
print(X[0:2, 0:2])
print(X[0:3, 0:2])

# X[i,j,k,l] matrix
images_pt = torch.zeros([32, 28,28,3])
print(images_pt)
images_tf = tf.zeros([32, 28,28,3])
print(images_tf)
