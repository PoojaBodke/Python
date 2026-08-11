'''
Exercise 4 — Interview Style
Find out whether a list contains duplicates.
Input:
numbers = [1, 2, 3, 4, 2]
Output:
Duplicate found
Don't use:
set(numbers)
to solve the whole problem directly.
Instead, use the seen set pattern I showed above.
'''

numbers = [1, 2, 3, 4, 2, 2]
num=set()
for number in numbers:
    if number in num:
        print("Duplicate Found")
        break
    else:
        num.add(number)
