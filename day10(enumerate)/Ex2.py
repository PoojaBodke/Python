'''
Given:
numbers = [10, 20, 30, 40, 50]
Print:
Index: 0, Value: 10
Index: 1, Value: 20
Use enumerate().
'''
numbers = [10, 20, 30, 40, 50]
for i,number in enumerate(numbers):
    print(f"Index: {i}, Value: {number}")