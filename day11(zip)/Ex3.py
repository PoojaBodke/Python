'''
Exercise 3
Given:
names = ["Pooja", "Rahul", "Alice"]
ages = [24, 25, 22]
Create a dictionary:

{
    "Pooja": 24,
    "Rahul": 25,
    "Alice": 22
}
'''
def main(names,ages):
    for name,age in zip(names,ages):
        return dict(zip(names,ages))
names = ["Pooja", "Rahul", "Alice"]
ages = [24, 25, 22]
print(main(names,ages))