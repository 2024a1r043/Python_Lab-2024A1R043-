choice = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ").upper()

if choice == "C":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif choice == "F":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid choice")