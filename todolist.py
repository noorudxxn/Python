from datetime import datetime
import os

todo_list = []
filename = "todo.txt"

# Load existing tasks
if os.path.exists(filename):
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(" | Time: ")

            if len(parts) == 2:
                task = parts[0].replace("Task: ", "", 1)
                time = parts[1]

                todo_list.append({
                    "task": task,
                    "time": time
                })

while True:
    print("\n----- TO-DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")

        while True:
            time = input("Enter time (HH:MM AM/PM): ")

            try:
                valid_time = datetime.strptime(time, "%I:%M %p")
                time = valid_time.strftime("%I:%M %p")
                break

            except ValueError:
                print("Invalid time! Example: 09:30 AM or 05:45 PM")

        todo_list.append({
            "task": task,
            "time": time
        })

        # Save tasks to the text file
        with open(filename, "w") as file:
            for todo in todo_list:
                file.write(
                    f"Task: {todo['task']} | Time: {todo['time']}\n"
                )

        print("Task saved successfully!")

    elif choice == "2":
        if not todo_list:
            print("No tasks available.")

        else:
            todo_list.sort(
                key=lambda x: datetime.strptime(
                    x["time"], "%I:%M %p"
                ).time()
            )

            print("\n========== MY TO-DO LIST ==========")

            for i, todo in enumerate(todo_list, start=1):
                print(f"{i}. Task: {todo['task']}")
                print(f"   Time: {todo['time']}")
                print("-----------------------------------")

    elif choice == "3":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")