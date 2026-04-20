import os

def filter_data(df):
    col = input("Enter column name: ").lower()
    value = input("Enter value to search: ").lower()

    if col in df.columns:
        result = df[df[col].astype(str).str.lower().str.contains(value)]
        print("\nFiltered Results:")
        print(result)
    else:
        print("Column not found!")

def save_file(df):
    path = input("Enter output file name (without extension): ")

    # Create folder if not exists
    os.makedirs("output", exist_ok=True)

    df.to_excel(f"output/{path}.xlsx", index=False)
    df.to_csv(f"output/{path}.csv", index=False)

    print("File saved successfully!")