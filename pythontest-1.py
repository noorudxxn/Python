print("Q1-pattern")
while True:

    try:
        n = int(input("Enter the number of rows: "))


        for i in range(1, n + 1):
            print("*" * i)

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    choice = input("\nDo you want to continue? (yes/no): ").lower()

    if choice == "yes":
        continue

    elif choice == "no":
        print("Program exited. Thank you!")
        break

    else:
        print("Program exited. Thank you!")
        break