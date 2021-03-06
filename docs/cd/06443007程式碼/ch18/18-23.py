words = {}
for topic in range(n_topics):
    word = pd.DataFrame(lda.components_[topic], index=idx).\
            sort_values(by=0, ascending=False)[:n_words].index.tolist()
    words[f'主題{topic+1}'] = word
pd.DataFrame(words)