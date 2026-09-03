#Write a python problem to simulate a digital lock system.
#The lock should ask the user to enter a 4-digit pin. if the entered pin does not contain exactly 4 digits, the program should display an error message and ask again. If the entered pin is correct,the lock should open. Otherwise , the program should ask the user to try again
correct_pin = "1234"

while True:
    pin = input("Enter 4-digit PIN: ")

    if len(pin) != 4:
        print("Error: PIN must contain exactly 4 digits.")
    elif pin == correct_pin:
        print("Lock opened!")
        break
    else:
        print("Incorrect PIN. Try again.")