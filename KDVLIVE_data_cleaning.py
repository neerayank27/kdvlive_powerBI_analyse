import pandas as pd
file_path = 'KDVLIVE_Sales_Data.csv'
df = pd.read_csv(file_path)

print("Original Data:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing values in each column:\n", df.isnull().sum())

threshold = len(df) * 0.5
df.dropna(axis=1, thresh=threshold, inplace=True)

numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

df.drop_duplicates(inplace=True)

df.columns = df.columns.str.strip()
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

for col in df.columns:
    if df[col].dtype == 'object':
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

df.to_csv('KDVLIVE_Sales_Data_Cleaned.csv', index=False)
print("\n Cleaned data saved as 'KDVLIVE_Sales_Data_Cleaned.csv'")