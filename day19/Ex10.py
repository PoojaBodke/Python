'''
Problem 10 — Two Sum
Given:
nums = [2, 7, 11, 15]
target = 9
Find the indices of the two numbers that add up to target.
Expected:
[0, 1]
'''
nums = [2, 7, 11, 15]
seen={}
target=9
for i in range (len(nums)):
    complement=target-nums[i]
    if complement in seen:
        print(seen[complement],i)
    seen[nums[i]]=i
