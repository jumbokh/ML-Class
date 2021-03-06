from IPython.display import display
df_train = pd.DataFrame(zip(train['data'], train['target']), 
                        columns=['content','target'])
display(df_train.head())
display(df_train['target'].value_counts())