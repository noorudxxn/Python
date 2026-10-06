paragraph = """
Python is a popular programming language.
This Python course teaches the basics of Python programming.
It is a beginner-friendly course for learning Python.
"""

print("Length of paragraph:", len(paragraph))

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

print("Preview:", paragraph[:50])

paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacement:")
print(paragraph)

paragraph = paragraph.lower()

paragraph = paragraph.strip()

words = paragraph.split()
print("\nWords:", words)

if "course" in words:
    print("\nThe word 'course' is found in the paragraph.")

print("\nThe course description is {} characters long and has {} words.".format(len(paragraph), len(words)))
