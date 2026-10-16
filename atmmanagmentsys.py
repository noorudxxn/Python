class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))

        if amount > 0:
            self.balance += amount
            self.transactions.append("Deposited: " + str(amount))
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount <= self.balance:
            self.balance -= amount
            self.transactions.append("Withdrawn: " + str(amount))
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)

    def transaction_history(self):
        print("\nTransaction History:")

        if len(self.transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))


while True:
    print("\n----- BANK MANAGEMENT SYSTEM -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Bank.deposit()

    elif choice == "2":
        Bank.withdraw()

    elif choice == "3":
        Bank.check_balance()

    elif choice == "4":
        Bank.transaction_history()

    elif choice == "5":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Please try again.")

account = Bank(name, balance)
account.display_menu()