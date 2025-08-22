# Create a BankAccount class with __init__, deposit, withdraw, and check_balance methods to manage deposits, withdrawals (with low-fund warnings),
# and display the current balance.


class Bank:

    def __init__(self, owner, balance):
        self.Owner = owner
        self.Balance = balance

    def deposit(self, amount):
        before_balance = self.Balance

        self.Balance += amount
        print(
            f"The {amount} is deposited into your account,: {before_balance} | Now your Balance is {self.Balance}"
        )
        return

    def withdraw(self, amount):
        before_balance = self.Balance

        found = False
        if self.Balance >= amount:
            self.Balance -= amount

            print(
                f"The {amount} has been withdraw from your current balance: {before_balance} | Your Balance now is {self.Balance}, "
            )
            found = True

        if not found:
            print("Not enough Funds to withdraw !!")

    def check_balance(self):
        print(f"Current Balance : {self.Balance}")
        return


account = Bank("Muhib Khan", 250000)


while True:

    menus = ["Check Balance", "Withdraw", "Deposit", "Exit"]

    print("Select your preferred operation : ")
    for i, menu in enumerate(menus, start=1):

        print(f"{i}. {menu}")

    user = input("Select an option from the Menu : ").strip().title()

    try:

        # If input is a number
        if user.isdigit():
            choice = int(user)

            if choice == 1:
                account.check_balance()

            elif choice == 2:
                amount = int(input("Enter amount to withdraw: "))
                account.withdraw(amount)

            elif choice == 3:
                amount = int(input("Enter amount to deposit: "))
                account.deposit(amount)

            elif choice == 4:
                print("Exiting!!")
                break
            else:
                print("Invalid choice! Please enter between 1-4.")

        elif user == menus[0]:
            account.check_balance()

        elif user == menus[1]:
            user_withdraw = int(input("Enter the amount you want to Withdraw : "))
            account.withdraw(user_withdraw)

        elif user == menus[2]:
            user_deposit = int(input("Enter the amount you want to deposit : "))
            account.deposit(user_deposit)

        elif user == menus[3]:
            print("Exiting !!")
            break

        else:
            print("Invalid Input !!")

    except ValueError:
        print("Invalid number! Please enter digits only")
