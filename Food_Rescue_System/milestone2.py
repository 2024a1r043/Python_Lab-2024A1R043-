
# Milestone 2: Process Multiple Donations

MEAL_SIZE_KG = 0.40

donations = []
food_categories = set()

print("=" * 50)
print("FOOD RESCUE SYSTEM - MULTIPLE DONATIONS")
print("=" * 50)

while True:

    donor_name = input("\nEnter donor name (DONE to finish): ")

    if donor_name.strip().upper() == "DONE":
        break

    food_category = input("Enter food category: ")

    quantity_kg = float(input("Enter quantity (kg): "))
    hours_remaining = int(input("Enter hours before expiry: "))

    # Reject invalid donations
    if quantity_kg <= 0 or hours_remaining <= 0:
        print("Invalid donation! Enter positive values.")
        print("Please enter the donation again.")
        continue

    # Calculate estimated meals
    estimated_meals = int(quantity_kg / MEAL_SIZE_KG)

    # Classify donation priority
    if hours_remaining <= 4:
        priority = "CRITICAL"
    elif hours_remaining <= 12:
        priority = "PRIORITY"
    else:
        priority = "NORMAL"

    # Store donation in list
    donation = {
        "donor": donor_name.strip().title(),
        "category": food_category.strip().upper(),
        "quantity": quantity_kg,
        "hours": hours_remaining,
        "meals": estimated_meals,
        "priority": priority
    }

    donations.append(donation)
    food_categories.add(food_category.strip().upper())

    print("\nDonation Accepted!")
    print("Donor Name:", donation["donor"])
    print("Estimated Meals:", estimated_meals)
    print("Priority:", priority)


# Display final summary
print("\n" + "=" * 50)
print("FINAL DONATION SUMMARY")
print("=" * 50)

total_quantity = 0
total_meals = 0

critical_count = 0
priority_count = 0
normal_count = 0

for donation in donations:

    print("\nDonor:", donation["donor"])
    print("Category:", donation["category"])
    print("Quantity:", donation["quantity"], "kg")
    print("Hours Remaining:", donation["hours"])
    print("Estimated Meals:", donation["meals"])
    print("Priority:", donation["priority"])

    total_quantity += donation["quantity"]
    total_meals += donation["meals"]

    if donation["priority"] == "CRITICAL":
        critical_count += 1

    elif donation["priority"] == "PRIORITY":
        priority_count += 1

    else:
        normal_count += 1


print("\n========== TOTAL SUMMARY ==========")

print("Total Donations:", len(donations))
print("Total Quantity:", total_quantity, "kg")
print("Total Estimated Meals:", total_meals)

print("CRITICAL Donations:", critical_count)
print("PRIORITY Donations:", priority_count)
print("NORMAL Donations:", normal_count)

print("Unique Food Categories:", food_categories)

print("\nThank you for using Food Rescue System!")
