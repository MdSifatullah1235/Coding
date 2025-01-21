import numpy as np
a = np.array([1,2,4,3,6])
print(np.sort(a))

print("First Array : ")
a = np.arange(9,dtype=np.float32).reshape(3,4)
print(a)

print("Second Array : ")
b = np.array([10,10,10])
print(b)

print("and the two arrays : ")

print(np.add(a,b))
print("Multiply the two arrays : ")
print(np.multiply(a,b))

