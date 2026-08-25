#WAP to take an amount in ruppees and calculate how many rs 500 and rs 100 notes are needed
amount = int(input("Enter amount in rupees: "))

notes_500 = amount // 500
remaining = amount % 500

notes_100 = remaining // 100

print("500 rupee notes:", notes_500)
print("100 rupee notes:", notes_100)