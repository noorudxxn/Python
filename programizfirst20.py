# 1. Python Program to Print Hello World!
print("Q1")
print("Hello, World!")


# 2. Python Program to Add Two Numbers
print("Q2")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2

print("The sum is", sum)


# 3. Python Program to Find the Square Root
print("Q3")
num = float(input("Enter a number: "))

sqrt = num ** 0.5

print("The square root is", sqrt)


# 4. Python Program to Calculate the Area of a Triangle
print("Q4")
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("The area of the triangle is", area)


# 5. Python Program to Solve a Quadratic Equation
print("Q5")

import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("This is not a quadratic equation.")
else:
    d = (b ** 2) - (4 * a * c)

    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)

    print("Root 1 =", root1)
    print("Root 2 =", root2)


# 6. Python Program to Swap Two Variables
print("Q6")

x = input("Enter first value: ")
y = input("Enter second value: ")

temp = x
x = y
y = temp

print("After swapping:")
print("First value =", x)
print("Second value =", y)


# 7. Python Program to Generate a Random Number
print("Q7")
import random

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

if start <= end:
    print("Random number =", random.randint(start, end))
else:
    print("Invalid range")


# 8. Python Program to Convert Kilometers to Miles
print("Q8")

kilometers = float(input("Enter distance in kilometers: "))

miles = kilometers * 0.621371

print("Distance in miles =", miles)


# 9. Python Program to Convert Celsius to Fahrenheit
print("Q9")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 1.8) + 32

print("Temperature in Fahrenheit =", fahrenheit)


# 10. Python Program to Check Positive, Negative, or Zero
print("Q10")

num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# 11. Python Program to Check Odd or Even
print("Q11")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 12. Python Program to Check Leap Year
print("Q12")

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# 13. Python Program to Find the Largest Among Three Numbers
print("Q13")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number =", a)
elif b >= a and b >= c:
    print("Largest number =", b)
else:
    print("Largest number =", c)


# 14. Python Program to Check Prime Number
print("Q14")

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


# 15. Python Program to Print All Prime Numbers in an Interval
print("Q15")

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers are:")

for num in range(max(2, lower), upper + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)


# 16. Python Program to Find the Factorial of a Number
print("Q16")

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    factorial = 1

    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial =", factorial)


# 17. Python Program to Display the Multiplication Table
print("Q17")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 18. Python Program to Print the Fibonacci Sequence
print("Q18")

n = int(input("How many terms? "))

a = 0
b = 1

if n <= 0:
    print("Enter a positive number")
else:
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()


# 19. Python Program to Check Armstrong Number
print("Q19")

num = int(input("Enter a number: "))

if num < 0:
    print("Not an Armstrong number")
else:
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == num:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")


# 20. Python Program to Find Armstrong Numbers in an Interval
print("Q20")

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Armstrong numbers are:")

for num in range(max(0, lower), upper + 1):
    digits = len(str(num))
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == num:
        print(num)
    