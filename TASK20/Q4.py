#Create a Product class 
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance  
    def deposit(self, amount):
        self.balance += amount
       
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount  
            print(f"Withdrawal successful. New balance: {self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance}")
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))
account = BankAccount(name, balance)
deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)
withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)
account.display_balance()