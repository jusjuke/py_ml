import numpy as np
import torch
import tensorflow as tf


#numpy
x = np.array([25,2,5])
print(len(x))
print(x.shape)
print(type(x))
x_t = x.T
print(x_t)
y = np.array([[25,2,5]])
print(y.shape)
print(y)
y_t = y.T
print(y_t.shape)
print(y_t) 
z = np.zeros(3)
print(z)

#PyTorch
x_pt = torch.tensor([25,2,5])
print(x_pt)

#TensorFlow
x_tf = tf.Variable([25,2,5])
print(x_tf)


