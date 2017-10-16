import pandas as pd

data = {'emp_id': ['1', '2', '3', '4', '5'],'first_name': ['Jason', 'Andy', 'Allen', 'Alice', 'Amy'],'last_name': ['Larkin', 'Jacob', 'A', 'AA', 'Jackson']}
df_1 = pd.DataFrame(data, columns = ['emp_id', 'first_name', 'last_name'])
print "df_1:"
print df_1

data = {'emp_id': ['4', '5', '6', '7'],'first_name': ['Brian', 'Shize', 'Kim', 'Jose'],'last_name': ['Alexander', 'Suma', 'Mike', 'G']}
df_2 = pd.DataFrame(data, columns = ['emp_id', 'first_name', 'last_name'])
print "df_2:"
print df_2

# Usingconcat
df = pd.concat([df_1, df_2])
print "pd.concat([df_1, df_2]):"
print df
print "pd.concat([df_1, df_2], axis=1):"
print pd.concat([df_1, df_2], axis=1)

# Merge two dataframes based on the emp_id value
# in this case only the emp_id's present in both table will be joined
print "pd.merge(df_1, df_2, on='emp_id'):"
print pd.merge(df_1, df_2, on='emp_id')