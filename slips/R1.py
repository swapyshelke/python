# Write a Python class BankAccount with attributes like account_number,
# balance, date_of_opening and customer_name, and methods like deposit,
# withdraw, and check_balance. 


class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = 0.0  # Initial balance is set to 0

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        """Check the current balance of the account."""
        print(f"Current balance: ${self.balance:.2f}")

# Example usage
if __name__ == "__main__":
    # Create a new bank account
    account = BankAccount(account_number="123456789", customer_name="John Doe", date_of_opening="2023-01-01")

    # Perform some operations
    account.deposit(500)
    account.withdraw(200)
    account.check_balance()
    account.withdraw(400)  # This should show insufficient funds