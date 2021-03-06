from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, 
                                                    random_state=2)

from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
model_pl = make_pipeline(KMeans(n_clusters=4), LogisticRegression())
model_pl.fit(X_train, y_train)
y_pred = model_pl.predict(X_test)

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
score = model_pl.score(X_test, y_test)
print('測試集的結果', score.round(3))
print(confusion_matrix(y_test, y_pred))
print('綜合報告')
print(classification_report(y_test, y_pred))