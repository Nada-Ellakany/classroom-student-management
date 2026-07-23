print("===== TASK 1: The Class List =====")

students = ["Omar", "Sara", "Ali", "Nour"]

students.append("Youssef")

students.remove("Ali")

first_student = students[0]
last_student = students[-1]
print("First student:", first_student)
print("Last student:", last_student)

total_students = len(students)
print("Total students:", total_students)

for student_name in students:
    print(student_name)


print("\n===== TASK 2: One Student's Profile =====")

student = {
    "name": "Sara",
    "age": 22,
    "gpa": 3.1
}

student["gpa"] = 3.6

student["city"] = "Giza"

del student["age"]

for key in student:
    print(key, "->", student[key])


print("\n===== TASK 3: The Whole Class + Remove Duplicates =====")

classroom = [
    {"name": "Omar", "gpa": 3.5},
    {"name": "Sara", "gpa": 3.9},
    {"name": "Ali", "gpa": 3.2}
]

for one_student in classroom:
    print(one_student["name"], "->", one_student["gpa"])

print("\nHigh performers:")
for one_student in classroom:
    if one_student["gpa"] >= 3.5:
        print(one_student["name"])

signups = ["Omar", "Sara", "Omar", "Ali", "Sara", "Omar"]

unique_signups = set(signups)
print("\nUnique students:", unique_signups)
print("Number of unique students:", len(unique_signups))

is_mona_signed_up = "Mona" in signups
print("Is Mona signed up?", is_mona_signed_up)
