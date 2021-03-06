# 從檔案讀入停用字，並做成串列
with open('stop.text','r', encoding='utf-8') as f:
    stops = f.read()
stops = stops.split('\n')

cv = CountVectorizer(token_pattern='(?u)\\b\\w+\\b', 
                     stop_words=stops)
bow = cv.fit_transform([s])
print(cv.get_feature_names())