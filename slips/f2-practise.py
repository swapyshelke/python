# Write a Python class BankAccount with attributes like account_number, balance,
# date_of_opening and customer_name, and methods like deposit, withdraw, and
# check_balance. 

class BankAccount:
    def __init__(self, account_number, initial_balance = 0, date_of_opening, customer_name):
        self.balance = balance
        self.account_number = account_number
        self.balance = initial_balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"amount deposited {amount}. Total amount {self.balance}")
        else:
            print("money should be positive \n")
            
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount