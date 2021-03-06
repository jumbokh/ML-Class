df_corr = df.drop('Class',axis=1).corrwith(df['Class']).\
sort_values(ascending=False)
print(df_corr[:3])
print(df_corr[-3:])