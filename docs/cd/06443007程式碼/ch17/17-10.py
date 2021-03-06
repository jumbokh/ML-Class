X = df[['title', 'content']]
from sklearn.compose import ColumnTransformer
data_pl = ColumnTransformer([
    ('title', CountVectorizer(stop_words='english'), 'title'),
    ('content', CountVectorizer(stop_words='english'), 'content')
])
data_pl.fit_transform(X).toarray()