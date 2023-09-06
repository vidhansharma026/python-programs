# import numpy as np
# li = [1,2,3,4,5]
# arr = np.array(li)
# print(arr)
# print(type(arr))

# create array from array module
import array
a = array.array('i', [1, 2, 3]) #first array is object and second is method
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
print(type(a))