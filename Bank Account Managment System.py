class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        before_balance = self.balance
        self.balance += amount
        print(f"Deposited: {amount} | Previous Balance: {before_balance} | Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        before_balance = self.balance
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount} | Previous Balance: {before_balance} | Current Balance: {self.balance}")
            if self.balance < 1000:
                print("Warning: Low funds in your account!")
        else:
            print("Not enough funds to withdraw!")

    def check_balance(self):
        print(f"Current Balance for {self.owner}: {self.balance}")


# Create account
account = BankAccount("Muhib Khan", 250000)

# Interactive menu
menus = ["Check Balance", "Withdraw", "Deposit", "Exit"]

while True:
    print("\nSelect your preferred operation:")
    for i, menu in enumerate(menus, start=1):
        print(f"{i}. {menu}")

    user_input = input("Enter your choice: ").strip()

    try:
        # If input is a number
        if user_input.isdigit():
            choice = int(user_input)
            if choice == 1:
                account.check_balance()
            elif choice == 2:
                amount = int(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == 3:
                amount = int(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == 4:
                print("Exiting! Thank you for using the Bank Account Management System.")
                break
            else:
                print("Invalid choice! Please enter a number between 1-4.")
        else:
            print("Invalid input! Please enter a number between 1-4.")

    except ValueError:
        print("Invalid number! Please enter digits only.")
