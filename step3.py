# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Initialize an empty list to store expense data
expenses = []

# Dictionary to store budget for each category
category_budgets = {}

# Define a function to input expense data
def add_expense(amount, category, description, date):
    expense = {
        "Amount": amount,
        "Category": category,
        "Description": description,
        "Date": date
    }
    expenses.append(expense)

# Function to display all expenses
def view_expenses():
    if expenses:
        expense_df = pd.DataFrame(expenses)
        print(expense_df)
    else:
        print("No expenses recorded yet.")

# Function to filter expenses by category
def filter_expenses_by_category(category):
    if expenses:
        expense_df = pd.DataFrame(expenses)
        filtered_df = expense_df[expense_df['Category'] == category]
        print(filtered_df if not filtered_df.empty else f"No expenses in category: {category}")
    else:
        print("No expenses recorded yet.")

# Function to set a budget for a category
def set_budget(category, budget):
    category_budgets[category] = budget
    print(f"Budget for {category} set to {budget}.")

# Function to check budget for a category
def check_budget(category):
    if category in category_budgets:
        total_spent = sum(exp['Amount'] for exp in expenses if exp['Category'] == category)
        remaining_budget = category_budgets[category] - total_spent
        print(f"Total spent in {category}: {total_spent}")
        print(f"Remaining budget for {category}: {remaining_budget}")
    else:
        print(f"No budget set for {category}.")

# Visualization Function: Expense Distribution by Category (Pie Chart)
def visualize_expenses_by_category():
    if expenses:
        expense_df = pd.DataFrame(expenses)
        category_sum = expense_df.groupby('Category')['Amount'].sum()
        category_sum.plot.pie(autopct='%1.1f%%', startangle=90, figsize=(8, 8))
        plt.title("Expense Distribution by Category")
        plt.ylabel('')  # Hide y-label
        plt.show()
    else:
        print("No expenses to visualize.")

# Visualization Function: Monthly Expense Trend (Bar Chart)
def visualize_monthly_expenses():
    if expenses:
        expense_df = pd.DataFrame(expenses)
        expense_df['Date'] = pd.to_datetime(expense_df['Date'])
        monthly_expenses = expense_df.groupby(expense_df['Date'].dt.to_period('M'))['Amount'].sum()
        monthly_expenses.plot(kind='bar', color='skyblue', figsize=(10, 6))
        plt.title("Monthly Expense Trend")
        plt.xlabel("Month")
        plt.ylabel("Total Amount")
        plt.xticks(rotation=45)
        plt.show()
    else:
        print("No expenses to visualize.")

# Example interaction
while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Filter by Category\n4. Set Budget for a Category\n5. Check Budget for a Category\n6. Visualize Expense by Category\n7. Visualize Monthly Expenses\n8. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Transport, Utilities): ")
        description = input("Enter a description: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        
        add_expense(amount, category, description, date)
        print("Expense added successfully.")
        
    elif choice == "2":
        view_expenses()
        
    elif choice == "3":
        category = input("Enter the category to filter by: ")
        filter_expenses_by_category(category)
        
    elif choice == "4":
        category = input("Enter the category: ")
        budget = float(input(f"Set budget for {category}: "))
        set_budget(category, budget)
        
    elif choice == "5":
        category = input("Enter the category to check the budget for: ")
        check_budget(category)
        
    elif choice == "6":
        visualize_expenses_by_category()
        
    elif choice == "7":
        visualize_monthly_expenses()
        
    elif choice == "8":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please try again.")
