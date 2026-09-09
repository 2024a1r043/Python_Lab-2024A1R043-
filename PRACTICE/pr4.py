#Write a python program to calculate the final bill amount after applying a discount. The program should take the total bill amount as input from the user and apply the discount according to the following rules. After calculating the discount, the program should display the dicount amount and  the final bill amount payable by the customer.
#Bill amount                      Discount
#Above 5000                         20%
#3000 to 5000                        10%
#Below 3000                          No discount
total_bill = float(input("Enter the total bill amount: "))
if total_bill > 5000:
    discount = total_bill * 0.20
elif 3000 <= total_bill <= 5000:
    discount = total_bill * 0.10
else:
    discount = 0
final_bill = total_bill - discount
print(f"Discount amount: {discount}")
print(f"Final bill amount payable: {final_bill}")