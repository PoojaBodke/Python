'''
Exercise 2 — Even Numbers
Given:
numbers = [1, 4, 7, 10, 13, 16, 20]
Create a new list containing only the even numbers.
'''
def even(numbers):
    even_number=[number for number in numbers if number%2==0 ]
    return even_number

numbers = [1, 4, 7, 10, 13, 16, 20]
result=even(numbers)
print(result)