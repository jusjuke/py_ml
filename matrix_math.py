import tensorflow as tf
import torch
import numpy as np


ANP = np.array([[25,2],[5,26],[3,7]])

print(ANP * 2 + 2)
print("---- Pytorch -----")
APT = torch.tensor([[25,2],[5,26],[3,7]])

print(APT * 2 + 2)
print(torch.add(torch.mul(APT, 2), 2))
APX = torch.tensor([[27,4],[7,28],[5,9]])
print(APT * APX) #행렬의 곱셈이 아니다.
print("----Tensor Flow -----")
ATF = tf.Variable([[25,2],[5,26],[3,7]])
print(tf.add(tf.multiply(ATF, 2), 2))
print(ATF * 2 + 2)

ATX = tf.Variable([[27,4],[7,28],[5,9]])
print(ATF * ATX) #행렬의 곱셈이 아니다.


