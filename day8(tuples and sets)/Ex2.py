
'''
Create:
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
Convert it into a set and print it.
Expected:
{1, 2, 3, 4, 5}
'''
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
num=set()
for number in numbers:
    num.add(number)
print(num)
