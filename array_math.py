import numpy as np

x=np.array([[1,2],[3,4],[5,6]])
y=np.array([[7,8],[9,10],[11,12]])
print "x"
print x

print "y"
print y

# Elementwise sum; both produce the array
print "print x+y:"
print x+y
print "np.add(x, y):"
print np.add(x, y)

# Elementwise difference; both produce the array
print "x-y:"
print x-y
print "np.subtract(x, y)"
print np.subtract(x, y)

# Elementwise product; both produce the array
print "x*y"
print x*y
print "np.multiply(x, y)"
print np.multiply(x, y)

print "x/y"
print x/y
print "np.divide(x, y)"
print np.divide(x, y)

# Elementwise square root; produces the array
print "np.sqrt(x)"
print np.sqrt(x)