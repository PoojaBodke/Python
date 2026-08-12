'''
Exercise 3 
Create this dictionary:
student = {
    "name": "Pooja",
    "degree": "Computer Science",
    "skills": ["Python", "Machine Learning", "SQL"]
}
Save it into:
student.json
using json.dump().
Then open the file again and read it using json.load().
Print the student's:
name
degree
skills
'''
import json
student = {
    "name": "Pooja",
    "degree": "Computer Science",
    "skills": ["Python", "Machine Learning", "SQL"]
}

with open("student.json","w") as file:
    json.dump(student,file)
with open("student.json","r") as file:
    student_new=json.load(file)
print(student_new["name"])
print(student_new["degree"])
print(student_new["skills"])
