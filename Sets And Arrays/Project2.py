import array as arr

array_num = arr.array("i",[1,3,5,6,9,3,7,3])

print("The array is :", str(array_num))
print("The number of times 3 occured in this array is :",str(array_num.count(3)))

array_num.reverse()
print("The reversed order of this array is :",str(array_num))