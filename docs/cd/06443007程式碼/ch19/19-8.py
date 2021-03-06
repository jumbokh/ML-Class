errors = []
for i in range(1,7):
    kms = KMeans(n_clusters=i)
    kms.fit(X, y)
    errors.append(kms.inertia_)
plt.plot(range(1,7), errors, marker='o')
plt.xlabel('集群數目')
plt.ylabel('集群內的誤差平方和');