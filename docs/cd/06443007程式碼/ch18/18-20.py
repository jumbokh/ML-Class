X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model_pl = make_pipeline(data_pl, 
                         RandomUnderSampler(),
                         MultinomialNB())
model_pl.fit(X_train, y_train)
y_pred = model_pl.predict(X_test)
score = model_pl.score(X_test, y_test)
print('測試集的結果', score.round(3))
print(confusion_matrix(y_test, y_pred))
print('綜合報告')
print(classification_report(y_test, y_pred))