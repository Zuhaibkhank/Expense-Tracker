# User Authentication Logic
from colorama import Fore, Style
users = {}

def register(username, password):
    if username in users:
        print(Fore.RED + Style.BRIGHT + "Username already exists. Please choose another one." + Style.RESET_ALL)
    else:
        users[username] = password
        print(Fore.CYAN + Style.BRIGHT + f"User {username} registered successfully." + Style.RESET_ALL)

def login(username, password):
    if username in users and users[username] == password:
        print(Fore.GREEN + Style.BRIGHT + f"Welcome, {username}!" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid username or password." + Style.RESET_ALL)
        print(Fore.RED + "(If you not registered yourself! Do that First)" + Style.RESET_ALL)
        print(Fore.RED + "(If registered! Try login again)" + Style.RESET_ALL)
        return False
