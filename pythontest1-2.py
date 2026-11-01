print("Q1-pattern")
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print("*" * i)

print("stopped")

print("Q2-multipliaction table")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("stopped")

print("Q3-student Id")

students = [
    {"id": 1, "name": "rajesh"},
    {"id": 2, "name": "rahul"},
    {"id": 3, "name": "sruthi"}
]

search_id = int(input("Enter student ID: "))

for student in students:
    if student["id"] == search_id:
        print("Student Name:", student["name"])
        break
else:
    print("Student not found")

print("stopped")

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

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", calc.addition(num1, num2))
print("Subtraction:", calc.subtraction(num1, num2))
print("Multiplication:", calc.multiplication(num1, num2))

if num2 != 0:
    print("Division:", calc.division(num1, num2))
else:
    print("Division by zero is not possible")