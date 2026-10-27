import os

filename = "students.txt"

if os.path.exists(filename):
    print("Existing student names:")

    with open(filename, "r") as file:
        print(file.read())

else:
    print("No existing student file found.")

n = int(input("\nHow many student names do you want to add? "))

with open(filename, "a") as file:
    for i in range(n):
        name = input(f"Enter student name {i + 1}: ")
        file.write(name + "\n")

print("\nUpdated list of student names:")

with open(filename, "r") as file:
    print(file.read())