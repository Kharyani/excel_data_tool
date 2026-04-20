def analyze_data(df):
    print("\n===== DATA ANALYSIS =====")

    print("\nTotal Records:", len(df))

    print("\nColumn Info:")
    df.info()

    print("\nStatistical Summary:")
    print(df.describe())

    col = input("\nEnter column to group by: ")

    if col in df.columns:
        print("\nGrouped Data:")
        print(df.groupby(col).size())
    else:
        print("Column not found!")