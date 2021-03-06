df['TotalCharges'] = df['TotalCharges'].replace(' ',0)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])