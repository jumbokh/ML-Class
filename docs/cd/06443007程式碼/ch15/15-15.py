from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import make_pipeline
np.random.seed(42)
models = [LogisticRegression(), SVC(), KNeighborsClassifier(), RandomForestClassifier()]
model_results = {}
for model in models:
    model_pl = make_pipeline(StandardScaler(), RandomUnderSampler(), model)
    model_pl.fit(X_train, y_train)
    y_pred = model_pl.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, pos_label=1)
    model_results[model.__class__.__name__] = [score, recall]
    print(f'{model.__class__.__name__:-^50}')
    print(confusion_matrix(y_test, y_pred))
    print(f'正確率: {score:.3f}， 召回率: {recall:.3f}')
    print()