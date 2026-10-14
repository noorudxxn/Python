balance = 1000

def deposit(balance):
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Deposit successful!")
    return balance

def withdrawal(balance):
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")
    return balance

def check_balance(balance):
    print("Balance:", balance)

while True:
    print("\n1. Deposit")
    print("2. Withdrawal")
    print("3. Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        balance = deposit(balance)
    elif choice == 2:
        balance = withdrawal(balance)
    elif choice == 3:
        check_balance(balance)
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")