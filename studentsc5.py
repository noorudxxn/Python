
Python = {"Rahul", "Asha", "Glen"}
Data_Science = {"Asha", "Yasir", "Neha"}

print("Python Students:", Python)
print("Data Science Students:", Data_Science)

Python.add("Sajith")
print("After adding a student:", Python)

Data_Science.remove("Yasir")
print("After removing a student:", Data_Science)

both_courses = Python.intersection(Data_Science)
print("Students in both courses:", both_courses)

python_only = Python.difference(Data_Science)
print("Students only in Python:", python_only)

all_students = Python.union(Data_Science)
print("All students:", all_students)

course_students = {
    "Python": len(Python),
    "Data Science": len(Data_Science)
}

for course, count in course_students.items():
    print(f"Course: {course}, Students: {count}")

expected_growth = {
    course: count * 2
    for course, count in course_students.items()
}

print("Expected growth:", expected_growth)