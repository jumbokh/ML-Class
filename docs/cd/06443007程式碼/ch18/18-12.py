df['rating'] = (df['rating'] > 3).map({True:1 , False:0})
df['rating'].value_counts()