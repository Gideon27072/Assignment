import numpy 
print("import successful!")

import numpy as npy
print("successful!")

list = npy.arange(1,101)
print(list)

array = npy.arange(2,101,2)
print('Array of all the even integers from 1 to 100')
print(array)

arr = npy.array([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,60,62,64,66,68,70,72,74,76,78,80,82,84])
x = npy.lcm.reduce(arr)
print(x)