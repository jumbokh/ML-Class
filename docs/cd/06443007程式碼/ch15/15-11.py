# 載入所有模型
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.metrics import recall_score

models = [LogisticRegression(), SVC(), KNeighborsClassifier(), RandomForestClassifier()]
model_results = {}
for model in models:
    model_pl = make_pipeline(StandardScaler(), model)
    model_pl.fit(X_train, y_train)
    y_pred = model_pl.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, pos_label=1)
    model_results[model.__class__.__name__] = [score, recall]
    print(f'模型名稱{model.__class__.__name__:-^50}')
    print('混亂矩陣\n',confusion_matrix(y_test, y_pred))
    print(f'正確率: {score:.3f}， 召回率: {recall:.3f}\n')