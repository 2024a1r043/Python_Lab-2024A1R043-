
import time

def display_donations(donations):
    for donation in donations:
        print(donation)


def sort_donations(donations):
    return sorted(donations, key=lambda d: d.hours_remaining)


def summarize_donations(donations):
    start_time = time.time()

    total_quantity = sum(d.quantity_kg for d in donations)
    total_meals = sum(d.estimated_meals() for d in donations)

    print("\n--- Donation Summary Report ---")
    print("Total Donations:", len(donations))
    print("Total Food Quantity:", total_quantity, "kg")
    print("Estimated Meals:", total_meals)

    end_time = time.time()
    print("Report Processing Time:", round(end_time - start_time, 6), "seconds")


def save_donation(donation, filename="rescue_records.txt"):
    with open(filename, "a") as file:
        file.write(
            f"{donation.donor_name}|"
            f"{donation.food_category}|"
            f"{donation.quantity_kg}|"
            f"{donation.hours_remaining}\n"
        )


def read_donations(filename="rescue_records.txt"):
    records = []

    try:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    fields = line.strip().split("|")

                    if len(fields) == 5:
                        record_id, donor, category, quantity, hours = fields
                    elif len(fields) == 4:
                        donor, category, quantity, hours = fields
                    else:
                        raise ValueError("Incorrect number of fields")

                    records.append({
                        "donor": donor,
                        "category": category,
                        "quantity": float(quantity),
                        "hours": int(hours)
                    })

                except ValueError:
                    print("Invalid record at line", line_number, "- skipped.")

    except FileNotFoundError:
        print("Error: Donation records file not found.")

    return records