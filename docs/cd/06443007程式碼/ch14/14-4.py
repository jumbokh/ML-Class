for idx, d in enumerate(df['TotalCharges']):
    try:
        float(d)
    except:
        print(f'problem data {d} at index {idx}')