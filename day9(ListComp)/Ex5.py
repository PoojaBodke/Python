'''
Exercise 5 — Interview Style
Given:
numbers = [3, 8, 12, 5, 7, 20, 1]
Create a list containing numbers greater than 10.
Expected:
[12, 20]
'''

numbers = [3, 8, 12, 5, 7, 20, 1]
result=[number for number in numbers if number>10]
print(result)


