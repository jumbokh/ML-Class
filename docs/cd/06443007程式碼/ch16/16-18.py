# 用這三行可以增加新的停用字詞
from sklearn.feature_extraction import text
extra_words = ['edu','subject','lines','com']
stop_words = text.ENGLISH_STOP_WORDS.union(extra_words)

lda = LatentDirichletAllocation(n_components=4)
cv = CountVectorizer(stop_words=stop_words)
bow = cv.fit_transform(train['data'])
X_topics = lda.fit_transform(bow)
words = {}
for topic in range(n_topics):
    word = pd.DataFrame(lda.components_[topic], index=cv.get_feature_names()).\
            sort_values(by=0, ascending=False)[:n_words].index.tolist()
    words[f'主題{topic+1}'] = word
pd.DataFrame(words)