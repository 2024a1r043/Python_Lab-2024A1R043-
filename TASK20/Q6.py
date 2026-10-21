#Create an electricitybill class that stores a customer's name and electricity units used. Calculate the bill using these rates: Rs 3 per unit for the first 100 units, Rs 5 per unit for the next 100 units, and Rs 7 per unit for units above 200.
#add a fixed charges of rs50. display the customer's name,units used, and total bill. if the entered units are negative, display an error message.
class ElectricityBill:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def calculate_bill(self):
        if self.units < 0:
            print("Error: Units cannot be negative.")
            return

        bill = 0
        if self.units <= 100:
            bill = self.units * 3
        elif self.units <= 200:
            bill = 100 * 3 + (self.units - 100) * 5
        else:
            bill = 100 * 3 + 100 * 5 + (self.units - 200) * 7

        total_bill = bill + 50
        print(f"Customer Name: {self.name}")
        print(f"Units Used: {self.units}")
        print(f"Total Bill: Rs {total_bill}")
        