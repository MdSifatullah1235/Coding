import numpy as np
array = np.array([1,2,3,4,5])
print(type(array))

print(array[4])
print(array[1:4])

arr = np.array([12,14,15], dtype="S")

print(arr)
print(arr.dtype)


arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newArr = arr.reshape(3,4)
print(newArr)

for i in arr:
    print(arr)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr =np.concatenate((arr1,arr2))
print(arr)

arr = np.array([1,2,3,4,5,6,7,8,9,10])
x = np.where(arr == 4)
print(x)

arr = np.array([1,2,3,4,5,6,7,8,9,10])
x = np.where(arr%2 == 0)
print(x)

from numpy import random

x = random.randint(100)
print(x)