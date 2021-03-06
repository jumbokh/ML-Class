from scipy.spatial import distance
print(f'第一筆資料為{X.loc[0].values}')
print(f'第一筆資料屬於集群{kms.predict(X.loc[[0]])}', end='')
print(f'，該集群的中心為{kms.cluster_centers_[2]}')
dst = distance.euclidean(X.loc[0].values, kms.cluster_centers_[2])
print(f'其距離平方和為{dst**2:.3f}')