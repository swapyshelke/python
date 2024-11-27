# Write a Python class BankAccount with attributes like account_number, balance,
# date_of_opening and customer_name, and methods like deposit, withdraw, and
# check_balance. 


class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, initial_balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: ${amount}. New balance: ${self.balance}.")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return f"Current balance: ${self.balance}"

# Example usage
if __name__ == "__main__":
    # Create a bank account
    account = BankAccount(account_number="123456789", customer_name="John Doe", date_of_opening="2023-01-01", initial_balance=1000)

    # Check balance
    print(account.check_balance())

    # Deposit money
    account.deposit(500)

    # Withdraw money
    account.withdraw(200)

    # Check balance again
    print(account.check_balance())

    # Attempt to withdraw more than the balance
    account.withdraw(2000)