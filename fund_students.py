from sklearn import datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
student = pd.read_csv('student-mat.csv', sep=';')

"""This creates a new DataFrame from the 
columns that we need: """

df = student[['studytime','G3']].copy()

# Simple scatter plot
df.plot(kind='scatter', x='studytime', y='G3', title='Grade vs Hours Studied')
# check the correlation between variables
print df.corr()