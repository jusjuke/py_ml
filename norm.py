import numpy as np

#3차원 공간 좌표의 길이 
x = np.array([25,2,5])
calc_x = (25 ** 2 + 2 ** 2 + 5 ** 2) ** (1/2)
print(calc_x)
norm_x = np.linalg.norm(x)
print(norm_x)

c = np.array([5,5])
norm_c = np.linalg.norm(c)
print(norm_c)

#원주길이 아님
pi = (2 * 3.14 * 5)
qpi = pi * 90 / 360
print(qpi)


#L1 norm
n1 = np.abs(25) + np.abs(2) + np.abs(5)
print(n1)

#Squared L2 Norm
norm_sqt = (25 ** 2 + 2 ** 2 + 5 ** 2)
print(norm_sqt)
print(np.dot(x, x))

#Max Norm
print(np.max([np.abs(25), np.abs(2), np.abs(5)]))

#orthogonal vectors
i = np.array([0,1])
j = np.array([1,0])
print(np.dot(i,j))
