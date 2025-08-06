import pandas as pd

# === 1. Load the CSV ===
df = pd.read_csv("trains.csv")

# === 2. Clean column names ===
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# === 3. Remove duplicate rows ===
df.drop_duplicates(inplace=True)

# === 4. Handle missing values ===
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

# === 5. Save the cleaned file ===
df.to_csv("cleaned_dataset.csv", index=False)

print(" Cleaning complete. File saved as cleaned_dataset.csv")
