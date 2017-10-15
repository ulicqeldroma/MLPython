import numpy as np

x=np.array([[1,2],[3,4]])
print "x:"
print x

# Compute sum of all elements
print "np.sum(x):"
print np.sum(x)

# Compute sum of each column
print "np.sum(x, axis=0):"
print np.sum(x, axis=0)

# Compute sum of each row
print "np.sum(x, axis=1):"
print np.sum(x, axis=1)