import numpy as np

x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
a=np.array([9,10])
b=np.array([11, 12])

print "x:"
print x
print "y:"
print y
print "a:"
print a
print "b:"
print b

# Inner product of vectors; both produce 219
print "a.dot(b):"
print a.dot(b)
print "np.dot(a, b):"
print np.dot(a, b)

# Matrix / vector product; both produce the rank 1 array [29 67]
print "x.dot(a):"
print x.dot(a)
print "np.dot(x, a):"
print np.dot(x, a)

# Matrix / matrix product; both produce the rank 2 array
print "x.dot(y):"
print x.dot(y)
print "np.dot(x, y):"
print np.dot(x, y)