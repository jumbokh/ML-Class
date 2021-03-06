np.random.seed(42)
model_pl = make_pipeline(
    CountVectorizer(stop_words='english', max_df=0.4),
    LatentDirichletAllocation(n_components=4)
)
X_topics = model_pl.fit_transform(train['data'])
lda = model_pl.named_steps['latentdirichletallocation']
cv = model_pl.named_steps['countvectorizer']

words = {}
for topic in range(n_topics):
    word = pd.DataFrame(lda.components_[topic], index=cv.get_feature_names()).\
            sort_values(by=0, ascending=False)[:n_words].index.tolist()
    words[f'主題{topic+1}'] = word
pd.DataFrame(words)