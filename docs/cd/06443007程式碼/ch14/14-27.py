from sklearn.metrics import precision_recall_curve
model_pl = make_pipeline(data_pl, LogisticRegression(class_weight='balanced')) 
model_pl.fit(X_train, y_train)
y_pred_proba = model_pl.predict_proba(X_test)[:,1]
prec, recall, thres = precision_recall_curve(y_test, y_pred_proba)
plt.plot(recall, prec)