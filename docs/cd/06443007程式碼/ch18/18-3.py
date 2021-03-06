size = df['rating'].value_counts().sort_index()
pct = df['rating'].value_counts(normalize=True).round(2).sort_index()
pd.DataFrame(zip(size, pct), columns=['次數', '百分比'], index=range(1,6))