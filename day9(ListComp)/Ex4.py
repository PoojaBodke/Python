'''
Exercise 4 — Strings
Given:
names = ["pooja", "rohit", "john", "alice"]
Create a new list containing all names in uppercase.
Expected:
["POOJA", "ROHIT", "JOHN", "ALICE"]
'''
names = ["pooja", "rohit", "john", "alice"]
words=[name.upper() for name in names]
print(words)