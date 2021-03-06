cv = CountVectorizer(stop_words='english')
X = cv.fit_transform(train['data'])
np.random.seed(42)
from sklearn.decomposition import LatentDirichletAllocation 
lda = LatentDirichletAllocation(n_components=4)
X_topics = lda.fit_transform(X)
lda.components_.shape