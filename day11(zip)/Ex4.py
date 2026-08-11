'''
Exercise 4 — Interview Style
Given:
students = ["Pooja", "Rahul", "Alice", "John"]
marks = [90, 65, 88, 45]
Create a dictionary containing only students who scored 75 or above.
Expected:

{
    "Pooja": 90,
    "Alice": 88
}
'''
students = ["Pooja", "Rahul", "Alice", "John"]
marks = [90, 65, 88, 45]
result={}
for student,mark in zip(students,marks):
    if mark>=75:
        result[student]=mark
print(result)
