from donation import FoodDonation
from rescue_utils import (
    display_donations,
    sort_donations,
    summarize_donations,
    save_donation,
    read_donations
)

donations = []

print("=== FOOD RESCUE SYSTEM ===")

while True:
    donor = input("\nEnter donor name (or DONE to finish): ")

    if donor.upper() == "DONE":
        break

    category = input("Enter food category: ")

    try:
        quantity = float(input("Enter food quantity in kg: "))
        hours = int(input("Enter hours remaining: "))

        if quantity <= 0 or hours <= 0:
            print("Quantity and hours must be positive.")
            continue

        donation = FoodDonation(
            donor, category, quantity, hours
        )

        donations.append(donation)
        save_donation(donation)

        print("Donation saved successfully!")

    except ValueError:
        print("Please enter valid numeric values.")

print("\n--- Current Donations ---")
display_donations(donations)

print("\n--- Sorted Donations ---")
sorted_donations = sort_donations(donations)
display_donations(sorted_donations)

summarize_donations(donations)

print("\n--- Saved Records ---")
saved_records = read_donations()

for record in saved_records:
    print(record)