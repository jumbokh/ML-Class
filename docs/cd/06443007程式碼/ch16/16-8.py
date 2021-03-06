string = ['He do love her and He does not loves he']
cv = CountVectorizer(ngram_range=(2,2))
bow = cv.fit_transform(string)
df_bow = pd.DataFrame(bow.toarray(), columns=cv.get_feature_names())
df_bow