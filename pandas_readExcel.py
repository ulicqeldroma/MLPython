import pandas as pd

# Reading
df=pd.read_excel('test.xlsx','Sheet1') # from Excel
print df

#Writing to csv in txt format
df.to_csv('test.txt', sep='\t', index=False)

#Reading from text file
df2=pd.read_csv('test.txt', sep='\t')
print "df2:"
print df2

# reading from multiple sheets of same Excel into different dataframes
xlsx = pd.ExcelFile('test.xlsx')
sheet2_df = pd.read_excel(xlsx, 'Sheet2')
print "sheet2_df:"
print sheet2_df

"""describe()- will returns the quick stats such as count, mean, std (standard
deviation), min, first quartile, median, third quartile, max on each column
of the dataframe"""
print "sheet2_df.describe():"
print sheet2_df.describe()

"""Covariance indicates how two variables are related. A positive
covariance means the variables are positively related, while a negative
covariance means the variables are inversely related. Drawback of covariance
is that it does not tell you the degree of positive or negative relation"""
print "sheet2_df.cov():"
print sheet2_df.cov()

"""Correlation is another way to determine how two variables are
related. In addition to telling you whether variables are positively or
inversely related, correlation also tells you the degree to which the
variables tend to move together. When you say that two items correlate, you
are saying that the change in one item effects a change in another item. You
will always talk about correlation as a range between -1 and 1. In the below
example code, petal length is 87% positively related to sepal length that
means a change in petal length results in a positive 87% change to sepal
lenth and vice versa."""
print "sheet2_df.corr():"
print sheet2_df.corr()