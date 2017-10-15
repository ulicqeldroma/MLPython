import numpy as np

# create a matrix
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print "a :"
print a

# create a vector
v = np.array([1, 0, 2])
print "v :"
print v

# create an empty matrix with the same shape as a
b = np.empty_like(a)

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(3):
	b[i, :] = a[i, :] + v

print "b :"
print b

# Stack 3 copies of v on top of each other
vv = np.tile(v, (3, 1))
print "vv = np.tile(v, (3, 1)) :"
print vv

# Add a and vv elementwise
b = a + vv
print "b = a + vv :"
print b
