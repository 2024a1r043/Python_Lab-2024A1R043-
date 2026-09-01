principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of interest: "))
time = float(input("Enter Time (in years): "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print("Simple Interest:", simple_interest)
print("Total Amount:", total_amount)