'''
Exercise 2
Ask the user for a number.
If the number is positive:
Positive Number
Otherwise:
Negative Number
'''
number=int(input("Enter a number: "))
if number>0:
    print("Positive Number")
elif number<0:
    print("Negative Number")
else:
    print("Neither positive nor Negative")