
Frontend = {"Rahul", "Asha", "Glen", "Neha"}
Backend = {"Asha", "Yasir", "Glen", "Vishnu"}

print("Frontend Students:", Frontend)
print("Backend Students:", Backend)

Backend.add("Sajith")
print("After adding a student to Backend:", Backend)

Frontend.remove("Neha")
print("After removing a student from Frontend:", Frontend)

both_courses = Frontend.intersection(Backend)
print("Students in both courses:", both_courses)

backend_only = Backend.difference(Frontend)
print("Students only in Backend:", backend_only)

all_students = Frontend.union(Backend)
print("All unique students:", all_students)
print("Total unique students:", len(all_students))

course_count = {
    "Frontend": len(Frontend),
    "Backend": len(Backend)
}

for course, count in course_count.items():
    print(f"Course: {course}, Students: {count}")

course_count_fullstack = {course: count for course, count in course_count.items()}

course_count_fullstack["Fullstack"] = sum(course_count.values())

print("Updated course dictionary:", course_count_fullstack)