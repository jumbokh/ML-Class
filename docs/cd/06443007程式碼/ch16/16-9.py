string = ['He do love her and He does not loves he']
cv = CountVectorizer(stop_words='english')
bow = cv.fit_transform(string)
df_bow = pd.DataFrame(bow.toarray(), columns=cv.get_feature_names())
df_bow