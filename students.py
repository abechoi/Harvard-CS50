import csv

students = []
    
with open("students.csv") as file:
    # DictReader returns a dictionary for each row, unlike default reader which returns a list
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

"""
def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]
"""

# lambda student: student["name"] = returns student["name"] for each student of students
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} of {student['home']}")