'''
Count how many vowels are in a word.
Example:
Input:
Computer
Output:
Vowels = 3
Don't use any library.
'''
word = str(input("Enter a word"))
sum=0
for ch in word:
    if (ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" ):
        sum=sum+1
print(sum)