import numpy as np

a = np.array([1, 2, 3, 4, 5])
print("1D array:", a)

b = np.array([[1, 2, 3],
              [4, 5, 6]])
print("2D array:\n", b)

c = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
print("3D array:\n", c)

r = a.reshape(5, 1)
print("Reshaped array:\n", r)

print("Slice of 1D array:", a[1:4])
print("Slice of 2D array:", b[:, 1])  

print("Element from 1D:", a[2])
print("Element from 2D:", b[1, 2])
print("Element from 3D:", c[0, 1, 1])
