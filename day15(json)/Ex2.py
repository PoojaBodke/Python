'''
Exercise 2
Given:
data = '{"name": "Pooja", "age": 24, "country": "USA"}'
Convert it into a Python dictionary using json.loads().
Then print:
Pooja
24
USA
'''
import json
data = '{"name": "Pooja", "age": 24, "country": "USA"}'
student=json.loads(data)
print(student["name"])
print(student["age"])
print(student["country"])