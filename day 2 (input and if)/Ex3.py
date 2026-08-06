'''
Exercise 3
Ask the user for marks.
Print:
90 and above → A
75–89 → B
60–74 → C
Below 60 → Fail
'''
marks = int(input("Enter your marks: "))
if marks>=90:
    print("A")
elif marks>=75 and marks<=89:
    print("B")
elif marks>=60 and marks<=74:
    print("C")
else:
    print("fail")