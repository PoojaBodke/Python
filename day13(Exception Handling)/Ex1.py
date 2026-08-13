'''
Exercise 1
Write a program that asks the user for a number.
If they enter a valid number:
You entered: 25
If they enter something like "hello":
Invalid number
Use try and except.
'''

try:
    number= int(input("Enter a number: "))
    print(number)
except:
    print("Enter a Valid Number")
