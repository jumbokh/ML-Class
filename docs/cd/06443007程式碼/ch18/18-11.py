cv = CountVectorizer(token_pattern='(?u)\\b\\w+\\b', 
                     stop_words=stops, 
                     ngram_range=(1,2))
bow = cv.fit_transform([s])
print(cv.get_feature_names())