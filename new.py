import pandas as pd
df = pd.read_csv("train.csv")  

print("Missing values:\n", df.isnull().sum())

# 2. Data types
print("\nData types:\n", df.dtypes)

# 3. Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

# 4. Duplicates
print("\nDuplicates before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates after:", df.duplicated().sum())

# 5. Fill missing Postal Code
df['Postal Code'] = df['Postal Code'].fillna(0)

# Quick sanity check
print("\nFinal shape:", df.shape)
print(df.dtypes)
df.to_csv("cleaned_orders.csv", index=False)

df['Order Month'] = df['Order Date'].dt.to_period('M').astype(str)
df.to_csv("cleaned_orders_with_month.csv", index=False)

Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Sales'] < lower_bound) | (df['Sales'] > upper_bound)]

outliers.to_csv('outliers_flagged.csv', index=False)
print(f"Flagged {len(outliers)} outlier rows out of {len(df)} total.")
