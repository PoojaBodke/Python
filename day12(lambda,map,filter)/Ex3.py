'''
Exercise 3 — filter()
Given:
numbers = [5, 12, 3, 18, 7, 20]
Use filter() to keep numbers greater than 10.
Expected:
[12, 18, 20]
'''
numbers = [5, 12, 3, 18, 7, 20]
greater=list(filter(lambda x: x>10,numbers))
print(greater)