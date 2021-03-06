from sklearn.feature_extraction.text import CountVectorizer
string = ['He do love her and He does not loves he']
cv = CountVectorizer()
bow = cv.fit_transform(string)
bow.toarray()