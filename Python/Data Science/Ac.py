import numpy as np

arr = np.arange(10)
print(arr)

new_arr = arr.copy()
new_arr[new_arr % 2 == 1] = -1
print(new_arr)

reshaped_arr = arr.reshape(2, 5)
print(reshaped_arr)

even_sum = arr[arr % 2 == 0].sum()
print(even_sum)