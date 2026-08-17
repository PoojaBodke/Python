'''
Problem 5 — Count Positive & Negative
Now we're going to combine patterns.
Given:
nums = [5, -2, 8, -10, 3, -7, 0]

Find:
Positive numbers = 3
Negative numbers = 3
Don't count 0 as either positive or negative.
'''
nums = [5, -2, 8, -10, 3, -7, 0]
positive=0
negative=0
for num in nums:
    if num>0:
        positive+=1
    elif num<0:
        negative+=1
    else:
        print("Neither Positive Nor Negative")
print(positive)
print(negative)