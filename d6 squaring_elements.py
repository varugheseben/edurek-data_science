import numpy as np
# list1 = [1,2,3,4,5]
# numpy_data = np.array(list1)
# numpy_squares = numpy_data ** 2
# print(numpy_squares)
#o/p: [ 1  4  9 16 25]

## Create array from scratch 

zero_np1 = np.zeros((3, 3)) # 3x3 array of zeros
# print(zero_np1)


##
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]


### Create array with all ones

np_one = np.ones((2,4)) ## 2x4 array of 1 
# print(np_one)
# #o/p: [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

## Create a array with value 7 in 2x2 matrix

np_full = np.full((2,2),7)
# print(np_full)

# #[[7 7]
#  [7 7]]

# Here it will create an array from 1 to 100...arange is like range
# arange(start,stop,step)
np_arange = np.arange(1,100,2)
# print(np_arange)

# #[ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47
#  49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95
#  97 99]

### Reshaping the arrays -> convert the rows to colums 
arr = np.array([[1,2,3],[2,3,4]])
print(arr)
print(arr.shape)

#o/p: 
# [[1 2 3]
#  [2 3 4]]
# (2, 3)
# now lets reshare the code
reshaped = arr.reshape((3,2))
print(reshaped)
print(reshaped.shape)
# #[[1 2]
#  [3 2]
#  [3 4]]
# (3, 2)

# i want to conver an array to 1D array
flattened = arr.flatten()
print(flattened)

#[1 2 3 2 3 4]