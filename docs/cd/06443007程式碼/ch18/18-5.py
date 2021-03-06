import jieba
# 載入繁體字典
jieba.set_dictionary('dict.txt.big')
print(list(jieba.cut('下雨天留客天留我不留')))
# 將串列組合回字串，用空白做區隔
s = ' '.join(jieba.cut('下雨天留客天留我不留'))
print(s)