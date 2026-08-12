'''
Exercise 1
Create:
student = {
    "name": "Pooja",
    "age": 24,
    "skills": ["Python", "SQL", "Machine Learning"]
}
Convert it into a JSON string using json.dumps().
Print it.
'''
import json
student = {
    "name": "Pooja",
    "age": 24,
    "skills": ["Python", "SQL", "Machine Learning"]
}
json_data=json.dumps(student)
print(json_data)
