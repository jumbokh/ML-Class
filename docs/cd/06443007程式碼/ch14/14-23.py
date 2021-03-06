from imblearn.over_sampling import SMOTE
smt = SMOTE()
X_train_upsample, y_train_upsample = smt.fit_sample(data_pl.fit_transform(X_train), y_train)
print('原資料的總個數',X_train.shape[0])
print('原本目標值1與0的個數')
print(pd.Series(y_train).value_counts())
print('向上取樣後的總個數',X_train_upsample.shape[0])
print('向上取樣後的目標值1與0的個數')
print(pd.Series(y_train_upsample).value_counts())