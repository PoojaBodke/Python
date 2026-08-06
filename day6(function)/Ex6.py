def largest(nums):
    first=float("-inf")
    second=float("-inf")
    third=float("-inf")
    for num in nums:
        if num>first:
            third = second
            second=first
            first=num 
        elif num>second:
            third=second
            second=num
        elif num>third:
            third=num
        else:
            num
    return third
            
nums=[2,3,4,10, 8,8, 7, 1]
print(largest(nums))
