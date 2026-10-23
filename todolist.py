from datetime import datetime

todo_list = []

while True:
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

    choice = input("Do you want to add another task? (yes/no): ")

    if choice.lower() == "no":
        break

todo_list.sort(
    key=lambda x: datetime.strptime(x["time"], "%I:%M %p").time()
)

print("\n========== MY TO-DO LIST ==========")

for i, todo in enumerate(todo_list, start=1):
    print(f"{i}. Task: {todo['task']}")
    print(f"   Time: {todo['time']}")
    print("-----------------------------------")