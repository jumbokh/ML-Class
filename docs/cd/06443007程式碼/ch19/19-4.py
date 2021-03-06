pd.DataFrame(kms.transform(X)[:3], 
             columns=['集群0','集群1','集群2']).style.highlight_min(axis=1)