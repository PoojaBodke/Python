'''
Exercise 2
Given:
products = ["Laptop", "Phone", "Tablet"]
prices = [1000, 700, 400]
Print:
Laptop costs $1000
Phone costs $700
Tablet costs $400
'''
def main(products,prices):
    for product,price in zip(products,prices):
        print(f"{product} costs ${price}")
products = ["Laptop", "Phone", "Tablet"]
prices = [1000, 700, 400]
main(products,prices)