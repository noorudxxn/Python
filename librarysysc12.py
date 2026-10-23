import re

try:
    title = input("Enter book title: ")
    year = input("Enter publication year: ")

    if not re.fullmatch(r'[A-Za-z ]+', title):
        raise ValueError("Invalid book title! Use only alphabets and spaces.")

    if not re.fullmatch(r'(19|20)\d{2}', year):
        raise ValueError("Invalid publication year! Enter a 4-digit year starting with 19 or 20.")

    print("Book title:", title)
    print("Publication year:", year)
    print("Book details accepted successfully.")

except ValueError as e:
    print("Error:", e)

finally:
    print("Library system execution completed.")