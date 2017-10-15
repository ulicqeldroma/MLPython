import numpy as np

x = np.array([5, 6, 7, 8, 9])
print x[1:7:2]

"""Negative k makes stepping go toward smaller indices. Negative i and j are
interpreted as n + i and n + j where n is the number of elements in the
corresponding dimension."""

print x[-2:5]
print x[-1:1:-1]

"""If n is the number of items in the dimension being sliced. Then if i is not
given then it defaults to 0 for k > 0 and n - 1 for k < 0. If j is not given
it defaults to n for k > 0 and -1 for k < 0. If k is not given it defaults
to 1. Note that :: is the same as : and means select all indices along this
axis."""
print x[4:]

"""(root) G:\MachineLearning\Python\book>python basic_slicing.py
[6 8]
[8 9]
[9 8 7]
[9]"""