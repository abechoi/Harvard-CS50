"""
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
num = 0

for i in range(len(students)):
    num += 1
    print(num, students[i])
"""
    
# dictionary

"""
students = {
"Hermione": "Gryffindor", 
"Harry": "Gryffindor", 
"Ron": "Gryffindor", 
"Draco": "Slytherin"
}
for student in students:
print(student, students[student], sep=", ")
"""

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}, 
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}, 
    {"name": "Ron", "house": "Gryffindor", "patronus": "Dog"}, 
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]


for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")