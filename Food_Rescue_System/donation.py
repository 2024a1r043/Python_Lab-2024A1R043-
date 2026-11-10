class FoodDonation:

    MEAL_SIZE_KG = 0.40

    def __init__(self, donor_name, food_category, quantity_kg, hours_to_expiry):
        self.donor_name = donor_name
        self.food_category = food_category
        self.quantity_kg = quantity_kg
        self.hours_to_expiry = hours_to_expiry
        self.hours_remaining = hours_to_expiry

    def estimated_meals(self):
        return int(self.quantity_kg / self.MEAL_SIZE_KG)

    def priority_level(self):
        if self.hours_to_expiry <= 4:
            return "CRITICAL"
        elif self.hours_to_expiry <= 12:
            return "PRIORITY"
        else:
            return "NORMAL"

    def __str__(self):
        return (
            f"Donor: {self.donor_name}, "
            f"Food: {self.food_category}, "
            f"Quantity: {self.quantity_kg} kg, "
            f"Hours Remaining: {self.hours_to_expiry}, "
            f"Priority: {self.priority_level()}"
        )