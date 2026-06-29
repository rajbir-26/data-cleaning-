# ==========================
# AMAZON DATA CLEANING
# ==========================

# Import Pandas
import pandas as pd

# --------------------------
# 1. Load Dataset
# --------------------------
df = pd.read_csv("amazon_messy.csv")

print("Dataset Loaded Successfully")
print("="*50)

# --------------------------
# 2. Basic Information
# --------------------------
print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# --------------------------
# 3. Remove Duplicate Rows
# --------------------------
df = df.drop_duplicates()

print("\nDuplicates Removed")

# --------------------------
# 4. Remove Extra Spaces
# --------------------------
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

print("Extra Spaces Removed")

# --------------------------
# 5. Standardize Category Names
# --------------------------
df['category'] = df['category'].replace({
    'Electroncs':'Electronics',
    'COMPUTERS&ACCESSORIES':'Computers&Accessories',
    'Computer & Accessories':'Computers&Accessories'
})

print("Category Names Standardized")

# --------------------------
# 6. Convert Rating to Numeric
# --------------------------
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# --------------------------
# 7. Clean Rating Count
# --------------------------
df['rating_count'] = (
    df['rating_count']
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace(" reviews", "", regex=False)
)

df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

print("Numeric Columns Cleaned")

# --------------------------
# 8. Fill Missing Values
# --------------------------

# Text Columns
text_columns = ['product_name','category','review_title']

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")

# Numeric Columns
df['rating'] = df['rating'].fillna(df['rating'].mean())

df['rating_count'] = df['rating_count'].fillna(df['rating_count'].median())

print("Missing Values Filled")

# --------------------------
# 9. Check Again
# --------------------------
print("\nRemaining Missing Values")
print(df.isnull().sum())

print("\nNew Shape")
print(df.shape)

# --------------------------
# 10. Save Cleaned Dataset
# --------------------------
df.to_csv("amazon_cleaned.csv", index=False)

print("\nCleaning Completed Successfully")
print("Cleaned File Saved as amazon_cleaned.csv")

