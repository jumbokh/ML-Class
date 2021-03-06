df_recall = pd.concat([df_orig, df_weight, df_down], axis=1, 
                      keys=['沒處理','權重法','向下取樣'])
df_recall.xs('recall', level=1, axis=1).style.highlight_max(axis=1)