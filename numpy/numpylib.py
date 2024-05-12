#pip install numpy
import numpy as np
a = np.array([1, 2, 3])
print(a)               # Output: [1, 2, 3]

print()
A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)
# Printing type of arr object 
print("Array is of type: ", type(A)) 
  
# Printing array dimensions (axes) 
print("No. of dimensions: ", A.ndim) 
  
# Printing shape of array 
print("Shape of array: ", A.shape) 
  
# Printing size (total number of elements) of array 
print("Size of array: ", A.size) 
  
# Printing type of elements in array 
print("Array stores elements of type: ", A.dtype)


A = np.array([[1.1, 2, 3], [3, 4, 5]]) # Array of floats
print(A)

zeors_array = np.zeros( (2, 3) )
print(zeors_array)

ones_array = np.ones( (1, 5), dtype=np.int32) # specifying dtype
print(ones_array)      # Output: [[1 1 1 1 1]]

