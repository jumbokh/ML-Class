n_topics = 12
n_words = 10
from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
cv = CountVectorizer(preprocessor=preprocessor, 
                     token_pattern='(?u)\\b\\w+\\b', 
                     stop_words=stops, 
                     max_df=0.5)
X_array = cv.fit_transform(df['content'])
X_topics = lda.fit_transform(X_array)
idx = cv.get_feature_names()

pd.DataFrame(lda.components_[0], index=idx, columns=['topic']).\
sort_values(by='topic', ascending=False)[:n_words]