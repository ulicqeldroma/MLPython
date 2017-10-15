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