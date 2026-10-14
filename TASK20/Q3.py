#Create a Product class with the product name, price, and quantity. Add an instance method to calculate the total cost. Take thse values from the userand
#display the product name and total cost
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity
name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))
product1 = Product(name, price, quantity)
print(f"Product Name: {product1.name}")
print(f"Total Cost: {product1.calculate_total()}")