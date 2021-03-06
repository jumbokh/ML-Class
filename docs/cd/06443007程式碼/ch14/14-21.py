from imblearn.under_sampling import RandomUnderSampler
rus = RandomUnderSampler()
X_train_resample, y_train_resample = rus.fit_sample(X_train, y_train)
print('原資料的總個數',X_train.shape[0])
print('原本目標值1與0的個數')
print(pd.Series(y_train).value_counts())
print('向下取樣後的總個數',X_train_resample.shape[0])
print('向下取樣後的目標值1與0的個數')
print(pd.Series(y_train_resample).value_counts())