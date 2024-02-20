import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)

# Joining Arrays Using Stack Functions
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# Stacking Along Rows
arr = np.hstack((arr1, arr2))
print(arr)

#Stacking Along Columns
arr = np.vstack((arr1, arr2))
print(arr)

# Stacking Along Height (depth)
arr = np.dstack((arr1, arr2))
print(arr)