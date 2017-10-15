import numpy as np

y = np.array([[[1],[2],[3]], [[4],[5],[6]]])
print "Shape of y: ", x.shape
print y[1:3]
# ---- output ----
Shape of y: (3L)
array([[[4], [5], [6]], [7]], dtype=object)

"""Ellipsis expand to the number of : objects needed to make a selection tuple
of the same length as x.ndim. There may only be a single ellipsis present."""_

x[...,0]
---- output ----
array([[0], [1], [2], [3]], dtype=object)

# Create a rank 2 array with shape (3, 4)
a = np.array([[5,6,7,8], [1,2,3,4], [9,10,11,12]])
print "Array a:", a

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
print "Array b:", b
---- output ----
Array a:  [[ 5  6  7  8]
 [ 1  2  3  4]
 [ 9 10 11 12]]
Array b:  [[6 7]
 [2 3]]

A slice of an array is a view into the same data, so modifying itwill modify
the original array.

print a[0, 1]
b[0, 0] = 77
print a[0, 1]
# ---- output ----
# 6
# 77

Middle row array can be accessed in two ways. 1) Slices along with integer
indexing will result in an arry of lower rank. 2) Using only slices will
result in same rank array.
Example code:

row_r1 = a[1,:]# Rank 1 view of the second row of a
row_r2 = a[1:2,:]# Rank 2 view of the second row of a
print row_r1, row_r1.shape # Prints "[5 6 7 8] (4,)"
print row_r2, row_r2.shape # Prints "[[5 6 7 8]] (1, 4)"
---- output ----
[1 2 3 4] (4L,)
[[1 2 3 4]] (1L, 4L)
[[1 2 3 4]] (1L, 4L)

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print col_r1, col_r1.shape # Prints "[ 2 6 10] (3,)"
print col_r2, col_r2.shape