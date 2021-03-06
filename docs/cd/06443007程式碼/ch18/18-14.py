def preprocessor(s):
    return ' '.join(jieba.cut(s))

print('斷字函數的結果：', preprocessor('下雨天留客天留我不留'))
cv = CountVectorizer(preprocessor=preprocessor,    
    token_pattern='(?u)\\b\\w+\\b', 
    stop_words=stops)
bow = cv.fit_transform(['下雨天留客天留我不留'])
pd.DataFrame(bow.toarray(), columns=cv.get_feature_names())