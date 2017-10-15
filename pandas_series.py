import pandas as pd
import numpy as np

"""Creating a series by passing a list of values, and a custom index label.
Note that the labeled index reference for each row and it can have duplicate values"""

s = pd.Series([1,2,3,np.nan,5,6], index=['A','B','C','D','E','F'])
print s
