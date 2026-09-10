#Write a python program to creste a simple password validation system.
#THe program should repeatedly ask the user to entera password until a valid password is entered. A password will b e considered valid only if it has at least 8 characters and contains the @ symbol.
#Once the user enters a valid password, the program should display "Password accepted" and stop. Otherwise, it should display "Weak password.Try again" and ask for the password again.
while True:
    p = input("Enter password:")

    if len(p) >= 8 and '@' in p:
        print("Password accepted")
        break
    else:
        print("Weak password. Try again.")