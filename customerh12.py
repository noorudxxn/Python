try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    if not name.strip() or not feedback.strip():
        raise ValueError("Name and feedback cannot be empty.")

    print("\nThank you for your feedback,", name)
    print("Your feedback:", feedback)

except ValueError as e:
    print("Error:", e)

finally:
    print("Thank you for visiting our restaurant!")