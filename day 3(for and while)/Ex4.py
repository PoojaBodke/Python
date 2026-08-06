'''
Exercise 4
Ask the user for a number n.
Calculate:
1 + 2 + 3 + ... + n
'''
number=int(input("Enter a number: "))
sum=0
for i in range(1,number+1):
    sum=sum+i
    i+=1
print(sum)