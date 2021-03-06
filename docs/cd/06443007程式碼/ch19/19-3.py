from sklearn.cluster import KMeans
kms = KMeans(n_clusters=3, random_state=42)
kms.fit(X, y)
print(kms.cluster_centers_)