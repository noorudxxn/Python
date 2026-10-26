import os

item = input("Enter the name of a new item: ")

if os.path.exists("items.txt"):
    with open("items.txt", "a") as file:
        file.write(item + "\n")
else:
    with open("items.txt", "w") as file:
        file.write(item + "\n")

print("\nList of Items:")

with open("items.txt", "r") as file:
    print(file.read())