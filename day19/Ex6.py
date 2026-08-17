'''
Problem 6 — Find the Second Largest
Now we're increasing the difficulty a little.
Given:
nums = [10, 5, 8, 20, 15]
Find the second largest number.
Expected:
15
'''
nums = [10, 5, 8, 20, 15]
first=nums[0]
second=nums[1]
for num in nums:
    if first<num:
        
        second=first
        first=num
    elif num>second:
        second=num

print(second)