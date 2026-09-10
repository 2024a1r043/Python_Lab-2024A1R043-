#Write a python program that asks the user to enter a username and password. The user should get only 3 attempts. If the correct credentials are entered, display "login Successful" and stop the loop. if all attempts are used, display "Account locked"
username=input("Enter username:")
password=input("Enter password:")
for i in range(3):
    if username=="Bhawanamanhas" and password=="Bhawana@123_":
        print("Login Successful")
        break
    else:
        print("Account Locked")

