print("Q4-calculator")

class Calculator:

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


calc = Calculator()

while True:

    
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 5:
        print("Thank you for using Calculator!")
        break

    elif choice in [1, 2, 3, 4]:

        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

        except ValueError:
            print("Please enter numbers only!")
            continue

        if choice == 1:
            print("Addition:", calc.addition(num1, num2))

        elif choice == 2:
            print("Subtraction:", calc.subtraction(num1, num2))

        elif choice == 3:
            print("Multiplication:", calc.multiplication(num1, num2))

        elif choice == 4:
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print("Division:", calc.division(num1, num2))

    else:
        print("Invalid choice! Please select between 1 and 5.")