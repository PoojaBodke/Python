'''
Given:
numbers = [5, 8, 12, 3, 20]
Find and print the index of 12.
Expected:
2
'''
numbers = [5, 8, 12, 3, 20]
for i,number in enumerate(numbers):
    if number==12:
        print(i)