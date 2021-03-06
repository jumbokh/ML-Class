def build_model(hidden_layers=1):
    model = models.Sequential()
    model.add(Dense(128, activation='relu', input_shape=(64,)))
    for i in range(hidden_layers):
        model.add(Dense(64, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

model_deep = KerasClassifier(build_fn=build_model, epochs=50, verbose=0)
model_pl = make_pipeline(MinMaxScaler(), model_deep)

param_grid = {
    'kerasclassifier__hidden_layers':range(1,5),
}
gs = GridSearchCV(model_pl, param_grid=param_grid, cv=5, scoring='accuracy')
gs.fit(X_train, y_train)

print('最佳參數：',gs.best_params_)
y_pred = gs.best_estimator_.predict(X_test)
print('正確率：',accuracy_score(y_test, y_pred).round(3))
print(confusion_matrix(y_test, y_pred))