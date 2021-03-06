from sklearn.compose import ColumnTransformer
X = df[['title', 'content']]
cv = CountVectorizer(preprocessor=preprocessor,    
    token_pattern='(?u)\\b\\w+\\b',
    stop_words=stops)
data_pl = ColumnTransformer([
    ('title', cv, 'title'),
    ('content', cv, 'content')
])
data_pl.fit_transform(X).toarray()