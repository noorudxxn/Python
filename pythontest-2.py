print("Q2-multipliaction table")
while True:

    try:
        num = int(input("Enter a number: "))

        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    choice = input("\nDo you want to continue? (yes/no): ").lower()

    if choice == "yes":
        continue

    else:
        print("Program exited. Thank you!")
        break