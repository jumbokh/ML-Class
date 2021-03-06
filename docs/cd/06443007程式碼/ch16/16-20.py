from IPython.display import display
print('每篇文章在不同主題的機率分布：')
df_class = pd.DataFrame(X_topics, columns=[f'主題{i}' for i in range(1,5)])
df_class['最有可能的主題'] = df_class.idxmax(axis=1) 
display(df_class.head().style.highlight_max(axis=1))

print('第一篇文章')
print(X_train[0])