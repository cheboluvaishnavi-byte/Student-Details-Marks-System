# main.py

from student import Marks

# Step 4: Create empty list to store students
students_list = []

# Step 5: Create two student objects
student1 = Marks(101, "Alice", {"Math": 90, "Physics": 85, "Chemistry": 88})
student2 = Marks(102, "Bob", {"Math": 78, "Physics": 82, "Chemistry": 80})

# Add to list
students_list.append(student1)
students_list.append(student2)

# Step 6: Display student details (ID, name, total marks)
print("Student Details:")
for student in students_list:
    sid, name = student.get_details()
    print(f"ID: {sid}, Name: {name}, Total Marks: {student.total_marks()}")

# Step 7: Operations
print("\n--- Step 7 Operations ---")

# 1. Count total number of students
print(f"Total number of students: {len(students_list)}")

# 2. Display only student names
print("Student Names:")
for student in students_list:
    _, name = student.get_details()
    print(name)

# 3. Display ID, name, total marks
print("ID, Name, Total Marks:")
for student in students_list:
    sid, name = student.get_details()
    print(f"{sid}, {name}, {student.total_marks()}")

# 4. Add new subject to student1
student1.add_subject("Biology", 92)
print(f"\nUpdated subjects for {student1._student_name}: {student1.get_subjects()}")

# 5. Update existing mark for student2
student2.update_mark("Physics", 90)
print(f"Updated marks for {student2._student_name}: {student2.get_marks()}")

# 6. Display all subject names of student1
print(f"Subjects of {student1._student_name}: {student1.get_subjects()}")

# 7. Display all marks for student2
print(f"Marks of {student2._student_name}: {student2.get_marks()}")

# 8. Calculate and display average marks of each student
for student in students_list:
    _, name = student.get_details()
    print(f"Average marks of {name}: {student.average_marks():.2f}")

# 9. Student with highest total marks
highest_student = max(students_list, key=lambda s: s.total_marks())
sid, name = highest_student.get_details()
print(f"Student with highest total marks: {name} ({highest_student.total_marks()})")

# 10. Display student names in reverse order
print("Student Names in reverse order:")
for student in reversed(students_list):
    _, name = student.get_details()
    print(name)
