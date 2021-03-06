from sklearn.feature_extraction.text import TfidfVectorizer
string = ['dog love loves',
         'pig love loves pig']
cv = TfidfVectorizer(stop_words='english')
bow = cv.fit_transform(string)
df_bow = pd.DataFrame(bow.toarray(), columns=cv.get_feature_names())
df_bow