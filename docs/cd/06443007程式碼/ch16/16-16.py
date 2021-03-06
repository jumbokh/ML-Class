pd.DataFrame(lda.components_[0], index=cv.get_feature_names(),
            columns=['topic']).sort_values(by='topic', ascending=False)[:8]