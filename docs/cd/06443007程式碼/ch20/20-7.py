from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
model_pl_kn = make_pipeline(MinMaxScaler(), KNeighborsClassifier())
model_pl_kn.fit(X_train, y_train)
y_pred = model_pl_kn.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
print('正確率：',accuracy_score(y_test, y_pred).round(3))
print(confusion_matrix(y_test, y_pred))