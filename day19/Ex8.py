'''
Problem 8 — Find Duplicate Numbers
nums = [1, 2, 3, 2, 4, 5, 1]
'''
def duplicate(nums):
    new = set()
    for num in nums:
        if num in new:
            return("Duplicate found")
        else:
            new.add(num)
nums = [1, 2, 3, 2, 4, 5, 1]
dup=duplicate(nums)
print(dup)