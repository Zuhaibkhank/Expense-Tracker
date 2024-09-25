from authentication import register, login
from database import create_connection, create_expense_table, add_expense_to_db, fetch_expenses
from exporter import export_to_csv
from colorama import Fore, Style

# Connect to SQLite Database
db_file = 'expenses.db'
conn = create_connection(db_file)
create_expense_table(conn)

# Colored text for welcoming user to the expense tracker.
print(Fore.CYAN + Style.BRIGHT + 'HELLO! WELCOME TO A FINEST EXPENSE TRACKER.' + Style.RESET_ALL)

# Main logic for handling user interaction
current_user = None
while True:
    print("\n1. Register\n2. Login\n3. Add Expense\n4. View Expenses\n5. Export to CSV\n6. Exit")
    choice = input(Fore.YELLOW + "Choose an option: " + Style.RESET_ALL)
    
    if choice == "1":
        username = input(Fore.YELLOW + "Enter a username: " + Style.RESET_ALL)
        password = input(Fore.YELLOW + "Enter a password: " + Style.RESET_ALL)
        register(username, password)
        
    elif choice == "2":
        username = input(Fore.YELLOW + "Enter your username: " + Style.RESET_ALL)
        password = input(Fore.YELLOW + "Enter your password: " + Style.RESET_ALL)
        if login(username, password):
            current_user = username
    
    elif choice == "3":
        if current_user:
            amount = float(input(Fore.YELLOW + "Enter amount: " + Style.RESET_ALL))
            category = input(Fore.YELLOW + "Enter category: " + Style.RESET_ALL)
            description = input(Fore.YELLOW + "Enter a description: " + Style.RESET_ALL)
            date = input(Fore.YELLOW + "Enter the date (YYYY-MM-DD): " + Style.RESET_ALL)
            
            expense = {
                "Amount": amount,
                "Category": category,
                "Description": description,
                "Date": date
            }
            add_expense_to_db(conn, expense)
        else:
            print(Fore.RED + Style.BRIGHT +"Please login first!" + Style.RESET_ALL)
    
    elif choice == "4":
        if current_user:
            expenses = fetch_expenses(conn)
            for row in expenses:
                print(row)
        else:
            print(Fore.RED + Style.BRIGHT + "Please login first!" + Style.RESET_ALL)
    
    elif choice == "5":
        if current_user:
            expenses = fetch_expenses(conn)
            export_to_csv(expenses)
        else:
            print(Fore.RED + Style.BRIGHT + "Please login first!" + Style.RESET_ALL)
    
    elif choice == "6":
        print("Exiting...")
        break
    
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid choice. Please try again." + Style.RESET_ALL)
