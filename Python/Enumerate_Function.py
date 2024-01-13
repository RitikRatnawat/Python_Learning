"""Learning about the Enumerate Function in Python."""

marks = [50, 68, 79, 49, 90, 82]

print("0-Indexing")
print("----------"*5)
for index, mark in enumerate(marks):
    print("Student", index, ":", mark)

print()

print("1-Indexing")
print("----------"*5)
for index, mark in enumerate(marks, start=1):
    print("Student", index, ":", mark)