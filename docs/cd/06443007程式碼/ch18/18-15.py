from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

cv = CountVectorizer(preprocessor=preprocessor,    
    token_pattern='(?u)\\b\\w+\\b', 
    stop_words=stops)
model_pl = make_pipeline(cv, MultinomialNB())
model_pl.fit(X_train, y_train)
y_pred = model_pl.predict(X_test)
score = model_pl.score(X_test, y_test)
print('測試集的結果', score.round(3))
print(confusion_matrix(y_test, y_pred))
print('綜合報告')
print(classification_report(y_test, y_pred))