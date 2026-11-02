print("Q3-student Id")

students = [{"id": 1, "name": "rajesh"},
            {"id": 2, "name": "rahul"},
            {"id": 3, "name": "sruthi"}
            ]

while True:

    try:
        search_id = int(input("Enter student ID: "))

        for student in students:
            if student["id"] == search_id:
                print("Student Name:", student["name"])
                break

        else:
            print("Student not found!")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    choice = input("\nDo you want to continue? (yes/no): ").lower()

    if choice == "yes":
        continue

    else:
        print("Program exited. Thank you!")
        break
