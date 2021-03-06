ks = KMeans(n_clusters=3)
ks.fit(X, y)
y_pred = ks.predict(X)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
df.plot(kind='scatter', x='sepal width (cm)', y='petal length (cm)', c='target',
       cmap='coolwarm', colorbar=False, ax=axes[0], title='原始資料')
df.plot(kind='scatter', x='sepal width (cm)', y='petal length (cm)', c=y_pred,
       cmap='coolwarm', colorbar=False, ax=axes[1], title='集群結果')
axes[1].scatter(ks.cluster_centers_[:,0], ks.cluster_centers_[:,1], s=70, c='red');