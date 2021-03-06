cv = CountVectorizer(token_pattern='(?u)\\b\\w+\\b')
bow = cv.fit_transform([s])
pd.DataFrame(bow.toarray(), columns=cv.get_feature_names())