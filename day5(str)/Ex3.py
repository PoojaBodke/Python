'''
Exercise 3
Ask the user for a word.
Print whether the length is:
Less than 5 → "Short"
5 or more → "Long"
'''
word = str(input("Enter a word: "))
length= len(word)
if length<5:
    print("Short")
else:
    print("Long")