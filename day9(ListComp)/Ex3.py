'''
Exercise 3 — Double the Numbers
Given:
numbers = [1, 2, 3, 4, 5]
Create:
[2, 4, 6, 8, 10]
'''

def double(numbers):
    double_num=[number*2 for number in numbers]
    return double_num

numbers = [1, 2, 3, 4, 5]
result=double(numbers)
print(result)