df['Churn'] = df['Churn'].replace({'No':0, 'Yes':1})
df.drop('customerID', axis=1, inplace=True)
df_orig = df.copy()