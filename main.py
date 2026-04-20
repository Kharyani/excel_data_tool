df = None
import pandas as pd
from cleaner import clean_data
from analyzer import analyze_data
from utils import filter_data, save_file


def load_file():
    global df
    path = input("Enter Excel file path: ")
    try:
        df = pd.read_excel(path)
        print("File loaded successfully!\n")
    except Exception as e:
        print("Error:", e)

def menu():
    global df  # IMPORTANT FIX

    while True:
        print("\n===== EXCEL DATA TOOL =====")
        print("1. Load File")
        print("2. Clean Data")
        print("3. Analyze Data")
        print("4. Filter/Search")
        print("5. Save Output")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            load_file()

        elif choice == "2":
            if df is not None:
                df = clean_data(df)
            else:
                print("Load file first!")

        elif choice == "3":
            if df is not None:
                analyze_data(df)
            else:
                print("Load file first!")

        elif choice == "4":
            if df is not None:
                filter_data(df)
            else:
                print("Load file first!")

        elif choice == "5":
            if df is not None:
                save_file(df)
            else:
                print("Load file first!")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()