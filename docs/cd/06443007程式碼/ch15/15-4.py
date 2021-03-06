size = df['Class'].value_counts()
pct = df['Class'].value_counts(normalize=True).round(3)
pd.DataFrame(zip(size, pct), columns=['次數', '百分比'], index=['No','Yes'])