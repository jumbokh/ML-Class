param_grid = {
    'kerasclassifier__epochs':[50, 100, 150],
    'kerasclassifier__validation_split':[0.1, 0.2]
}
from sklearn.model_selection import GridSearchCV
gs = GridSearchCV(model_pl, param_grid=param_grid, cv=5, scoring='accuracy')
gs.fit(X_train, y_train)

print('最佳參數：',gs.best_params_)
y_pred = gs.best_estimator_.predict(X_test)
print('正確率：',accuracy_score(y_test, y_pred).round(3))
print(confusion_matrix(y_test, y_pred))