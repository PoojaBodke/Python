'''
Exercise 4 — Interview/Real-world
Given:
data = '{"employees": [{"name": "Pooja", "role": "ML Engineer"}, {"name": "John", "role": "Data Scientist"}]}'
Convert it using json.loads().
Then print:
Pooja → ML Engineer
John → Data Scientist
You'll need to combine:
JSON + dictionary + list + loop
This is exactly the kind of code you'll encounter when working with APIs.
'''
import json
data = '{"employees": [{"name": "Pooja", "role": "ML Engineer"}, {"name": "John", "role": "Data Scientist"}]}'
data_new=json.loads(data)
employees=data_new["employees"]
for employee in employees:
    print(f'{employee["name"]}->{employee["role"]}')

