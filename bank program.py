class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Example usage
if __name__ == "__main__":
    my_account = BankAccount(123456, "John Doe", "Savings", 1000.0)
    print(f"Initial balance: ${my_account.balance}")

    my_account.deposit(500.0)
    my_account.withdraw(200.0)