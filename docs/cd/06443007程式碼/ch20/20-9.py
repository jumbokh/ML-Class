from sklearn.preprocessing import OneHotEncoder
oh = OneHotEncoder()
y_train_oh =  oh.fit_transform(y_train.reshape(-1,1))
y_test_oh = oh.transform(y_test.reshape(-1,1))
print('第一筆資料的目標值：', y_train[0])
print('獨熱編碼結果：')
print(pd.DataFrame(y_train_oh.toarray()[[0]]))