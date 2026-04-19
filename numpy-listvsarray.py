# compare the time taken to perform a task in a list and array to see
# which one is faster

import  numpy as np
import time
# py_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
x = 10000000
py_list = list(range(x))
# print(py_list)
start = time.time()
print(start)  #1774753748.330815
for x in py_list:
    result = x * 2  #computation where are just multipying the list with 2
end = time.time()
print(end)
print(f"Difference in the Python list execution time is {end - start}")

#### NUMPY ARRAYS 
np_array = np.array(py_list)
start = time.time()
for i in range(size)
    result[i] = np_array[i] * 2 
end = time.time()
print(f"Difference in the arrays  execution time is {end - start}")

# Difference in the Python list execution time is 2.1941723823547363
##Difference in the arrays  execution time is 0.1373286247253418