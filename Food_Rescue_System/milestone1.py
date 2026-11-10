
# Milestone 1: Record One Donation and Estimate Meal Support

MEAL_SIZE_KG = 0.40

print("=" * 50)
print("FOOD RESCUE SYSTEM - RECORD ONE DONATION")
print("=" * 50)

# Accept donation details from user
donor_name = input("Enter donor name: ")
food_category = input("Enter food category: ")

quantity_kg = float(input("Enter quantity (kg): "))
hours_remaining = int(input("Enter hours before expiry: "))

# Display data types
print("\nData type of quantity:", type(quantity_kg))
print("Data type of hours remaining:", type(hours_remaining))

# Calculate estimated meals
estimated_meals = int(quantity_kg / MEAL_SIZE_KG)

# Calculate leftover food
leftover_kg = round(
    quantity_kg - estimated_meals * MEAL_SIZE_KG, 2
)

# Format donor name and food category
clean_donor = donor_name.strip().title()
clean_category = food_category.strip().upper()

# Display donation summary
print("\n" + "=" * 50)
print("DONATION SUMMARY")
print("=" * 50)

print("Donor Name       :", clean_donor)
print("Food Category    :", clean_category)
print("Quantity         :", quantity_kg, "kg")
print("Hours Remaining  :", hours_remaining, "hours")
print("Meal Size Assumed:", MEAL_SIZE_KG, "kg")
print("Estimated Meals  :", estimated_meals)
print("Leftover Food    :", leftover_kg, "kg")

print("=" * 50)
