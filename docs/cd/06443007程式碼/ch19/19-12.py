from sklearn.base import BaseEstimator, TransformerMixin
class Kmeans_label(BaseEstimator, TransformerMixin):
    def __init__(self, n_clusters):
        self.n_clusters = n_clusters

    def fit(self, X, y=None):
        self.model = KMeans(self.n_clusters).fit(X, y)
        return self
    
    def transform(self, X, y=None):
        return self.model.predict(X).reshape(-1, 1)
np.random.seed(42)
kms_l = Kmeans_label(n_clusters=4)
kms_l.fit(X_train, y_train)
kms_l.transform(X_train)[:5]