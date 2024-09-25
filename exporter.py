import pandas as pd

def export_to_csv(expenses, filename='expenses.csv'):
    if expenses:
        expense_df = pd.DataFrame(expenses)
        expense_df.to_csv(filename, index=False)
        print(f"Expenses exported to {filename} successfully.")
    else:
        print("No expenses to export.")
print("Export module loaded successfully")
