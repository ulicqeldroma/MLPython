import pandas as pd
import numpy as np

df = pd.DataFrame({'Name' : ['jack', 'jane', 'jack', 'jane', 'jack', 'jane','jack', 'jane'],'State' : ['SFO', 'SFO', 'NYK', 'CA', 'NYK', 'NYK', 'SFO', 'CA'],'Grade':['A','A','B','A','C','B','C','A'],'Age' : np.random.uniform(24, 50, size=8),'Salary' : np.random.uniform(3000, 5000, size=8),})
print "df:"
print df

# Find max age and salary by Name / State
# with groupby, we can use all aggregate functions such as min, max, mean, count, cumsum
print "df.groupby(['Name','State']).max():"
print df.groupby(['Name','State']).max()

# Pivot Function
print "pd.pivot_table(df, values='Age', index=['State', 'Name'], columns=['Grade']):"
print pd.pivot_table(df, values='Age', index=['State', 'Name'], columns=['Grade'])
