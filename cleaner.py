import pandas as pd

def clean_data(df):
    print("\nCleaning Data...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Handle missing values properly (NO inplace!)
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].mean())

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna("Unknown")

    print("Data cleaned successfully!")
    return df