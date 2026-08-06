'''
Exercise 2
Ask the user to enter 5 numbers.
Store them in a list.
Then print the complete list.
'''
numbers=[]
for i in range(0,5):
    number=int(input("Enter number"))
    numbers.append(number)
print(numbers)