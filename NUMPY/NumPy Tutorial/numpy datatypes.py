import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr1 = np.array(['apple', 'banana', 'cherry'])
print(arr1.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)