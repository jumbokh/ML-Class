from sklearn.metrics import roc_curve, auc, roc_auc_score
model_pl = make_pipeline(StandardScaler(), 
                         RandomUnderSampler(),
                         LogisticRegression()) 
model_pl.fit(X_train, y_train)
y_pred_proba = model_pl.predict_proba(X_test)[:,1]
fpr, tpr, thres = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr) 
roc_auc
plt.plot(fpr, tpr, marker='.')
plt.title(roc_auc.round(2));