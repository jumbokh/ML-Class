from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

def build_model():
    model = models.Sequential()
    model.add(Dense(512, activation='relu', input_shape=(64,)))
    model.add(Dense(10, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', 
                  metrics=['accuracy'])
    return model

np.random.seed(42)
model_deep = KerasClassifier(build_fn=build_model, epochs=50, verbose=0)
model_pl = make_pipeline(MinMaxScaler(), model_deep)
model_pl.fit(X_train, y_train)
y_pred = model_pl.predict(X_test)

print('正確率：',accuracy_score(y_test, y_pred).round(3))
print(confusion_matrix(y_test, y_pred))