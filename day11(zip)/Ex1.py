'''
Exercise 1
Given:
names = ["Pooja", "Rahul", "Alice"]
scores = [90, 85, 95]
Print:
Pooja scored 90
Rahul scored 85
Alice scored 95
'''
def main(names,scores):
    for name, score in zip(names,scores):
        print(f"{name} scored {score}")

names = ["Pooja", "Rahul", "Alice"]
scores = [90, 85, 95]
main(names,scores)