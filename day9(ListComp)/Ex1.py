'''
Exercise 1 — Squares
Create a list containing the squares of numbers 1–10.
Expected:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Use a list comprehension.
'''
square=[x**2 for x in range(1,11)]
print(square)