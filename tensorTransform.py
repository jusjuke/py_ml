import tensorflow as tf
import torch
import numpy as np


x_np = np.array([[25,2],[5,26],[3,7]])
print(x_np.transpose())

x_pt = torch.tensor([[25,2],[5,26],[3,7]])
print(x_pt.T)

x_tf = tf.Variable([[25,2],[5,26],[3,7]])
print(tf.transpose(x_tf))
