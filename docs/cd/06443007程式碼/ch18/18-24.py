cv = CountVectorizer(preprocessor=preprocessor, 
                     token_pattern='(?u)\\b\\w+\\b', 
                     stop_words=stops, max_df=0.5)
bow = cv.fit_transform(df['content'])
df_bow = pd.DataFrame(bow.toarray(), columns=cv.get_feature_names())
df_bow.head()