import pandas as pd

data = {
    "Name": ["Ali", "Sara", "John", "Ali"],
    "Age": [25, 30, None, 25],
    "Department": ["IT", "HR", "Finance", "IT"],
    "Salary": [50000, 60000, 70000, 50000]
}

df = pd.DataFrame(data)

df.to_excel("sample_data.xlsx", index=False)

print("Excel file created successfully in this folder!")