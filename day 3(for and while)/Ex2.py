'''
Exercise 2
Print all even numbers between 1 and 20.
Try to use range() cleverly instead of checking each number with an if.
'''
for i in range(1,21):
    if i%2==0:
        print(i)
        i+=1
    