import pandas as pd

data = {'emp_id': ['1', '2', '3', '4', '5'],'first_name': ['Jason', 'Andy', 'Allen', 'Alice', 'Amy'],'last_name': ['Larkin', 'Jacob', 'A', 'AA', 'Jackson']}
df_1 = pd.DataFrame(data, columns = ['emp_id', 'first_name', 'last_name'])
print "df_1:"
print df_1

data = {'emp_id': ['4', '5', '6', '7'],'first_name': ['Brian', 'Shize', 'Kim', 'Jose'],'last_name': ['Alexander', 'Suma', 'Mike', 'G']}
df_2 = pd.DataFrame(data, columns = ['emp_id', 'first_name', 'last_name'])
print "df_2:"
print df_2

# Left join
print "pd.merge(df_1, df_2, on='emp_id', how='left'):"
print pd.merge(df_1, df_2, on='emp_id', how='left')

# Merge while adding a suffix to duplicate column names of both table
print "pd.merge(df_1, df_2, on='emp_id', how='left', suffixes=('_left', '_right')):"
print pd.merge(df_1, df_2, on='emp_id', how='left', suffixes=('_left', '_right'))

"""Right join - Right join produces a complete set of records from Table B,
with the matching records where available in Table A. If there is no match,
the left side will contain null."""
print "pd.merge(df_1, df_2, on='emp_id', how='right'):"
print pd.merge(df_1, df_2, on='emp_id', how='right')

"""Inner join produces only the set of records that match in both Table A and Table B"""
print "pd.merge(df_1, df_2, on='emp_id', how='inner'):"
print pd.merge(df_1, df_2, on='emp_id', how='inner')

"""Full outer join produces the set of all records in Table A and Table B, with matching records from both sides where available. If
there is no match, the missing side will contain null"""
print "pd.merge(df_1, df_2, on='emp_id', how='outer'):"
print pd.merge(df_1, df_2, on='emp_id', how='outer')