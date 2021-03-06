from sklearn.preprocessing import StandardScaler
model_pl_lr = make_pipeline(StandardScaler(), LogisticRegression())
model_pl_lr.fit(X_train, y_train)
y_pred = model_pl_lr.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))