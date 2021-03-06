df_orig = pd.DataFrame(model_results.values(), index=model_results.keys(),
             columns=['prec','recall']).sort_values(by='recall', ascending=False)
df_orig