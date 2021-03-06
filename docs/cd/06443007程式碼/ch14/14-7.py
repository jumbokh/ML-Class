size = df['Churn'].value_counts()
pct = df['Churn'].value_counts(normalize=True).round(2)
pd.DataFrame(zip(size, pct), columns=['次數', '百分比'], index=['No','Yes'])