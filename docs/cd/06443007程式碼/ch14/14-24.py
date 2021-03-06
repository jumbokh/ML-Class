X_upsample, y_upsample = smt.fit_sample(data_pl.fit_transform(X), y)
X_train_up, X_test_up, y_train_up, y_test_up = train_test_split(X_upsample, 
                                                                y_upsample, test_size=0.3)
# 固定隨機亂數的起點，讓我們的結果會一致
np.random.seed(42)

lr = LogisticRegression()
lr.fit(X_train_up, y_train_up)
y_pred_up = lr.predict(X_test_up)
print('正確率')
print(accuracy_score(y_test_up, y_pred_up))
print('混亂矩陣')
print(confusion_matrix(y_test_up, y_pred_up))
print('綜合報告')
print(classification_report(y_test_up, y_pred_up))