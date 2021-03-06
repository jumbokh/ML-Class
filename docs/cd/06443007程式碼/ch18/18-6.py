from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
bow = cv.fit_transform([s])
pd.DataFrame(bow.toarray(), columns=cv.get_feature_names())