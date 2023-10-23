import csv

"""
students = []
    
with open("students.csv") as file:
    # DictReader returns a dictionary for each row, unlike default reader which returns a list
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
    
# lambda student: student["name"] = returns student["name"] for each student of students
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} of {student['home']}")
"""

name = input("Enter name: ")
home = input("Enter home: ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})














