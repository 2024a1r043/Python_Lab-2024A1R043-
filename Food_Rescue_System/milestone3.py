
# Milestone 3: Food Donation Using OOP

MEAL_SIZE_KG = 0.40


# Class for Food Donation
class FoodDonation:

    organization_name = "Food Rescue Organization"

    # Constructor
    def __init__(self, donation_id, donor_name, food_category,
                 quantity_kg, hours_to_expiry):

        self.donation_id = donation_id
        self.donor_name = donor_name
        self.food_category = food_category
        self.quantity_kg = quantity_kg
        self.hours_to_expiry = hours_to_expiry

    # Calculate estimated meals
    def estimated_meals(self):
        return int(self.quantity_kg / MEAL_SIZE_KG)

    # Calculate priority level
    def priority_level(self):
        if self.hours_to_expiry <= 4:
            return "CRITICAL"
        elif self.hours_to_expiry <= 12:
            return "PRIORITY"
        else:
            return "NORMAL"

    # Display donation summary
    def summary(self):
        return (
            f"Donation ID: {self.donation_id}, "
            f"Donor: {self.donor_name}, "
            f"Category: {self.food_category}, "
            f"Quantity: {self.quantity_kg} kg, "
            f"Meals: {self.estimated_meals()}, "
            f"Priority: {self.priority_level()}"
        )

    # String representation
    def __str__(self):
        return (
            f"ID: {self.donation_id} | "
            f"Donor: {self.donor_name} | "
            f"Category: {self.food_category} | "
            f"Pickup Priority: {self.priority_level()}"
        )


# Main Program
print("=" * 50)
print("FOOD RESCUE SYSTEM - OOP")
print("=" * 50)

donations = []

# Create two donation objects using user input
for i in range(2):

    print("\nEnter details for Donation", i + 1)

    donor_name = input("Enter donor name: ")
    food_category = input("Enter food category: ")

    try:
        quantity_kg = float(input("Enter quantity (kg): "))
        hours_to_expiry = int(input("Enter remaining hours: "))

        if quantity_kg <= 0 or hours_to_expiry <= 0:
            print("Invalid values! Please enter positive numbers.")
            continue

        donation = FoodDonation(
            i + 1,
            donor_name.strip().title(),
            food_category.strip().upper(),
            quantity_kg,
            hours_to_expiry
        )

        donations.append(donation)

    except ValueError:
        print("Invalid input! Please enter numeric values.")


# Display donation objects
print("\n========== DONATION DETAILS ==========")

for donation in donations:
    print(donation)

# Display detailed summaries
print("\n========== DETAILED SUMMARY ==========")

for donation in donations:
    print(donation.summary())

print("\nOrganization:", FoodDonation.organization_name)
print("\nThank you for using Food Rescue System!")
