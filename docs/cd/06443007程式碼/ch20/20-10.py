np.random.seed(42)
model.fit(X_train, y_train_oh.toarray(), 
          epochs=50, verbose=0, validation_split=0.2)

y_pred_oh = model.predict(X_test)
y_pred = y_pred_oh.argmax(axis = 1)

print('正確率：',accuracy_score(y_test, y_pred).round(3))
print(confusion_matrix(y_test, y_pred))